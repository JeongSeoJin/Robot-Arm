import time
import Adafruit_PCA9685

servo = Adafruit_PCA9685.PCA9685()
servo_min = 150
servo_max = 550

def map(value, min_angle, max_angle, min_pulse, max_pulse):
	angle_range = max_angle - min_angle
	pulse_range = max_angle - min_pulse
	scale_factor = float(angle_range)/float(pulse_range)
	return min_pulse+(value/scale_factor)

def set_angle(channel, angle):
	pulse = int(map(angle, 0, 180, servo_min, servo_max))
	servo.set_pwm(channel, 0, pulse)

servo.set_pwm_freq(60)

while True:
	value = int(input(" Degree : "))
	set_angle(0, value)
