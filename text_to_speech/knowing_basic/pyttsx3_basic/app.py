import pyttsx3

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Set properties (optional)
engine.setProperty('rate', 150)  # Speed of speech

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id) 

engine.say("Hello , how are you doing ? I am fine , hope you are as well. So this is just the beginning we will crack this!! ")

engine.runAndWait()