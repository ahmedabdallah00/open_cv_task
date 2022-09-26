import cv2
import numpy as np

def getContours(image):
    contours,hierarchy =cv2.findContours(image,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        area=cv2.contourArea(cnt)
        if area>500:
            #cv2.drawContours(image_c,cnt,-1,(0,0,255),3)
            peri=cv2.arcLength(cnt,True)
            approx=cv2.approxPolyDP(cnt,0.02*peri,True) 
            obj=len(approx)   
            x,y,w,h=cv2.boundingRect(approx) 
            
            if obj ==3: obj_type='trangle'
            elif obj ==4: 
                asp=w/float(h)
                if asp>0.95 and asp<1.05: obj_type='Square'
                else: obj_type='rectangle'
            elif obj ==5: obj_type='five'
            elif obj ==6: obj_type='hex'
            elif obj ==10: obj_type='star'
            elif obj ==7: obj_type='7'
            elif obj ==8: obj_type='8'
            elif obj ==9: obj_type='9'
            else: obj_type='none'
           
            cv2.rectangle(image_c,(x,y),(w+x,h+y),(0,0,255),3)
            cv2.putText(image_c,obj_type,(x+(w//2)-10,y+(h//2)-10),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,255,255),2)


image=cv2.imread('D:\\Users\\Desktop\\project\\ROV soft\\session 20\\stream 2\\clean.jpg')
b=np.zeros_like(image)
print(image.shape)
b[150:700,150:600]=(255,255,255)
# Bitwise AND
bitwise_and = cv2.bitwise_and(image, b)
cv2.imshow('bitwise_and',bitwise_and)
gray_image=cv2.cvtColor(bitwise_and,cv2.COLOR_BGR2GRAY)
imgblur=cv2.GaussianBlur(gray_image,(7,7),1)
imgcanny=cv2.Canny(imgblur,155,170)


image_c=bitwise_and.copy()
getContours(imgcanny)
cv2.imshow("task12",image_c)
cv2.waitKey(0)