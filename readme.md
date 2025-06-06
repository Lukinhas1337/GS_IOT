# 🚨 Guardian Grid - Detector de Gestos para Emergências

<div align="center">
  <img src="https://img.shields.io/badge/Python-3.10%2B-blue">
  <img src="https://img.shields.io/badge/MediaPipe-0.10.11-orange">
  <img src="https://img.shields.io/badge/OpenCV-4.9.0-green">
  <a href="https://youtu.be/qXyvo8B5c2I"><img src="https://img.shields.io/badge/Video_Demo-YouTube-red"></a>
</div>

---

## 📝 Descrição

**Guardian Grid** é um sistema de reconhecimento de gestos voltado para situações de emergência, especialmente durante apagões. Desenvolvido com **Python**, **MediaPipe** e **OpenCV**, o sistema identifica gestos mesmo em ambientes com **baixa luminosidade** e emite **alertas sonoros** automaticamente.

---

## 🎥 Vídeo Demonstrativo

▶️ Assista aqui: [https://youtu.be/qXyvo8B5c2I](https://youtu.be/qXyvo8B5c2I)

---

## 👥 Equipe

| Nome                         | RM     |
|-----------------------------|--------|
| Lucas Carlos B. Teixeira    | 98640  |
| Júlio César Zampieri        | 98772  |
| João Gabriel D. M. do Nascimento | 99092  |

---

## 🛠️ Funcionalidades

- 📍 Detecção de gestos: **SOS**, **Pedido de ajuda** e **Confirmação**
- 🌑 Funcionamento em **baixa luminosidade**
- 🔊 **Alerta sonoro** ao reconhecer gestos
- 👁️ Interface visual em **tempo real**

---

## ⚙️ Tecnologias

| Tecnologia  | Versão    | Finalidade                   |
|-------------|-----------|------------------------------|
| Python      | 3.10+     | Lógica principal             |
| MediaPipe   | 0.10.11   | Detecção de gestos           |
| OpenCV      | 4.9.0     | Processamento de vídeo       |
| Pygame      | 2.5.2     | Reprodução de sons           |

---

## 🎮 Como Usar

1. Posicione sua mão na frente da **webcam**.
2. Faça um dos gestos abaixo:

   - ✊ **Punho fechado**: Alerta de **SOS**
   - 🤘 **Polegar + mindinho**: Pedido de **ajuda**
   - 👌 **Sinal OK**: Gesto de **confirmação**

3. O sistema irá detectar o gesto e **emitir um som de alerta** correspondente.

---

## 📂 Estrutura do Projeto

```
guardian-grid/
├── gesture_detection.py   # Código principal
├── alert.wav              # Som de alerta
├── requirements.txt       # Dependências
├── README.md              # Este arquivo
└── assets/                # Imagens de exemplo (opcional)
```

---

## 📌 Aplicações Práticas

- 🏥 Apoio em **hospitais** durante quedas de energia
- 🧓 Segurança para **idosos** em casa
- 🆘 Comunicação silenciosa em situações de **emergência**

---

## 📋 Requisitos (requirements.txt)

```
opencv-python==4.9.0.80
mediapipe==0.10.11
numpy==1.26.4
pygame==2.5.2
```

---

<div align="center">Desenvolvido por Lucas (RM98640), Júlio (RM98772) e João (RM99092)</div>
