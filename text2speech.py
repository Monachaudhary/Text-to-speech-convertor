import pyttsx3

data = input("enter text:")
engine = pyttsx3.init()
engine.say(data)
engine.runAndWait()