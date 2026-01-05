import pyttsx3

engine = pyttsx3.init()
voices = engine.getProperty('voices')

print("Available Voices:")
for index, voice in enumerate(voices):
    print(f"ID: {index}")
    print(f"Name: {voice.name}")
    print(f"Languages: {voice.languages}")
    print("-" * 20)
