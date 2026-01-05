import google.generativeai as genai

API_KEY = "AIzaSyCBFvxukPgvtCnSODN-K3KOqfd4qVQ82QE"
genai.configure(api_key=API_KEY)

with open("models.txt", "w") as f:
    try:
        for m in genai.list_models():
            if 'generateContent' in m.supported_generation_methods:
                f.write(m.name + "\n")
    except Exception as e:
        f.write(f"Error: {e}")
