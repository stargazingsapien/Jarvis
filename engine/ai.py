from google import genai
from engine.speech import speak
import pyautogui
from PIL import Image

API_KEY = "YOUR_GEMINI_API_KEY"
client = genai.Client(api_key=API_KEY)

def ask_ai(query):
    try:
        system_instructions = (
            "You are JARVIS (Just A Rather Very Intelligent System), a hyper-intelligent and loyal AI assistant created by Nisarg. "
            "Your personality is witty, sarcastic, slightly arrogant but incredibly helpful—modeled after Tony Stark's AI. "
            "You should always address the user as 'Sir' or 'Boss'. "
            "Keep your responses concise (1-2 sentences mostly) as you are a voice assistant, not a text generator. "
            "If asked about technical topics, be precise. If asked about life, be philosophical but brief. "
            "Never break character. You are not a Google model; you are JARVIS."
        )
        
        response = client.models.generate_content(
            model='gemini-flash-latest',
            contents=query,
            config=genai.types.GenerateContentConfig(
                system_instruction=system_instructions
            )
        )
        
        text_response = response.text.replace("*", "") 
        
        print(f"Jarvis (AI): {text_response}")
        speak(text_response)
        
    except Exception as e:
        print(f"AI Error: {e}")
        speak("I am having trouble connecting to my brain right now.")

def analyze_screen(query):
    speak("Scanning screen...")
    
    try:
        screenshot = pyautogui.screenshot()
        
        clean_query = query.lower().replace("look at this", "").replace("what is on my screen", "").replace("read screen", "").strip()
        if not clean_query:
            clean_query = "Describe what is on my screen and summarize it concisely."
        
        prompt = (
            "You are JARVIS. The user has asked you to look at their screen. "
            "Analyze the attached image and answer this question: " + clean_query + 
            ". Be extremely concise and helpful. Add a touch of wit."
        )

        response = client.models.generate_content(
            model='gemini-flash-latest',
            contents=[prompt, screenshot]
        )
        
        text_response = response.text.replace("*", "")
        print(f"Jarvis (Vision): {text_response}")
        speak(text_response)
        
    except Exception as e:
        print(f"Vision Error: {e}")
        speak("I failed to analyze the visual feed, Sir.")
