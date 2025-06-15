# 🤖 JARVIS - Your Personal Voice Assistant (Python)

JARVIS is a voice-activated AI assistant built using Python. It can perform a wide variety of tasks including telling time, searching Wikipedia, sending WhatsApp messages, taking screenshots, playing songs on YouTube, checking the weather, and more — all with your voice!

---

## 🧠 Features

- 🕒 Tells time and date
- 🌐 Wikipedia search (voice-based)
- 📱 Send WhatsApp messages via browser
- 🌦️ Weather updates for any city
- 🧮 Voice-based calculator
- 📸 Takes screenshots
- 📂 Opens applications (e.g., Notepad, Chrome, Calculator)
- 🔋 Checks system battery status
- 😂 Tells programming jokes
- ⏱️ Timer with voice alerts
- 📜 Voice note-taking
- 🎵 Plays songs on YouTube
- 🔒 System lock, restart, and shutdown

---

## 🎙️ Technologies Used

- `pyttsx3` - Text-to-speech
- `speech_recognition` - Speech-to-text
- `wikipedia` - Fetching summaries
- `pyautogui` - GUI automation (e.g., taking screenshots, sending keys)
- `pyjokes` - Programming jokes
- `psutil` - System battery and performance
- `pywhatkit` - Play songs on YouTube
- `requests` - For fetching weather via `wttr.in`
- `subprocess`, `os`, `webbrowser`, `datetime` - Native Python modules

---

## ⚙️ Setup Instructions

1. **Clone the repository:**
   git clone https://github.com/your-username/jarvis-assistant.git
   cd jarvis-assistant
Install required dependencies:

pip install -r requirements.txt
Run the assistant:


python jarvis.py
📦 Requirements
Ensure you have the following libraries installed:

pyttsx3
speechrecognition
pyautogui
wikipedia
requests
pyjokes
psutil
pywhatkit

You can install them all via:

pip install pyttsx3 SpeechRecognition pyautogui wikipedia requests pyjokes psutil pywhatkit
Also install pyaudio:


pip install pyaudio
Note: On Windows, if you have trouble installing PyAudio, use:


pip install pipwin
pipwin install pyaudio
