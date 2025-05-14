import cv2
import numpy as np
import math

image = cv2.imread('./week3/img2.jpg')
h, w = image.shape[:2]
x0, y0 = w // 2, h // 2
theta = 180
theta_rad = math.radians(theta)
cos_theta = math.cos(theta_rad)
sin_theta = math.sin(theta_rad)

tx = x0 - x0 * cos_theta - y0 * sin_theta
ty = y0 - x0 * (-sin_theta) - y0 * cos_theta

M = np.array([[cos_theta, sin_theta, tx],[-sin_theta, cos_theta, ty]])

rotated = cv2.warpAffine(image, M, (w, h))

cv2.imshow('Rotated Image', rotated)
cv2.waitKey(0)
cv2.destroyAllWindows()