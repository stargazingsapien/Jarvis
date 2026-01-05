import speech_recognition as sr

def test_force_sensitivity():
    print("Testing Microphone with FIXED sensitivity (no auto-adjustment)...")
    
    device_index = 1
    
    print(f"\n--- Forcing Device {device_index} ---")
    
    r = sr.Recognizer()
    
    r.energy_threshold = 150 
    r.dynamic_energy_threshold = False 
    
    try:
        with sr.Microphone(device_index=device_index) as source:
            print(f"Energy Threshold set to: {r.energy_threshold}")
            print(f"Please speak CLOSELY into the microphone now...")
            
            try:
                audio = r.listen(source, timeout=5, phrase_time_limit=5)
                print("Signal detected! Processing...")
                text = r.recognize_google(audio)
                print(f"SUCCESS! You said: {text}")
                
            except sr.WaitTimeoutError:
                print("Timed out again. It seems NO audio is reaching Python at all.")
                print("Possibilities:")
                print("1. Privacy Settings (Microphone access disabled for apps)")
                print("2. Hardware Mute Button")
                print("3. Wrong Device Index (maybe your mic is actually device 6?)")
                
            except sr.UnknownValueError:
                print("Detected sound, but couldn't understand words.")
                
    except Exception as e:
        print(f"Error opening device: {e}")

if __name__ == "__main__":
    test_force_sensitivity()
