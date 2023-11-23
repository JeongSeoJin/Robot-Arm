#!/usr/bin/env python3
""" test example file for rpiMotorlib.py A4988 NEMA"""

import time
import RPi.GPIO as GPIO

"""
# Next 3 lines for development, local library testing import
# Comment out in production release and change RpiMotorLib.A4988Nema to A4988Nema
import sys
sys.path.insert(0, '/home/pi/Documents/tech/RpiMotorLib/RpiMotorLib')
from RpiMotorLib import A4988Nema
"""

# Production installed library import
from RpiMotorLib import RpiMotorLib

"""
# Comment in To Test motor stop, put a push button to VCC on GPIO 17
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
"""

 
def main():
    # Microstep Resolution MS1-MS3 -> GPIO Pin , can be set to (-1,-1,-1) to turn off 
    GPIO_pins = (14, 15, 18)  
    direction= 20       # Direction -> GPIO Pin
    step = 21      # Step -> GPIO Pin
    
    # (self, direction_pin, step_pin, mode_pins , motor_type):
    mymotortest = RpiMotorLib.A4988Nema(direction, step, GPIO_pins, "A4988")
    # ========================== section B =========================
    print("TEST SECTION B")
    
    # motor_go(clockwise, steptype", steps, stepdelay, verbose, initdelay)
    input("TEST: Press <Enter> to continue Full Test6")
    time.sleep(3)
    mymotortest.motor_go(True, "Full" , 200, .005, True, .05)
    time.sleep(1)
    
    # input("TEST: Press <Enter> to continue Full Test7")
    # mymotortest.motor_go(False, "Full" , 400, .005, True, .05)
    # time.sleep(1)
    
    # input("TEST: Press <Enter> to continue Full Test8")
    # mymotortest.motor_go(False, "Half" , 200, .005, True, .05)
    # time.sleep(1)

    input("TEST: Press <Enter> to continue Full Test8")
    time.sleep(3)
    mymotortest.motor_go(True, "Half" , 400, .005, True, .05)
    time.sleep(1)
    
"""
# Comment in for testing motor stop ,  put push button to VCC on GPIO 17
def button_callback(channel):
    print("Test file: Stopping motor")
    mymotortest.motor_stop()
"""

# ===================MAIN===============================

if __name__ == '__main__':

    print("TEST START")
    main()
    GPIO.cleanup()
    print("TEST END")
    exit()

# =====================END===============================