import cv2
img = cv2.imread('./week3/img2.jpg')
height, width, channels = img.shape
aspect_ratio = width / height

new_width = 150
new_height = int(new_width / aspect_ratio)


resize_img2 = cv2.resize(img, (new_width, new_height))
cv2.imwrite("./week3/img2.jpg", resize_img2)
cv2.imshow("Resize Image", resize_img2)
cv2.waitKey(0)
cv2.destroyAllWindows()