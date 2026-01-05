import datetime
from engine.speech import speak
from engine.listen import take_command
from engine.commands import (
    tell_time, tell_date, unknown_command,
    play_youtube, search_google, search_wikipedia, open_app,
    play_spotify, volume_control, take_screenshot, switch_window,
    send_whatsapp, read_news
)
from engine.ai import ask_ai, analyze_screen
from engine.email_client import check_emails

def run_jarvis():
    while True: 
        print("\nWaiting for wake word...")
        while True:
            wake_command = take_command(silent=True).lower()
            if "hello jarvis" in wake_command or "wake up" in wake_command:
                speak("Hello Nisarg. I am online and ready for your commands.")
                break
        
        while True:
            query = take_command() 
            
            if "exit" in query or "quit" in query:
                speak("Goodbye, Nisarg. Shutting down completely.")
                return 
                
            elif "sleep" in query or "standby" in query:
                speak("Going into standby mode. Clap twice to wake me up.")
                break 
                
            elif "time" in query:
                tell_time()
                
            elif "date" in query:
                tell_date()
                
            elif "spotify" in query:
                play_spotify(query)
                speak("Enjoy the music. I'm going into standby mode.")
                break 

            elif "whatsapp" in query or "message" in query:
                send_whatsapp(query)
                break 
                
            elif "news" in query or "headlines" in query:
                read_news()
                break 

            elif "play" in query or "youtube" in query:
                play_youtube(query)
                break 

            elif "search" in query or "google" in query:
                search_google(query)
                break 
            
            elif "open" in query:
                open_app(query)
                break 
                
            elif "wikipedia" in query:
                search_wikipedia(query)
                break 
                
            elif "volume" in query or "mute" in query:
                volume_control(query)
                
            elif "screenshot" in query:
                take_screenshot()
                break 
                
            elif "switch" in query and "window" in query:
                switch_window()
                break 

            elif "thanks" in query or "thank you" in query:
                speak("You're very welcome Nisarg, ask me whenever you need me.")
                break 
                
            elif "look at this" in query or "read screen" in query or "read my screen" in query or "on my screen" in query:
                analyze_screen(query)
                # We stay in active mode for follow-up questions or just break to standby?
                # Usually vision queries are "one-off". Let's wait for next command.
                
            elif "email" in query or "mail" in query or "inbox" in query:
                check_emails()
                
            elif query != "None":
                ask_ai(query)

if __name__ == "__main__":
    run_jarvis()
