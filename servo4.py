import RPi.GPIO as GPIO  
from time import sleep



GPIO.setmode(GPIO.BOARD) 

GPIO.setup(12, GPIO.OUT) 
GPIO.setup(11, GPIO.OUT) 

p = GPIO.PWM(12, 50)   
p2 = GPIO.PWM(11, 50)  

p.start(0)    
p2.start(0)        

p.ChangeDutyCycle(3.5) 
p2.ChangeDutyCycle(12) 
sleep(1)

p.ChangeDutyCycle(4) 
p2.ChangeDutyCycle(11) 
sleep(1)

p.ChangeDutyCycle(5) 
p2.ChangeDutyCycle(10) 
sleep(1)

p.ChangeDutyCycle(6) 
p2.ChangeDutyCycle(9) 
sleep(1)

p.ChangeDutyCycle(7) 
p2.ChangeDutyCycle(8) 
sleep(1)

p.ChangeDutyCycle(6) 
p2.ChangeDutyCycle(9) 
sleep(1)

p.ChangeDutyCycle(5) 
p2.ChangeDutyCycle(10) 
sleep(1)

p.ChangeDutyCycle(4) 
p2.ChangeDutyCycle(11) 
sleep(1)

p.ChangeDutyCycle(3.5) 
p2.ChangeDutyCycle(12) 
sleep(1)

p.stop()        
p2.stop()        

GPIO.cleanup() 