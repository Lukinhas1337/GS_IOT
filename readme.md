🚨 Guardian Grid - Detector de Gestos para Emergências
<div align="center"> <img src="https://img.shields.io/badge/Python-3.10%2B-blue"> <img src="https://img.shields.io/badge/MediaPipe-0.10.11-orange"> <img src="https://img.shields.io/badge/OpenCV-4.9.0-green"> <a href="https://youtu.be/qXyvo8B5c2I"><img src="https://img.shields.io/badge/Video_Demo-YouTube-red"></a> </div>
📝 Descrição
Sistema de reconhecimento de gestos para situações de emergência durante apagões, desenvolvido com Python e MediaPipe. Detecta gestos específicos mesmo em ambientes com baixa luminosidade e aciona alertas sonoros.

🎥 Vídeo Demonstrativo
https://img.youtube.com/vi/qXyvo8B5c2I/0.jpg

👥 Equipe
Nome	RM
Lucas Carlos Bandeira Teixeira	98640
Júlio César Zampieri	98772
João Gabriel Dias Mello do Nascimento	99092
🛠️ Funcionalidades
✊ Detecção de gestos: SOS, pedido de ajuda e confirmação

🌑 Operação em baixa luminosidade

🔉 Alerta sonoro ao reconhecer gestos

🖥️ Interface visual em tempo real

⚙️ Tecnologias
Tecnologia	Versão	Uso
Python	3.10+	Lógica principal
MediaPipe	0.10.11	Detecção de gestos
OpenCV	4.9.0	Processamento de vídeo
Pygame	2.5.2	Reprodução de sons
📦 Instalação
Clone o repositório:

bash
git clone https://github.com/seu-usuario/guardian-grid.git
cd guardian-grid
Instale as dependências:

bash
pip install -r requirements.txt
Execute:

bash
python gesture_detection.py
🎮 Como Usar
Posicione sua mão frente à webcam

Faça um dos gestos:

✊ Punho fechado: Alerta de SOS

🤘 Polegar + mindinho: Pedido de ajuda

👌 Sinal OK: Confirmação

O sistema emitirá um alerta sonoro

📂 Estrutura do Projeto
text
guardian-grid/
├── gesture_detection.py  # Código principal
├── alert.wav             # Som de alerta
├── requirements.txt      # Dependências
├── README.md             # Este arquivo
└── assets/               # Imagens de exemplo
📌 Aplicações Práticas
🏥 Auxílio em hospitais durante apagões

🏠 Segurança para idosos em residências

🚨 Comunicação em emergências

💻 Código Fonte
python
import cv2
import numpy as np
import mediapipe as mp
import pygame
import time

# Configurações iniciais
pygame.mixer.init()
alert_sound = pygame.mixer.Sound("alert.wav")

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(
    max_num_hands=1,
    min_detection_confidence=0.7,
    min_tracking_confidence=0.5
)
mp_draw = mp.solutions.drawing_utils

# Definir gestos
GESTURES = {
    "SOS": [0, 1, 1, 1, 1],        # Punho fechado
    "AJUDA": [1, 1, 0, 0, 1],      # Polegar + mindinho
    "OK": [0, 1, 1, 0, 0]          # Sinal de OK
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
📋 requirements.txt
text
opencv-python==4.9.0.80
mediapipe==0.10.11
numpy==1.26.4
pygame==2.5.2
<div align="center"> Desenvolvido com ❤️ por Lucas (RM98640), Júlio (RM98772) e João (RM99092) </div> ```