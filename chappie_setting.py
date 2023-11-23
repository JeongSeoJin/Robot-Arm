import RPi.GPIO as GPIO  
from time import sleep
from random import *
import sys

d = [4, 5, 6, 7]
t = [1, 2, 3]

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD) 
GPIO.setup(12, GPIO.OUT) 
GPIO.setup(11, GPIO.OUT) 
GPIO.setup(13, GPIO.OUT)
GPIO.setup(15, GPIO.OUT)

ser = GPIO.PWM(12, 50)   
ser2 = GPIO.PWM(11, 50)   

GPIO.output(13, True)
GPIO.output(15, True)

ser.start(0)    
ser2.start(0)  
while True:

    degree = choice(d)
    time = choice(t)
    ser.ChangeDutyCycle(degree)
    if degree == 4:
    	degree2 = 11
    	print(degree2)
    elif degree == 5:
    	degree2 = 10
    	print(degree2)
    elif degree == 6:
    	degree2 = 9
    	print(degree2)
    elif degree == 7:
    	degree2 = 8
    	print(degree2)
    ser2.ChangeDutyCycle(degree2)
    sleep(time)


  
ser.stop()        
ser2.stop()            
GPIO.cleanup()
GPIO.output(13, False)
GPIO.output(15, False)
 	