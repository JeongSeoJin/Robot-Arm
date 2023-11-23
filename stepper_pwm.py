import RPi.GPIO as GPIO
import time

DIR = 20
STEP = 21

GPIO.setmode(GPIO.BCM)
GPIO.setup(DIR, GPIO.OUT)
GPIO.setup(STEP, GPIO.OUT)
p = GPIO.PWM(DIR, 500)

def spin_motor(direction, num_steps):
	GPIO.output(STEP, direction)
	while num_steps > 0:
		p.start(1)
		time.sleep(0.01)
		num_steps -= 1

	p.stop()
	GPIO.cleanup()
	return True

direction_input = raw_input("Please enter 0 or C for Open or Close : ")
num_steps = input("Please enter the number of steps : ")
if direction_input == 'c':
	spin_motor(False, num_steps)

else:
	spin_motor(True, num_steps)
# spin_motor(True, num_steps)

