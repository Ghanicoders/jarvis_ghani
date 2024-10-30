from datetime import datetime
import pyttsx3
import os

# Access environment variables
USER = os.getenv('USER')
BOT = os.getenv('BOT')
# from decouple import config

# # Access environment variables
# USER = config('USER')
# BOT = config('BOT')

# Initialize pyttsx3 engine
engine = pyttsx3.init('sapi5')
engine.setProperty('volume', 1.5)
engine.setProperty('rate', 225)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def greetingme():
    hour = datetime.now().hour
    if hour >= 6 and hour < 12:
        speakers(f"Good Morning {USER}")

    elif hour >= 12 and hour < 16:
        speakers(f"Good Afternoon {USER}")

    elif hour >= 16 and hour < 18:
        speakers(f"Good Evening {USER}")

    else:
        speakers(f"Hey, I am {BOT}. How may I assist you, {USER}?")

def speakers(text):
    engine.say(text=text)
    engine.runAndWait()

greetingme()
