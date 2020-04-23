import Adafruit_BBIO.ADC as ADC #Similar to analog read
import time as T
import math as m

def piezoread():

    piezo1list = []
    piezo2list = []
    count = 0
    samples = 20
    voltMulti = 5

    ADC.setup()

    piezo1 = ADC.read("P9_35") * 100
    piezo2 = ADC.read("P9_37") * 100 
    for i in range(samples):
        count = count + 1

        piezo1list.append(piezo1)
        piezo2list.append(piezo2)

    if (count == samples):
        avgpiezo1 = round(sum(piezo1list) / len(piezo1list),3)
        avgpiezo2 = round(sum(piezo2list) / len(piezo2list),3)
			
        piezo1list = []
        piezo2list = []

        count = 0

    return (avgpiezo1,avgpiezo2)
