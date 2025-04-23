#Python has lots of libraries that make it easy to work with images, audio, and video. In this course, we'll be using the following libraries:
#To install Pillow, run the following command in your terminal:
#  pip install Pillow
#To install OpenCV, run the following command in your terminal:
#  pip install opencv-python

#In this course, we'll also be using Pygame, Pydub, and MoviePy. To install these libraries, run the following commands in your terminal to install all of them at once:
#  pip install pygame pydub moviepy

#Problem 01: Write a simple Python script using PIL (Pillow) to open and display an image.
#=========================================================================================
#Solution:
from PIL import Image
img = Image.open("apple.jpg") # Open the image
img.show() # Display the image



#Problem 02: Write a simple Python script using OpenCV to open and display an image.
#=========================================================================================
#Solution:
# import cv2
# img = cv2.imread("apple.jpg") # Read the image
# cv2.imshow("Image", img) # Display the image
# cv2.waitKey(0) # Wait for the user to press any key
# cv2.destroyAllWindows() # Close the window





