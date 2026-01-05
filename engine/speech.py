import pyttsx3

def speak(text):
    engine = pyttsx3.init()
    
    voices = engine.getProperty('voices')

    if len(voices) > 0:
        engine.setProperty('voice', voices[0].id) 
    
    engine.setProperty('rate', 190) 
    
    print(f"Jarvis: {text}")
    engine.say(text)
    engine.runAndWait()

if __name__ == "__main__":
    speak("Initialization successful. I am ready.")
