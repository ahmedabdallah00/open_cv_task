import cv2
import numpy as np

def mouse_click(event, x, y,flags,param):

    if event == cv2.EVENT_RBUTTONUP:
        points.append((x,y))
        if len(points) >=2 and len(points)%2 ==0:
            cv2.rectangle(image,points[-1],points[-2],(0,255,0),2)

    if event == cv2.EVENT_LBUTTONUP:
        points1.append((x,y))
        if len(points1) >=2 and len(points1)%2 ==0:
            cv2.rectangle(image,points1[-1],points1[-2],(255,0,0),2)   
    if event == ord("D") or event == ord("d"):
        points.pop() 
    if event == ord("Q") or event == ord("q"):
        points1.pop()      
    cv2.imshow('image',image) 
        
  

while True:
    points=[]
    points1=[]
    image=cv2.imread("D:\\Users\\Desktop\\project\\new.png") 
    cv2.imshow("image",image)
    cv2.setMouseCallback('image',mouse_click)
   # if key == ord("D") or key == ord("d"):
    #    points.pop() 
    cv2.waitKey(0)
cv2.destroyAllWindows()