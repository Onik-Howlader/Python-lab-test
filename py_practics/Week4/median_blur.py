import cv2

img2 = cv2.imread('./week3/img2.jpg')
median_blur = cv2.medianBlur(img2, 5)

cv2.imshow('Median Blur', median_blur)
cv2.waitKey(0)
cv2.destroyAllWindows()