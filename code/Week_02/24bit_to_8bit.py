# Problem: Convert an image from color (RGB) to grayscale using OpenCV.
#=========================================================================
# In this problem, we'll convert an image from color (RGB) / 24-bit to grayscale / 8-bit using OpenCV.
#Solution:
import cv2
import numpy as np

# Read the image
img = cv2.imread("apple.jpg") 

# Get the dimensions of the image
height, width, channels = img.shape

# Create a new image with the same dimensions as the original image
img_gray = np.zeros((height, width), np.uint8) 

# Loop through each pixel in the image
for i in range(height):
    for j in range(width):
        # Get the RGB values of the pixel
        b, g, r = img[i, j]
        
        # Convert the RGB values to grayscale using the formula: Y = 0.299R + 0.587G + 0.114B
        gray = 0.299 * r + 0.587 * g + 0.114 * b
        
        # Set the pixel value in the new image
        img_gray[i, j] = gray
        
# Store the grayscale image
cv2.imwrite("./Week_02/apple_gray.jpg", img_gray)

# Display the grayscale image
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

