import cv2
import numpy as np

img = cv2.imread('./apple_128.jpg')

#get the image dimensions
height, width, channel = img.shape

#Create a new image array
gray_img = np.zeros((height, width), np.uint8)

for i in range(height):
    for j in range(width):
        pixel = img[i, j] # [B, G, R]
        b = pixel[0]
        g = pixel[1]
        r = pixel[2]
        
        #avg = (r * 0.2126) + (g * 0.7152) + (b * 0.0722)
        
        avg = (r + g + b) // 3
        
        gray_img[i, j] = avg
        
cv2.imwrite("apple_128_gray_trash.jpg", gray_img)

cv2.imshow("Gray Image", gray_img)
cv2.waitKey(0)
cv2.destroyAllWindows()