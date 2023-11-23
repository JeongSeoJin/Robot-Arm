import RPi.GPIO as GPIO
import time

pin = 12
pin2 = 11
GPIO.setmode(GPIO.BOARD)
GPIO.setup(pin, GPIO.OUT) 
GPIO.setup(pin2, GPIO.OUT) 

servo = GPIO.PWM(pin2, 50)
servo2 = GPIO.PWM(pin, 50)  
servo.start(0)
servo2.start(0)  

try:
	while True:
		key = raw_input("Enter T, B, M : ")
		if key.upper() =='T':
			print("Top : 7")
			servo.ChangeDutyCycle(7.5)
			servo2.ChangeDutyCycle(7.5)
			time.sleep(0.5)
			
		if key.upper() =='B':
			print("Bottom : 3")
			servo.ChangeDutyCycle(12)
			servo2.ChangeDutyCycle(3)
			time.sleep(0.5)

		if key.upper() =='M':
			print("Middle : 5")
			servo.ChangeDutyCycle(10)
			servo2.ChangeDutyCycle(5)
			time.sleep(0.5)
except KeyBoardInterrupt:
	servo.stop()
	servo2.stop()

GPIO.cleanup()
		
b