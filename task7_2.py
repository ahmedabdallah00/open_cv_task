import cv2
import numpy as np
coordinates = []
def points(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        cv2.circle(image, (x, y), 5, (255, 0, 0), 2)
        coordinates.append([x, y])
image = cv2.imread("D:\\Users\\Desktop\\level 300\\imgscv.jpg.png")

cv2.namedWindow("smith")
cv2.setMouseCallback("smith", points)
while True:
    cv2.imshow("smith", image)
    key = cv2.waitKey(1)
    if key == ord("Q") or key == ord("q"):
        break
    if key == 13:
        pts_1 = np.float32(coordinates)
        pts_2 = np.float32([[0, 0], [300, 0], [0, 300], [300, 300]])

        # To correct the perspective (also known as perspective transformation) you need to create the transformation matrix
        # making use of the function cv2.getPerspectiveTransform(), where a 3x3 matrix is constructed:
        M = cv2.getPerspectiveTransform(pts_1, pts_2)

        # Then, apply cv2.warpPerspective(), where the source image is transformed applying
        # the specified matrix and with a specified size:
        dst_image = cv2.warpPerspective(image, M, (300, 300))
        cv2.imshow("dst", dst_image)
cv2.destroyAllWindows()