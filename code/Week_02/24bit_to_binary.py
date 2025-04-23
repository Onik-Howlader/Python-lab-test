#Problem: Convert an image from color (RGB) / 24-bit to binary / 1-bit using OpenCV.
#===========================================================================

#Solution:
import cv2
import numpy as np

# Read the image
img = cv2.imread("apple.jpg")

# Get the dimensions of the image
height, width, channels = img.shape

# Create a new image with the same dimensions as the original image
img_bw = np.zeros((height, width), np.uint8)

# Loop through each pixel in the image
for i in range(height):
    for j in range(width):
        # Get the RGB values of the pixel
        b, g, r = img[i, j]
        
        # Convert the RGB values to binary using the formula: Y = 0.299R + 0.587G + 0.114B
        gray = 0.299 * r + 0.587 * g + 0.114 * b
        
        # Convert the grayscale value to binary
        if gray > 128:
            binary = 255
        else:
            binary = 0
            
        # Set the pixel value in the new image
        img_bw[i, j] = binary
        
        
# Store the binary image
cv2.imwrite("./Week_02/apple_bw.jpg", img_bw)

# Display the binary image
cv2.imshow("Binary Image", img_bw)
cv2.waitKey(0)
cv2.destroyAllWindows()