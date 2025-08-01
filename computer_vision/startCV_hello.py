import cv2

image = cv2.imread("picture1.jpg")

cv2.imshow("My First Image" , image)

#تبدیل به تصویر سیاه سفید
gray_image = cv2.cvtColor(image , cv2.COLOR_BGR2GRAY)

#لبه یابی تصویر
edges = cv2.Canny(gray_image , 100 , 200)

cv2.imshow("Edges Image - 100 , 200 " , edges)

edges2 = cv2.Canny(gray_image , 50 , 150)

cv2.imshow("Edges Image - 50 , 150 " , edges2)

cv2.waitKey(0)

cv2.destroyAllWindows()