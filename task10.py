import cv2
import numpy as np


def empty():
    pass
#trad_method
image=cv2.imread("D:\\Users\\Desktop\\project\\manual1.png") 





cv2.namedWindow("track bar")
cv2.resizeWindow("track bar",640,240)
cv2.createTrackbar("H min","track bar",0,179,empty)
cv2.createTrackbar("H max","track bar",179,179,empty)
cv2.createTrackbar("s min","track bar",0,255,empty)
cv2.createTrackbar("s max","track bar",255,255,empty)
cv2.createTrackbar("v min","track bar",0,179,empty)
cv2.createTrackbar("v max","track bar",255,179,empty)
HSV=cv2.cvtColor(image,cv2.COLOR_BGR2HSV)
while True:
    h_min=cv2.getTrackbarPos("H min","track bar")
    h_max=cv2.getTrackbarPos("H max","track bar")
    s_min=cv2.getTrackbarPos("s min","track bar")
    s_max=cv2.getTrackbarPos("s max","track bar")
    v_min=cv2.getTrackbarPos("v min","track bar")
    v_max=cv2.getTrackbarPos("v max","track bar")
    lower=np.array([h_min,s_min,v_min])
    upper=np.array([h_max,s_max,v_max])
    mask=cv2.inRange(HSV,lower,upper)
    cv2.imshow('color detection',mask)
    key =cv2.waitKey(1)
    if key==13:
        break
    
cv2.destroyAllWindows()    