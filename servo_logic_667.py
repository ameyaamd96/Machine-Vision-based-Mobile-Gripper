import Adafruit_BBIO.GPIO as GPIO
import Adafruit_BBIO.PWM as PWM
import time
import random as rand
from IR_667 import IRread, distanceCalc
from piezo_667 import piezoread

Threshold = 10
servoPin1 = "P8_13"
servoPin2 = "P8_19"
PWM.start(servoPin1,0,50)
PWM.start(servoPin2,0,50)
dutycycle1 = 10
dutycycle2 = 5
time.sleep(1)
while True:
    contact1, contact2 = piezoread()
    print(contact1, contact2)
    if (contact1 < Threshold):
        dutycycle1 = dutycycle1 - 0.1
        PWM.set_duty_cycle(servoPin1,max(dutycycle1,8))
        time.sleep(0.1)
    if (contact2 < Threshold):
        dutycycle2 = dutycycle2 + 0.1
        PWM.set_duty_cycle(servoPin2,min(dutycycle2,7.25))
        time.sleep(0.1)


#dutycycle1 = 8.25 #for gripping
#dutycycle2 = 7