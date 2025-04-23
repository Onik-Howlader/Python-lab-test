import cv2
import numpy as np

img = cv2.imread('./apple_128.jpg')

#get the image dimensions
height, width, channel = img.shape

#Create a new image array
new_img = img.copy()

for i in range(height):
    for j in range(width):
        pixel = img[i, j] # [B, G, R]
        b = pixel[0]
        g = pixel[1]
        r = pixel[2]
        
        if(r > 230 and g > 230 and b > 230):
            new_img[i, j] = [0, 255, 255]
        
cv2.imwrite("apple_128_yellow_bg.jpg", new_img)

cv2.imshow("Gray Image", new_img)
cv2.waitKey(0)
cv2.destroyAllWindows()