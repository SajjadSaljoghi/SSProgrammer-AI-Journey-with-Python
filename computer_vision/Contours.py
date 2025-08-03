import cv2
import matplotlib.pyplot as plt


image = cv2.imread("picture2.png")
gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

_, threshold = cv2.threshold(gray,127,255,cv2.THRESH_BINARY)

contours , hierarchy = cv2.findContours(threshold,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

img_contours = image.copy()
cv2.drawContours(img_contours,contours,-1 , (0,255,0) , 2)

plt.figure(figsize=(10,5))

plt.subplot(1,2,1)
plt.title("Original")
plt.imshow(cv2.cvtColor(image,cv2.COLOR_BGR2RGB))

plt.subplot(1,2,2)
plt.title("Contours")
plt.imshow(cv2.cvtColor(img_contours,cv2.COLOR_BGR2RGB))

print("Number of contours found:", len(contours))

plt.show()

