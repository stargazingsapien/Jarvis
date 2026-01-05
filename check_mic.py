import speech_recognition as sr

def scan_microphones():
    print("Scanning all available input devices...")
    working_indices = []
    
    mic_names = sr.Microphone.list_microphone_names()
    
    for index, name in enumerate(mic_names):

        print(f"\n--- Checking Device {index}: {name} ---")
        
        r = sr.Recognizer()
        r.energy_threshold = 300 
        
        try:
            with sr.Microphone(device_index=index) as source:
                try:
                    print(f"  Status: Listening (2s)... speak now!")
                    audio = r.listen(source, timeout=2, phrase_time_limit=2)
                    print(f"  >>> SIGNAL DETECTED on Device {index}! <<<")
                    
                    try:
                        text = r.recognize_google(audio)
                        print(f"  >>> RECOGNIZED: '{text}'")
                        working_indices.append(index)
                    except sr.UnknownValueError:
                        print("  >>> Audio detected, but speech not recognized.")
                        working_indices.append(index)
                    except:
                        pass
                        
                except sr.WaitTimeoutError:
                    print("  Status: No audio detected (Timeout).")
                    
        except OSError:
            print("  Status: Device could not be opened (OSError).")
        except Exception as e:
            print(f"  Status: Error {e}")

    print("\n\n====== SUMMARY ======")
    if working_indices:
        print(f"Working Microphone Indices: {working_indices}")
        print("Update your code to use one of these indices.")
    else:
        print("No working microphone found on any index.")
        print("1. Check Windows Privacy Settings > Microphone.")
        print("2. Check Physical Mute Switch.")
        print("3. Check Input Volume in Sound Settings.")

if __name__ == "__main__":
    scan_microphones()
