import cv2
import numpy as np

count = 0
# Dictionary containing some colors:
#colors = {'blue': (255, 0, 0), 'green': (0, 255, 0), 'red': (0, 0, 255), 'yellow': (0, 255, 255),
#          'magenta': (255, 0, 255), 'cyan': (255, 255, 0), 'white': (255, 255, 255), 'black': (0, 0, 0),
#          'gray': (125, 125, 125), 'rand': np.random.randint(0, high=256, size=(3,)).tolist(),
#         'dark_gray': (50, 50, 50), 'light_gray': (220, 220, 220)}
colors=[(255, 0, 0),(0, 255, 0),(0, 0, 255),(0, 255, 255),(255, 0, 255),(255, 255, 0),(125, 125, 125)]
center = []
points=[]
def show_color_event(event, x, y, flag, param):
    global count
    
    if count == 0:
        image1[:,:]=(255,255,255)
        cv2.putText(image1, 'BLUE', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.9, colors[0], 2,
            cv2.LINE_4)
    elif count == 1:
        image1[:,:]=(255,255,255)
        cv2.putText(image1, 'GREEN', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.9, colors[1], 2,
            cv2.LINE_4)
    elif count == 2:
        image1[:,:]=(255,255,255)
        cv2.putText(image1, 'RED', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.9, colors[2], 2,
            cv2.LINE_4)
    elif count == 3:
        image1[:,:]=(255,255,255)
        cv2.putText(image1, 'YELLOW', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.9, colors[3], 2,
            cv2.LINE_4)
    elif count == 4:
        image1[:,:]=(255,255,255)
        cv2.putText(image1, 'magenta', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.9, colors[4], 2,
            cv2.LINE_4) 
    elif count == 5:
        image1[:,:]=(255,255,255)
        cv2.putText(image1, 'cyan', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.9, colors[5], 2,
            cv2.LINE_4)
    elif count == 6:
        image1[:,:]=(255,255,255)
        cv2.putText(image1, 'gray', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.9, colors[6], 2,
            cv2.LINE_4)  
                  


def draw_rec(event, x, y, flag, param):
    global count
    global points

    if event == cv2.EVENT_LBUTTONDOWN:
        points.append((x,y))
        center.append([(x, y), colors[count]])
        for point, color in center:
            print(point)
            if len(points) >=2 and len(points)%2 ==0:
                cv2.rectangle(image,points[-1],points[-2],color,2)
    
    if event == cv2.EVENT_RBUTTONDOWN:
        count += 1
        if count == 7:
            count = 0
image= cv2.imread('D:\\Users\\Desktop\\project\\manual1.png')
#image[:,:]=(0,0,0)
image1= np.ones((96,192,3),np.uint8)*255
#cv2.imshow("image",image)
image_name = "MAP"
cv2.namedWindow(image_name)
cv2.namedWindow('event_color')
cv2.setMouseCallback(image_name, draw_rec)
cv2.setMouseCallback('event_color', show_color_event)


while True:
  #  image_copy = image.copy()
    
    image1_copy = image1.copy()
    
    cv2.imshow(image_name, image)
    cv2.imshow('event_color', image1_copy)
    key = cv2.waitKey(1)
    if key == ord("Q") or key == ord("q"):
        break
    if key == ord("D") or key == ord("d"):
        if len(center):
            center.pop()
cv2.destroyAllWindows()