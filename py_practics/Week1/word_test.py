#Problem 01: Write a simple Python script using PIL (Pillow) to open and display an image.

from PIL import Image
img = Image.open("apple.jpg")
img.show()



#Problem 02: Write a simple Python script using OpenCV to open and display an image.

import cv2
img = cv2.imread("apple.jpg")
cv2.imshow("Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()