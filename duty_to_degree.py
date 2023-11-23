import RPi.GPIO as GPIO  
from time import sleep

servo_min_duty = 3
servo_max_duty = 12 

GPIO.setmode(GPIO.BOARD) 

GPIO.setup(12, GPIO.OUT) 
GPIO.setup(11, GPIO.OUT) 

p = GPIO.PWM(12, 50)   
p2 = GPIO.PWM(11, 50)  

p.start(0)
p2.start(0)

def servo(degree):
	if degree > 180:
		degree == 180

	duty = (servo_min_duty - degree)*20

	p.ChangeDutyCycle(duty)
	p2.ChangeDutyCycle(duty)


if __name__ == "__main__": 

servo(180)
sleep(1)

servo(90)
sleep(1)

servo(0)
sleep(1)

p.stop()
p2.stop()


GPIO.cleanup()