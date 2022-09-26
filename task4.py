import cv2
import argparse
import numpy as np
import math

image= np.ones((96*5,192*5,3),np.uint8)*255
#image[:,:]=(255,0,0)
cv2.imshow("image",image)
for i in range(0,192*5,4*5):
    cv2.line(image,(0,i),(192*5,i),(0,0,0),1)
    for j in range(0,192*5,4*5):
        cv2.line(image,(j,0),(j,192*5),(0,0,0),1)
    cv2.imshow("image",image)

image[24*5:28*5,40*5:44*5]=(0,0,0)


image[13*4*5:14*4*5,35*4*5:36*4*5]=(0,0,0)
cv2.line(image,(42*5,26*5),(142*5,54*5),(0,0,0),2)
cv2.imshow("image",image)
cv2.waitKey()
cv2.destroyAllWindows()

watr=math.sqrt(pow(8,2)+pow(26,2))
print(watr*2)


