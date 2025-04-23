import cv2

img = cv2.imread('apple.jpg')
gaussian_blur = cv2.GaussianBlur(img, (199, 199), 0)  # The kernel size must be odd so that it has a clear center pixel to align over each image pixel during convolution.

cv2.imshow('Gaussian Blur', gaussian_blur)
cv2.waitKey(0)
cv2.destroyAllWindows()