import numpy as np
import cv2
import time
import random as rand
from IR_667 import IRread, distanceCalc
video = cv2.VideoCapture(0)
i=1
Threshold = 10

from functions import *
mode = 1;
PWM.start("P9_21",0,50)
PWM.start("P9_22",0,50)
PWM.start("P8_13",0,50)
PWM.start("P8_19",0,50)
time.sleep(1)
i=1
error_prev = 0;
while True:
  ret, frame = video.read()
  blurred_frame = cv2.GaussianBlur(frame, (5, 5), 0)
  hsv = cv2.cvtColor(blurred_frame, cv2.COLOR_BGR2HSV)
  ORANGE_MIN = np.array([5,150,155],np.uint8)
  ORANGE_MAX = np.array([30,255,240],np.uint8)
  mask = cv2.inRange(hsv, ORANGE_MIN, ORANGE_MAX)
  _, contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
  areas = [cv2.contourArea(c) for c in contours]
  if (len(areas)!=0):
    max_index = np.argmax(areas)
    contour=contours[max_index]
    area = np.max(areas)
  else:
    area = 0
  print(area)
  if (len(contours)!=0 and area>50):
        rect = cv2.minAreaRect(contour)
        box = cv2.boxPoints(rect)
        box_d = np.int0(box)
        cv2.drawContours(frame, [box_d], -1, (0, 255, 0), 3)
        average_x = (box[0][0]+box[1][0]+box[2][0]+box[3][0])/4
        error_x = 320-average_x + 0.3*error_prev
        
        if (area>30000):
          if abs(error_x)>30 and area<30000:
            if (i%30==0):
              yawcorrection((320-average_x)/2)
            else:
              yawcorrection(np.sign(error_x)*100)
            break
        else:
          if abs(error_x)>30 and area<30000:
            if (i%10==0):
              yawcorrection(error_x)
            else:
              yawcorrection(np.sign(error_x)*100)
          elif (abs(error_x)<=30 and area<30000):
            if (i%10==0):
              moveforward(area)
            else:
              moveforward(20000)
          else:
              k=1#movebackward(area)
        error_prev = error_prev + error_x*0.05;
        print("\t",error_x)
  else:
    if (i%10==0):
        yawcorrection(320)
    else:
        yawcorrection(100)    
  front = IRread()

        # Calculates their values in cm:
  cmFront = distanceCalc(front)
  z_error = cmFront - Threshold
  print("\t",cmFront)
  if (cmFront <= Threshold and area>30000):
    break
  i = i+1;      
        
        
        
        
  if cv2.waitKey(1) and 0xFF == ord('q'):
    break
    # i=2;
PWM.start("P9_21",0,50)
PWM.start("P9_22",0,50)
PWM.start("P8_13",0,50)
PWM.start("P8_19",0,50)
video.release()
cv2.destroyAllWindows()
