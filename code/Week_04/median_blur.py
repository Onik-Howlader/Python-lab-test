import cv2

img = cv2.imread('real_apple.png')
median_blur = cv2.medianBlur(img, 25)

cv2.imshow('Median Blur', median_blur)
cv2.waitKey(0)
cv2.destroyAllWindows()
