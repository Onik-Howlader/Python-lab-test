#Problem: Replace the white background of an image with a Yellow background using OpenCV.
#========================================================================================

#Solution:
import cv2
import numpy as np

# Read the image
img = cv2.imread("apple.jpg")

# Get the dimensions of the image
height, width, channels = img.shape

# set the white tolerance
white_tolerance = 230

# Copy the image
img_yellow = img.copy()

# Loop through each pixel in the image
for i in range(height):
    for j in range(width):
        # Get the RGB values of the pixel
        b, g, r = img[i, j]
        
        # Check if the pixel is white
        if r > white_tolerance and g > white_tolerance and b > white_tolerance:
            # Set the pixel value to yellow
            img_yellow[i, j] = [0, 255, 255]
        
# Store the image with the yellow background
cv2.imwrite("./Week_02/apple_yellow.jpg", img_yellow)

# Display the image with the yellow background
cv2.imshow("Yellow Background Image", img_yellow)
cv2.waitKey(0)

