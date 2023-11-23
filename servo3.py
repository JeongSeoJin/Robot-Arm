import RPi.GPIO as GPIO
from time import sleep 

SERVO_MAX_DUTY    = 12   
SERVO_MIN_DUTY    = 3   
servo_degree = range(0, 180)

def setServoPos(degree):

  if degree > 180:
    degree = 180


  duty = SERVO_MIN_DUTY+(degree*(SERVO_MAX_DUTY-SERVO_MIN_DUTY)/180.0)

  print("Degree: {} to {}(Duty)".format(degree, duty))

  servo1.ChangeDutyCycle(duty)
  servo2.ChangeDutyCycle(duty)

if __name__ == "__main__":  

  setServoPos(0)
  sleep(1)
 
  setServoPos(90)
  sleep(1)
 
  setServoPos(180)
  sleep(1)

  setServoPos(90)
  sleep(1)

  setServoPos(0)
  sleep(1)

  servo1.stop()
  servo2.stop()

  GPIO.cleanup()