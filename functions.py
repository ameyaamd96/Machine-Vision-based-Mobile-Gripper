import Adafruit_BBIO.PWM as PWM
import time
def yawcorrection(error):
    if error>30:
        coeff = min((error)/320*70,70)
        PWM.set_duty_cycle("P9_21",0)
        PWM.set_duty_cycle("P9_22",0)
        PWM.set_duty_cycle("P8_13",coeff)
        PWM.set_duty_cycle("P8_19",0)
    elif error<-30:
        coeff = -max((error)/320*60,-60)
        PWM.set_duty_cycle("P9_21",coeff)
        PWM.set_duty_cycle("P9_22",0)
        PWM.set_duty_cycle("P8_13",0)
        PWM.set_duty_cycle("P8_19",0)
        

def moveforward(area):
    coeff = min((30000-area)/30000*100,100)
    PWM.set_duty_cycle("P9_21",coeff)
    PWM.set_duty_cycle("P9_22",0)
    PWM.set_duty_cycle("P8_13",coeff)
    PWM.set_duty_cycle("P8_19",0)
    
def movebackward(area):
    coeff = min((19000-area)/19000*50,50)
    PWM.set_duty_cycle("P9_21",coeff)
    PWM.set_duty_cycle("P9_22",0)
    PWM.set_duty_cycle("P8_13",coeff)
    PWM.set_duty_cycle("P8_19",0)
    