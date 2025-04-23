import cv2

img = cv2.imread("Macaw.jpg")
bilateral_filtered = cv2.bilateralFilter(img, 15, 75, 75)

cv2.imshow("B-filter", bilateral_filtered)
cv2.waitKey(0)
cv2.destroyAllWindows()