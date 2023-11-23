from gtts import gTTS
import sys
import time
import pygame

mytext = "Text To Speech Conversation Using Python"

language = "en"

output = gTTS(text = mytext, lang = language, slow = False)

output.save("output.mp3")

# os.system("start output.mp3")

pygame.mixer.init()

pygame.mixer.music.load("output.mp3")

pygame.mixer.music.play()

clock = pygame.time.Clock()

while pygame.mixer.music.get_busy():
    clock.tick(30)
pygame.mixer.quit()
