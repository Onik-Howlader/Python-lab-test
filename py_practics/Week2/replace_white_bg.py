# #Problem: Replace the white background of an image with a Yellow background using OpenCV.

import cv2
import numpy as np

img = cv2.imread("apple.jpg")
height, width, channels = img.shape
white_tolerance = 230
img_yellow = img.copy()

for i in range(height):
    for j in range(width):
        b, g, r = img[i, j]
        
        if r > white_tolerance and g > white_tolerance and b > white_tolerance:
            img_yellow[i, j] = [0, 255, 0]
        
cv2.imwrite("apple_yellow.jpg", img_yellow)

cv2.imshow("Yellow Background Image", img_yellow)
cv2.waitKey(0)

