import cv2
img = cv2.imread("apple.jpg")
print(img[255, 0, 0])