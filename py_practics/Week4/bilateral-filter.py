import cv2

img = cv2.imread("./Week4/tree.jpg")
bilateral_filtered = cv2.bilateralFilter(img, 35, 95, 95)

cv2.imshow("B-filter", bilateral_filtered)
cv2.waitKey(0)
cv2.destroyAllWindows()