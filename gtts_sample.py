# -*- coding: utf-8 -*-

from gtts import gTTs
import pygame
import sys
import time

clock = pygame.time.Clock()

def talk2(talktext):
   mytext = talktext
   text_lang = 'ko'
   myspeech = gTTS(text=mytext, lang=text_lang, slow=False)
   myspeech.save("weather.mp3")

   pygame.init()
   #display=pygame.display.set_mode((400,300))
   #pygame.display.set_caption("sound")
   pygame.mixer.music.load("weather.mp3")

   pygame.mixer.music.play()
   #print(mytext)
   while pygame.mixer.music.get_busy():
      clock.tick(1000)