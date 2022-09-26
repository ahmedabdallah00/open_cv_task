import numpy as np
import cv2  
width=int(input("please entre width: "))
length=int(input("please entre length: "))
cap = cv2.VideoCapture(0)   
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (width, length))
  
while(True):
   
    print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    ret, frame = cap.read() 
    print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    out.write(hsv) 
    cv2.imshow('Original', frame)
    cv2.imshow('frame', hsv)
    key = cv2.waitKey(1)
    if key == ord('a'):
        break
    
cap.release() 
out.release()  
cv2.destroyAllWindows()