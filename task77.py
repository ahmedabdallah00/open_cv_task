import cv2
import matplotlib.pyplot as plt
import numpy as np


def show_with_matplotlib(color_img, title, pos):
    """Shows an image using matplotlib capabilities"""

    # Convert BGR image to RGB
    img_RGB = color_img[:, :, ::-1]
    plt.subplot(1, 3, pos)
    plt.imshow(img_RGB)
    plt.title(title)
    plt.tight_layout(pad=3)
    plt.show()
    #plt.axis('off')


# Read the input image:
image = cv2.imread('D:\\Users\\Desktop\\level 300\\imgscv.jpg.png')
print(image)
# Show loaded image:
#show_with_matplotlib(image, 'Original image', 1)

# A copy of the image is created to show the points that will be used for the affine transformation:
image_points = image.copy()
cv2.circle(image_points, (120, 220), 10, (255, 0, 255), -1)
cv2.circle(image_points, (700, 80), 10, (255, 0, 255), -1)
cv2.circle(image_points, (840, 350), 10, (255, 0, 255), -1)
cv2.circle(image_points, (220, 580), 10, (255, 0, 255), -1)

# Show the image with the three created points:
#show_with_matplotlib(image_points, 'before perespective', 2)

pts_1 = np.float32([[120, 220], [700, 80], [220, 580], [840, 350]])
pts_2 = np.float32([[0, 0], [300, 0], [0, 300], [300, 300]])

# To correct the perspective (also known as perspective transformation) you need to create the transformation matrix
# making use of the function cv2.getPerspectiveTransform(), where a 3x3 matrix is constructed:
M = cv2.getPerspectiveTransform(pts_1, pts_2)

# Then, apply cv2.warpPerspective(), where the source image is transformed applying
# the specified matrix and with a specified size:
dst_image = cv2.warpPerspective(image, M, (300, 300))
show_with_matplotlib(dst_image, 'after perespective transform', 3)

cv2.imshow('pts',pts_1)
cv2.imshow("dst",dst_image)
cv2.imshow("src",image)