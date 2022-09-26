import cv2
import numpy as np

image1=cv2.imread('D:\\Users\\Desktop\\project\\ROV soft\\session 20\\stream 2\\s11.png')
image2=cv2.imread('D:\\Users\\Desktop\\project\\ROV soft\\session 20\\stream 2\\s12.png')
image3=cv2.imread('D:\\Users\\Desktop\\project\\ROV soft\\session 20\\stream 2\\s13.png')
image4=cv2.imread('D:\\Users\\Desktop\\project\\ROV soft\\session 20\\stream 2\\s14.png')
image5=cv2.imread('D:\\Users\\Desktop\\project\\ROV soft\\session 20\\stream 2\\s15.png')
w,h=image1.shape[:2]
w1,h1=image4.shape[:2]
w2,h2=image5.shape[:2]
image8=np.zeros((w2,h2,3),np.uint8)
image7=np.zeros((w,h,3),np.uint8)
image6=np.zeros((w1,h1,3),np.uint8)
image12=np.vstack((image7,image1))
image2_resize=cv2.resize(image2,(285,87))
image34=np.vstack((image3,image2_resize))
image56=np.vstack((image6,image4))
image78=np.vstack((image8,image5))
'''
cv2.imshow('1',image12)
cv2.imshow("2",image34)
cv2.imshow("3",image56)
cv2.imshow("4",image78)
'''
image34_resize=cv2.resize(image34,(285,180))
image1234=np.hstack((image12,image34_resize))
#cv2.imshow("5",image1234)
image56_resize=cv2.resize(image56,(w1*2,182))
image5678=np.hstack((image56_resize,image78))
#cv2.imshow("5",image1234)
image1234_resize=cv2.resize(image1234,(w+285,182))
image_task=np.hstack((image1234_resize,image5678))
cv2.imshow('final',image_task)
cv2.waitKey(0)
print(image5.shape)