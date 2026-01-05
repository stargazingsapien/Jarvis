import speech_recognition as sr
from engine.speech import speak

def take_command(silent=False):
    r = sr.Recognizer()

    try:
        source = sr.Microphone(device_index=1)
        with source:
            if not silent:
                print("Listening...")
            r.pause_threshold = 1
            r.energy_threshold = 150 
            r.dynamic_energy_threshold = False
            
            try:
                audio = r.listen(source, timeout=5, phrase_time_limit=5)
            except sr.WaitTimeoutError:
                if not silent:
                    print("Listening timed out. No speech detected.")
                return "None"
            except Exception as e:
                if not silent:
                    print(f"Listening ignored error: {e}")
                return "None"
    except Exception as e:
        if not silent:
            print(f"Error accessing microphone: {e}.")
        return "None"

    try:
        if not silent:
            print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except sr.UnknownValueError:
        if not silent:
            print("Could not understand audio")
        return "None"
    except sr.RequestError as e:
        if not silent:
            print(f"Could not request results; {e}")
        return "None"
    except Exception as e:
        if not silent:
            print(f"Error: {e}") 
        return "None"
    return query.lower()

if __name__ == "__main__":
    take_command()
