from gtts import gTTS
from playsound import playsound

text = 'Hello , how are you doing ? I am fine , hope you are as well. So this is just the beginning we will crack this!! '

text_hn = 'नमस्ते! यह Google Text-to-Speech का एक परीक्षण है।'

sound = gTTS(text=text_hn, lang='hi')

sound.save('start.mp3')

playsound('start.mp3')