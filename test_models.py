from google import genai
import time

API_KEY = "Your API_KEY"
client = genai.Client(api_key=API_KEY)

def test_model(model_name):
    print(f"Testing {model_name}...")
    try:
        response = client.models.generate_content(
            model=model_name,
            contents="Hello",
        )
        print(f"SUCCESS: {response.text}")
        return True
    except Exception as e:
        print(f"FAILED: {e}")
        return False

if not test_model('gemini-flash-latest'):
    if not test_model('gemini-1.5-flash-001'):
         test_model('gemini-2.0-flash-exp')
