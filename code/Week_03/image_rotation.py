# Problem: Implement a program to rotate an image by 90, 180, and 270 degrees.
#=============================================================================

import cv2

# Read the image
img = cv2.imread("apple_128.jpg")

# # Rotate the image by 90 degrees
# rotated_img_90 = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
# cv2.imwrite("./Week_03/apple_rotated_90.jpg", rotated_img_90)

# # Rotate the image by 180 degrees
# rotated_img_180 = cv2.rotate(img, cv2.ROTATE_180)
# cv2.imwrite("./Week_03/apple_rotated_180.jpg", rotated_img_180)

# # Rotate the image by 270 degrees
# rotated_img_270 = cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE)
# cv2.imwrite("./Week_03/apple_rotated_270.jpg", rotated_img_270)


# We can also do this by modifying the image matrix directly
# Rotate the image by 90 degrees
rotated_img_90 = cv2.transpose(img)
rotated_img_90 = cv2.flip(rotated_img_90, 1) # 1 = horizontal flip, 0 = vertical flip

cv2.imshow("Rotated Image 90", rotated_img_90)
cv2.waitKey(0)
