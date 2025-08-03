import cv2
import matplotlib.pyplot as plt

image = cv2.imread("picture2.png")

gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

_,tresholded = cv2.threshold(gray , 127 , 255 ,cv2.THRESH_BINARY)
#_,tresholded = cv2.threshold(gray , 80 , 255 ,cv2.THRESH_BINARY)
# _,tresholded = cv2.threshold(gray , 150 , 255 ,cv2.THRESH_BINARY)
# _,tresholded = cv2.threshold(gray , 200 , 255 ,cv2.THRESH_BINARY)


plt.figure(figsize=(10 , 5))

plt.subplot(1,2,1)
plt.imshow(gray,cmap="gray")
plt.title("Gray Image")

plt.subplot(1,2,2)
plt.imshow(tresholded,cmap="gray")
plt.title("Tresholded Image")

plt.tight_layout()
plt.show()
