import Adafruit_BBIO.ADC as ADC #Similar to analog read
import time as T
import math as m

def IRread():
	# Useful Lists:
	IR1list = []

	# General purpose variables:
	count = 0
	samples = 20
	voltMulti = 5

	ADC.setup()

	# Reading analog inputs:
	IR1 = ADC.read("P9_33") * voltMulti #added a voltage multiplier

	for i in range(samples):
		count = count + 1

		IR1list.append(IR1)

		if (count == samples):
			# Calculating the average of 20 readings:
			avgIR1 = round(sum(IR1list) / len(IR1list),3)
			
			# Clearing each list:
			IR1list = []

			count = 0

	return (avgIR1)

def distanceCalc(volt):
	# NOTE: This function works only if you position the sensor 10cm from the edge.
	return (41.543 * m.pow((volt + 0.30221), -1.5281))