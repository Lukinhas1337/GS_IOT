import cv2
import numpy as np
import mediapipe as mp
import pygame
import time

# Configurações iniciais
pygame.mixer.init()
alert_sound = pygame.mixer.Sound("alert.wav")  # Arquivo de som (criar ou substituir)

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(
    max_num_hands=1,
    min_detection_confidence=0.7,
    min_tracking_confidence=0.5
)
mp_draw = mp.solutions.drawing_utils

# Definir gestos (baseado na posição dos dedos)
GESTURES = {
    "SOS": [0, 1, 1, 1, 1],        # Punho fechado (polegar dentro)
    "AJUDA": [1, 1, 0, 0, 1],       # Polegar + mindinho levantados
    "OK": [0, 1, 1, 0, 0]           # Gestos de "OK"
}

def detect_gesture(hand_landmarks):
    finger_tips = [4, 8, 12, 16, 20]  # Pontas dos dedos
    finger_states = []
    
    for tip_id in finger_tips:
        # Verificar se dedo está levantado
        if tip_id == 4:  # Polegar
            finger_states.append(1 if hand_landmarks.landmark[tip_id].x < hand_landmarks.landmark[tip_id-1].x else 0)
        else:
            finger_states.append(1 if hand_landmarks.landmark[tip_id].y < hand_landmarks.landmark[tip_id-2].y else 0)
    
    # Identificar gesto
    for gesture, pattern in GESTURES.items():
        if finger_states == pattern:
            return gesture
    return None

def main():
    cap = cv2.VideoCapture(0)
    last_alert_time = 0
    
    while cap.isOpened():
        success, frame = cap.read()
        if not success:
            continue
        
        # Simular baixa luminosidade
        low_light = cv2.convertScaleAbs(frame, alpha=0.4, beta=0)
        
        # Detectar mãos
        rgb_frame = cv2.cvtColor(low_light, cv2.COLOR_BGR2RGB)
        results = hands.process(rgb_frame)
        
        gesture_detected = None
        
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                mp_draw.draw_landmarks(
                    low_light, hand_landmarks, mp_hands.HAND_CONNECTIONS)
                
                gesture = detect_gesture(hand_landmarks)
                if gesture:
                    gesture_detected = gesture
                    cv2.putText(low_light, f"GESTO: {gesture}", (50, 50),
                                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
                    
                    # Acionar alerta (com debounce)
                    if time.time() - last_alert_time > 5:
                        alert_sound.play()
                        last_alert_time = time.time()
                        print(f"ALERTA ACIONADO! Gestos: {gesture}")
        
        # Mostrar frame
        cv2.imshow('Guardian Grid - Detector de Gestos', low_light)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()