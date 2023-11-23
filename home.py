 	
# Simple demo of of the PCA9685 PWM servo/LED controller library.
# This will move channel 0 from min to max position repeatedly.
# Author: Tony DiCola
# License: Public Domain
from __future__ import division
import time

# Import the PCA9685 module.
import Adafruit_PCA9685


# Uncomment to enable debug output.
#import logging

#logging.basicConfig(level=logging.DEBUG)

# Initialise the PCA9685 using the default address (0x40).
pwm = Adafruit_PCA9685.PCA9685()

# Alternatively specify a different address and/or bus:
#pwm = Adafruit_PCA9685.PCA9685(address=0x41, busnum=2)

# Configure min and max servo pulse lengths
servo_min = 150  # Min pulse length out of 4096
servo_mid = 350
servo_max = 530  # Max pulse length out of 4096


# Helper function to make setting a servo pulse width simpler.
def set_servo_pulse(channel, pulse):
    pulse_length = 1000000    # 1,000,000 us per second
    pulse_length //= 60       # 60 Hz
    print('{0}us per period'.format(pulse_length))
    pulse_length //= 4096     # 12 bits of resolution
    print('{0}us per bit'.format(pulse_length))
    pulse *= 1000
    pulse //= pulse_length
    pwm.set_pwm(channel, 0, pulse)

# Set frequency to 60hz, good for servos.
pwm.set_pwm_freq(50)

while True:
    # Move servo on channel O between extremes.
    question = input("[ 1 : Home | 2 : Go forward ] : ")
    if int(question) == 1:
        print("To Home")
        pwm.set_pwm(0, 0, 175)
        pwm.set_pwm(1, 0, 180)
        pwm.set_pwm(2, 0, 350)
    elif int(question) == 2:
        print("Go forward")
        pwm.set_pwm(0, 0, 450)
        pwm.set_pwm(1, 0, 230)
        time.sleep(0.5)
        pwm.set_pwm(2, 0, 130)

    # print("servo 0")
    # pwm.set_pwm(0, 0, servo_min)
    # time.sleep(1.5)
    # pwm.set_pwm(0, 0, servo_max)
    # time.sleep(1.5)

    # print("servo 0")
    # pwm.set_pwm(1, 0, servo_min)
    # time.sleep(1.5)
    # pwm.set_pwm(1, 0, servo_max)
    # time.sleep(1.5)

    # pwm.set_pwm(2, 0, servo_min)
    # time.sleep(1.5)
    # pwm.set_pwm(2, 0, servo_max)
    # time.sleep(1.5)

    # pwm.set_pwm(3, 0, servo_min)
    # time.sleep(1.5)
    # pwm.set_pwm(3, 0, servo_max)
    # time.sleep(1.5)

    # pwm.set_pwm(4, 0, servo_min)
    # time.sleep(1.5)
    # pwm.set_pwm(4, 0, servo_max)
    # time.sleep(1.5)

    # pwm.set_pwm(5, 0, servo_min)
    # time.sleep(1.5)
    # pwm.set_pwm(5, 0, servo_max)
    # time.sleep(1.5)

