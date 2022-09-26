import numpy as np
import argparse
import imutils
import cv2


image1=cv2.imread('D:\\Users\\Desktop\\project\\manual1.png')
gray=cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
blank=np.zeros(image1.shape,np.uint8)
ret,thresh=cv2.threshold(gray,125,255,cv2.THRESH_BINARY)
#contours, hierarchy =cv2.findContours(image1,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
#cnts = cv2.findContours(image1.astype(np.uint8), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
#cnts = cnts[0] if imutils.is_cv2() else cnts[1]  
#cntsSorted = sorted(cnts, key=lambda x: cv2.contourArea(x))
cnts, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
cnt = sorted(cnts, key=cv2.contourArea)
print(cnt)
cv2.drawContours(blank,cnts,-1,(0,0,255),1)
cv2.imshow('controus',blank)
cv2.waitKey(0)