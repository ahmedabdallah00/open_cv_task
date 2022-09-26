import cv2
import numpy as np

def empty():
    pass
#trad_method
image=cv2.imread("D:\\Users\\Desktop\\project\\manual1.png") 
gray=cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#gray = cv2.imread("D:\\Users\\Desktop\\project\\manual1.png", cv2.IMREAD_GRAYSCALE)
gray1=cv2.GaussianBlur(gray,(5,5),0)
blank=np.zeros(image.shape,np.uint8)
cv2.imshow("grayscale",gray)
#   Canny
canny =cv2.Canny(gray,150,200)
cv2.imshow("Canny edge",canny)
canny1 =cv2.Canny(gray1,150,200)
cv2.imshow("Canny edge1",canny1)
#solbel
sbox=cv2.Sobel(gray,cv2.CV_64F,1,0)
sboy=cv2.Sobel(gray,cv2.CV_64F,0,1)
cv2.imshow("Sobel edge x_Axis",sbox)
cv2.imshow("Sobel edge y_Axis",sboy)
sbox1=cv2.Sobel(gray1,cv2.CV_64F,1,0)
sboy1=cv2.Sobel(gray1,cv2.CV_64F,0,1)
cv2.imshow("Sobel edge x_Axis1",sbox1)
cv2.imshow("Sobel edge y_Axis1",sboy1)
#laplacian
laplacian =cv2.Laplacian(gray,cv2.CV_64F)
cv2.imshow("Laplacian",laplacian)
laplacian1 =cv2.Laplacian(gray1,cv2.CV_64F)
cv2.imshow("Laplacian1",laplacian1)
#find_contours
ret,thresh=cv2.threshold(gray,125,255,cv2.THRESH_BINARY)
contours, hierarchy =cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
contours1, hierarchy1 =cv2.findContours(thresh,cv2.RETR_LIST,cv2.CHAIN_APPROX_NONE)
contours2, hierarchy2 =cv2.findContours(thresh,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
#contours3, hierarchy3 =cv2.findContours(canny,cv2.RETR_FLOODFILL,cv2.CHAIN_APPROX_NONE)
#contours4, hierarchy4 =cv2.findContours(canny,cv2.RETR_CCOMP,cv2.CHAIN_APPROX_NONE)

cv2.drawContours(blank,contours,-1,(0,0,255),1)
cv2.imshow('contours ', blank)

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
    cv2.waitKey(1)


cv2.destroyAllWindows()    
