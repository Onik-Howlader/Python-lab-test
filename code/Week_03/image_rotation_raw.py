import cv2
import numpy as np
import math

# Load the image
image = cv2.imread('apple.jpg')

# Image height and width
h, w = image.shape[:2]

# Rotation center (x0, y0) - let's rotate around the center of the image
x0, y0 = w // 2, h // 2

# Rotation angle in degrees
theta = 180  # rotate by 45 degrees

# Convert angle to radians
theta_rad = math.radians(theta)

# Calculate cos and sin
cos_theta = math.cos(theta_rad)
sin_theta = math.sin(theta_rad)

# Build rotation matrix manually
# [ cosθ  sinθ  tx ]
# [-sinθ  cosθ  ty ]

tx = x0 - x0 * cos_theta - y0 * sin_theta
ty = y0 - x0 * (-sin_theta) - y0 * cos_theta

M = np.array([
    [cos_theta, sin_theta, tx],
    [-sin_theta, cos_theta, ty]
])

# Apply warpAffine (rotates the entire image)
rotated = cv2.warpAffine(image, M, (w, h))

# Show the result
cv2.imshow('Rotated Image', rotated)
cv2.waitKey(0)
cv2.destroyAllWindows()
