import RPi.GPIO as GPIO  
from time import sleep
from random import * 

GPIO.setmode(GPIO.BOARD) 

GPIO.setup(11, GPIO.OUT) 
ser1 = GPIO.PWM(11, 50)   
GPIO.setup(12, GPIO.OUT) 
ser2 = GPIO.PWM(12, 50)
 
d = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
t = [1, 2, 3, 4]

while True:
	ser1.ChangeDutyCycle(7.5)
	sleep(1)
	ser1.ChangeDutyCycle(3)

	sleep(2)

	ser2.ChangeDutyCycle(7.5)
	ser1.ChangeDutyCycle(4)
	sleep(1)
	ser1.ChangeDutyCycle(0)
	ser2.ChangeDutyCycle(0)
	
    # degree = choice(d)
    # time = choice(t)
    # p.ChangeDutyCycle(degree)
    # sleep(time)
    # degree = choice(d)
    # time = choice(t)
    # p.ChangeDutyCycle(degree)
    # sleep(time)
    # degree = choice(d)
    # time = choice(t)
    # p.ChangeDutyCycle(degree)
    # sleep(time)
    # degree = choice(d)
    # time = choice(t)
    # p.ChangeDutyCycle(degree)
    # sleep(time)
  
p.stop()                

GPIO.cleanup() 