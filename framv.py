from email.mime import image
import cv2
import numpy as np

camera=cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))
while True:
    isTrue , frame=camera.read()
   # key = cv2.waitKey(1)
    cv2.imshow('video',frame)
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    out.write(hsv) 
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    out.write(gray)
    cv2.imshow('video1',hsv)
    cv2.imshow('video2',gray)
    key=cv2.waitKey(1)
  
    if key==ord('k'):
        w,h=frame.shape[:2]
        M= cv2.getRotationMatrix2D((w/2,h/2),45,1)
        dst=cv2.warpAffine(frame,M,(w,h))
        cv2.imshow('video',dst)
        cv2.waitKey()
    elif key== ord('H'):
       # hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        #out.write(hsv) 
        #cv2.imshow('Original', frame)
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        out.write(hsv)
        cv2.imshow('frame', hsv)
        cv2.waitKey(1)
    elif key == ord('X'):        
        cv2.imshow("orginal",frame)
        cv2.imshow("frame",hsv)
       # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
       # out.write(gray)
        cv2.imshow("grayscale",gray)
        cv2.waitKey(0)
    elif key == ord('z'):
        cv2.imshow("orginal",frame)
    elif key == ord('c'):
        cv2.imwrite("D:\\Users\\Desktop\\level 300\\task.jpg",frame)
    elif key == ord("G"):
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        out.write(gray)
        cv2.waitKey(1)
    elif key == ord("Q"):
        camera.release()
        out.release()
        cv2.destroyAllWindows()
        break
    elif key == ord("R"):
        out.write(frame)