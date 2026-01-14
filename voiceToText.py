# pip install pipwin
# pipwin install pyaudio

import speech_recognition as sr
import pyautogui
import time

# Small delay so you can click Notepad
print("⏳ Switch to Notepad... You have 5 seconds")
time.sleep(5)

recognizer = sr.Recognizer()

with sr.Microphone() as source:
    print("🎤 Speak now...")
    recognizer.adjust_for_ambient_noise(source)
    audio = recognizer.listen(source)

try:
    text = recognizer.recognize_google(audio)
    print("🧠 You said:", text)

    # Type the text slowly (looks real on video)
    pyautogui.write(text, interval=0.05)

except sr.UnknownValueError:
    print("❌ Could not understand audio")

except sr.RequestError as e:
    print("❌ API error:", e)
