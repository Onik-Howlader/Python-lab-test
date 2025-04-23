# # Problem: Write a Python script to crop a specific region from an image.

# import cv2

# # Read the image
# img = cv2.imread("cliff.jpg")

# # Crop the image
# cropped_img = img[100:300, 100:300] # [y1:y2, x1:x2]

# # Show the cropped image
# cv2.imshow("Cropped Image", cropped_img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# Problem: Convert a rectangular image into a circular cropped version.



import cv2
import numpy

# Read the image
img = cv2.imread("cliff.jpg")

# Get the dimensions of the image
height, width, channels = img.shape

# Create a mask
mask = numpy.zeros((height, width), numpy.uint8)

# Create a white circle on the mask
cv2.circle(mask, (width//2, height//2), 100, (255, 255, 255), -1) # arguments: image, center, radius, color, thickness (-1 = fill)

# Apply the mask to the image
masked_img = cv2.bitwise_and(img, img, mask=mask)

# Show the masked image
cv2.imshow("Masked Image", masked_img)
cv2.waitKey(0)
cv2.destroyAllWindows()