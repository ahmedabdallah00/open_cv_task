import cv2
import numpy as np

# Dictionary containing some colors:
colors = {'blue': (255, 0, 0), 'green': (0, 255, 0), 'red': (0, 0, 255), 'yellow': (0, 255, 255),
          'magenta': (255, 0, 255), 'cyan': (255, 255, 0), 'white': (255, 255, 255), 'black': (0, 0, 0),
          'gray': (125, 125, 125), 'rand': np.random.randint(0, high=256, size=(3,)).tolist(),
          'dark_gray': (50, 50, 50), 'light_gray': (220, 220, 220)}

def mousefunc(key, x,y,flags,param):
    
    
    global circles
    #if key ==4:
    #   cv2.circle(black,(x,y),50,(0,255,255),5)
    if key == cv2.EVENT_LBUTTONDBLCLK:
        # Add the circle with coordinates x,y
        print("event: EVENT_LBUTTONDBLCLK")
        circles.append((x, y))
    if key == cv2.EVENT_RBUTTONDBLCLK:
        # Delete all circles (clean the screen)
        print("event: EVENT_RBUTTONDBLCLK")
        circles[:] = []
    elif key == cv2.EVENT_RBUTTONDOWN:
        # Delete last added circle
        print("event: EVENT_RBUTTONDOWN")
        try:
            circles.pop()
        except (IndexError):
            print("no circles to delete")
    if key == cv2.EVENT_MOUSEMOVE:
        print("event: EVENT_MOUSEMOVE")
    if key == cv2.EVENT_LBUTTONUP:
        print("event: EVENT_LBUTTONUP")
    if key == cv2.EVENT_LBUTTONDOWN:
        print("event: EVENT_LBUTTONDOWN")
    '''
    else:
        cv2.circle(black,(x,y),50,(0,0,0),5)
   '''

circles = []

cv2.namedWindow("black")
cv2.setMouseCallback("black",mousefunc)
black = np.zeros((600,600,3),np.uint8) 
clone = black.copy()


while True:
    black = clone.copy()
    
    for pos in circles:
        # We print the circle (filled) with a  fixed radius (30):
        cv2.circle(black, pos, 30, colors['blue'], -1)

    cv2.imshow("black",black)
    key=cv2.waitKey(1)
    if key ==13:
        break


cv2.destroyAllWindows()    