import cv2

img3 = cv2.imread('./week2/img3.jpg')
gaussian_blur = cv2.GaussianBlur(img3,(199, 199), 0)

cv2.imshow('Gaussian Blur', gaussian_blur)
cv2.waitKey(0)
cv2.destroyAllWindows()