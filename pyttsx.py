import pyttsx3

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

engine.setProperty('rate', 150)
engine.say("Hi my name is Jeong Seo Jin")
engine.runAndWait()

def speech(str):
    engine.say(str)
    engine.runAndWait()

speech("Hello, what's going on")
