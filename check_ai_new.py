from google import genai

API_KEY = "Your API_KEY"
client = genai.Client(api_key=API_KEY)

with open("models_v2.txt", "w") as f:
    try:
        for m in client.models.list():
            f.write(f"{m.name}\n")
    except Exception as e:
        f.write(f"Error: {e}")
