import cv2
import numpy

img2 = cv2.imread("./week3/img2.jpg")

height, width, channels = img2.shape

mask = numpy.zeros((height, width), numpy.uint8)
cv2.circle(mask, (width//2, height//2), 180, (255, 255, 255), -1)

masked_img2 = cv2.bitwise_and(img2, img2, mask=mask)

cv2.imshow("masked Image", masked_img2)
cv2.waitKey(0)
cv2.destroyAllWindows()