import cv2

image = cv2.imread("picture2.png")
gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

edges1 = cv2.Canny(gray,30,100)
edges2 = cv2.Canny(gray,50,150)
edges3 = cv2.Canny(gray,100,200)

cv2.imshow("Original Image",image)
cv2.imshow("edges 30 - 100",edges1)
cv2.imshow("edges 50 - 150",edges2)
cv2.imshow("edges 100 - 200",edges3)

cv2.waitKey(0)
cv2.destroyAllWindows()
