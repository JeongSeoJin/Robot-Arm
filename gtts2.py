from gtts import gtts
import os

mytext = 'Hello python'
text_lang = 'en'
myspeech = gTTs(txt = mytext, lang = text_lang, slow = False)

myspeech.save("Welcome.mp3")
os.system("welcome.mp3")