import datetime
import pywhatkit
import wikipedia
import wikipedia
import webbrowser
from AppOpener import open as app_open 
from engine.speech import speak
import pyautogui
import time
import os

def tell_time():
    strTime = datetime.datetime.now().strftime("%H:%M:%S")
    speak(f"The time is {strTime}")

def tell_date():
    strDate = datetime.datetime.now().strftime("%Y-%m-%d")
    speak(f"Today's date is {strDate}")

def play_youtube(query):
    fillers = ['play', 'on youtube', 'youtube', 'open', 'from', 'the', 'video', 'of']
    song = query.lower()
    for word in fillers:
        song = song.replace(word, '')
    
    song = song.strip()
    speak(f"Playing {song} on YouTube")
    pywhatkit.playonyt(song)

def search_google(query):
    fillers = ['search for', 'search', 'google', 'on google', 'find me', 'look up', 'about']
    search_term = query.lower()
    for word in fillers:
        search_term = search_term.replace(word, '')
        
    search_term = search_term.strip()
    speak(f"Searching Google for {search_term}")
    pywhatkit.search(search_term)

def open_app(query):
    app_name = query.lower().replace("open", "").replace("the", "").replace("application", "").replace("app", "").strip()
    speak(f"Opening {app_name}...")
    try:
        app_open(app_name, match_closest=True, output=False)
        speak(f"Opened {app_name}")
    except:
        speak(f"I could not find the application {app_name}")

def search_wikipedia(query):
    speak("Searching Wikipedia...")
    query = query.replace("wikipedia", "").replace("search", "").strip()
    try:
        results = wikipedia.summary(query, sentences=2)
        speak("According to Wikipedia")
        speak(results)
    except wikipedia.exceptions.DisambiguationError:
        speak("There were multiple results, please be more specific.")
    except wikipedia.exceptions.PageError:
        speak("I couldn't find a page for that.")

def play_spotify(query):
    song = query.replace('play', '').replace('spotify', '').replace('on', '').replace('open', '').replace('and', '').replace('the', '').strip()
    
    speak(f"Opening Spotify and attempting to play {song}")

    webbrowser.open(f"spotify:search:{song}")
    
    time.sleep(5) 
    
    pyautogui.press('enter')
    time.sleep(1)
    
    for _ in range(3):
        pyautogui.press('tab')
        time.sleep(0.5)
        pyautogui.press('enter')
        time.sleep(0.5)
    
    speak(f"Playing {song}")

def volume_control(command):
    if "mute" in command:
        pyautogui.press("volumemute")
        speak("System muted")
    elif "up" in command or "increase" in command:
        pyautogui.press("volumeup", presses=5)
        speak("Volume increased")
    elif "down" in command or "decrease" in command:
        pyautogui.press("volumedown", presses=5)
        speak("Volume decreased")

def take_screenshot():
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"screenshot_{timestamp}.png"
    pyautogui.screenshot(filename)
    speak(f"Screenshot taken and saved as {filename}")

def switch_window():
    pyautogui.hotkey("alt", "tab")
    speak("Switched window")

def send_whatsapp(query):
    from engine.listen import take_command
    
    CONTACTS = {
        "dad": "Dad",
        "mom": "Mom",
        "papa": "Dad",
        "mummy": "Mom",
        "part": "Parth", 
        "parth": "Parth",
        "nisarg": "Nisarg",
        "bhai": "Bhai",
        "friend": "Best Friend"
    }

    speak("Opening WhatsApp Web. Sir, please ensure you are logged in and the browser window is focused.")
    webbrowser.open("https://web.whatsapp.com")
    
    contact = ""
    query = query.lower()
    if "message to" in query:
        contact = query.split("message to")[1].strip()
    elif "whatsapp" in query and " to " in query:
        contact = query.split(" to ")[1].strip()
    elif "message" in query and " to " in query:
        contact = query.split(" to ")[1].strip()
        
    time.sleep(10) 
    
    selected_contact = False
    
    while not selected_contact:
        if not contact:
            speak("Whom should I message, Sir?")
            contact = take_command()
            if contact == "None":
                 speak("I didn't catch that. Please say the name again.")
                 continue

        speak(f"Searching for {contact}...")
        
        pyautogui.hotkey('ctrl', 'alt', '/') 
        time.sleep(1)
        pyautogui.hotkey('ctrl', 'a') 
        pyautogui.press('backspace')
        pyautogui.write(contact)
        time.sleep(2) 
        
        speak("Please look at the screen. Say 'Select' to choose, 'Next' to move down, or 'Change' to try a different name.")
        
        while True:
            cmd = take_command(silent=True) 
            
            if "select" in cmd or "yes" in cmd or "ok" in cmd:
                pyautogui.press('enter')
                selected_contact = True
                break
                
            elif "next" in cmd or "down" in cmd:
                pyautogui.press('down')
                
            elif "up" in cmd or "previous" in cmd:
                pyautogui.press('up')
                
            elif "change" in cmd or "wrong" in cmd or "retry" in cmd:
                contact = "" 
                speak("Okay, let's try the name again.")
                break 
                
            elif "cancel" in cmd or "stop" in cmd:
                speak("Cancelling WhatsApp message.")
                return

    speak(f"Contact selected. What is the message?")
    message = take_command()
    if message == "None":
        speak("No message detected. Cancelling.")
        return

    speak(f"Sir, the message is: {message}. Send it?")
    confirmation = take_command()

    if "yes" in confirmation or "send" in confirmation or "sure" in confirmation:
        speak(f"Confirmed. Sending...")
        
        pyautogui.write(message)
        time.sleep(1)
        pyautogui.press('enter')
        
        speak("Message sent.")
    else:
        speak("Cancelled.")

def read_news():
    speak("Opening the latest news headlines for you.")
    webbrowser.open("https://news.google.com")


def unknown_command(query):
    speak(f"I heard: {query}. But I am not sure what to do with that yet.")
