import cv2

img = cv2.imread("face.png", 0)
canny = cv2.Canny(img, 60, 100)

cv2.imshow("Canny-image", canny)
cv2.waitKey(0)
cv2.destroyAllWindows()