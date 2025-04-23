# Problem: Convert an image from color (RGB) to grayscale using OpenCV.
#Solution:
import cv2
import numpy as np

img = cv2.imread("apple.jpg") 

height, width, channels = img.shape

img_gray = np.zeros((height, width), np.uint8) 

for i in range(height):
    for j in range(width):
        b, g, r = img[i, j]
        
        gray = 0.299 * r + 0.587 * g + 0.114 * b
        
        img_gray[i, j] = gray
        
cv2.imwrite("./Week_02/apple_gray.jpg", img_gray)

cv2.imshow("Grayscale Image", img_gray)
cv2.waitKey(0)
cv2.destroyAllWindows()

# An easier way to convert an image from color to grayscale is to use the cvtColor function in OpenCV.
#=======================================================================================================
# Read the image
img = cv2.imread("apple.jpg")
# Convert the image to grayscale
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Store the grayscale image
cv2.imwrite("./Week_02/apple_gray.jpg", img_gray)

# Display the grayscale image
cv2.imshow("Grayscale Image", img_gray)
cv2.waitKey(0)
cv2.destroyAllWindows()

