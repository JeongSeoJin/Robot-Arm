import RPi.GPIO as GPIO  
from time import sleep

servoPin = 12

GPIO.setmode(GPIO.BOARD)   
GPIO.setup(servoPin, GPIO.OUT) 

servo = GPIO.PWM(servoPin, 50)  
servo.start(0)  