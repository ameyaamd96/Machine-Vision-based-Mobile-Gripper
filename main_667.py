import Adafruit_BBIO.GPIO as GPIO
import Adafruit_BBIO.PWM as PWM
import time
import random as rand
from IR_667 import IRread, distanceCalc

Threshold = 10
Kp=2
Kp_reverse=10  #can be tuned more
left_forward="P8_13"
left_backward="P8_19"
right_forward="P9_21"
right_backward="P9_22"
PWM.start(left_forward,5,50) #left_forward
PWM.start(left_backward,5,50)
PWM.start(right_forward,5,50) #right_forward
PWM.start(right_backward,5,50)  # might reduce to 2

time.sleep(1)
while True:
    time.sleep(0.25) #VITAL!!

        # Reads each of the IR sensors:
    front = IRread()

        # Calculates their values in cm:
    cmFront = distanceCalc(front)
    z_error = cmFront - Threshold
    print(z_error)
    if cmFront > Threshold:
        z_error = min(25,z_error)
        pwm = Kp * (z_error) 
        PWM.set_duty_cycle(left_forward,pwm)  
        PWM.set_duty_cycle(right_forward,pwm)
        PWM.set_duty_cycle(left_backward,0)
        PWM.set_duty_cycle(right_backward,0)
        time.sleep(1)
    else:
        z_error = max(-5,z_error)
        pwm = Kp_reverse * (z_error*(-1)) 
        PWM.set_duty_cycle(left_forward,0)
        PWM.set_duty_cycle(left_backward,pwm)
        PWM.set_duty_cycle(right_forward,0)
        PWM.set_duty_cycle(right_backward,pwm)
        time.sleep(1)
