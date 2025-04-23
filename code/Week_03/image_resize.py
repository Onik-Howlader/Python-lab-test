# Problem: Write a Python script to resize an image while maintaining its aspect ratio.
#=========================================================================================

import cv2

# Read the image
img = cv2.imread("apple.jpg")

# Get the dimensions of the image
height, width, channels = img.shape

# Calculate the aspect ratio of the image
aspect_ratio = width / height

# Set the new width and height
new_width = 50
new_height = int(new_width / aspect_ratio)

# Resize the image
resized_img = cv2.resize(img, (new_width, new_height))

# Stop the resized image
cv2.imwrite("./Week_03/apple_resized.jpg", resized_img)

# Display the resized image
cv2.imshow("Resized Image", resized_img)
cv2.waitKey(0)
cv2.destroyAllWindows()