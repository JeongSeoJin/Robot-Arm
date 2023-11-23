import RPi.GPIO as GPIO  
from time import sleep

servoPin = 11

GPIO.setmode(GPIO.BOARD)   
GPIO.setup(servoPin, GPIO.OUT) 

servo1 = GPIO.PWM(servoPin, 50)  
servo1.start(0)  