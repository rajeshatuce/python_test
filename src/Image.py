import cv2

img = cv2.imread("C:\\Users\\User\\Desktop\\republic_day_2019\\2.JPG", 1)
print(img)
print(type(img))
print(img.shape)
resize = cv2.resize(img, (int(img.shape[1] / 8), int(img.shape[0] / 8)))
cv2.imshow("Gaurav", resize)
cv2.waitKey(0)
cv2.destroyAllWindows()
