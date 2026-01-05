# JARVIS: Next-Gen AI Voice Assistant 🤖🦾

**JARVIS** (Just A Rather Very Intelligent System) is a powerful, persona-driven AI agent that transforms your PC into an interactive workspace. Powered by **Google Gemini 1.5 Flash**, it doesn't just chat—it takes action.

## ✨ Key Features

- **🌐 Intelligent Communication**:
  - **WhatsApp**: Multi-step messaging with name extraction and visual navigation.
  - **Email**: Backend Gmail integration to read, summarize, and reply to emails via voice.
- **👁️ Vision System**:
  - Analyze your screen in real-time. Jarvis can explain code, summarize charts, or read documents using Multimodal AI.
- **🎵 Media Mastery**:
  - Context-aware YouTube search and Spotify desktop automation.
- **🖥️ System Control**:
  - Voice-activated app launching, volume control, window switching, and screenshots.
- **🧠 Continuous Awareness**:
  - Runs in a persistent loop with a "Silent Standby" mode. Wakes up to "Hello Jarvis".

## 🛠️ Tech Stack

- **Core**: Python 3.x
- **Brain**: Google Gemini 1.5 Flash (Generative AI SDK)
- **Voice**: `pyttsx3`
- **Hearing**: `SpeechRecognition`
- **Automation**: `PyAutoGUI`, `PyWhatKit`, `AppOpener`

## 🚀 Quick Start (Local Setup)

1. **Clone the Repo**:
   ```bash
   git clone https://github.com/stargazingsapien/Jarvis.git
   ```
2. **Setup Credentials**:
   - Insert your Gemini API Key in `engine/ai.py`.
   - Insert your Gmail App Password in `engine/email_client.py`.
3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
4. **Run Jarvis**:
   ```bash
   python main.py
   ```

---
*Created by Nisarg*
