import numpy as np
import matplotlib.pyplot as plt
import cv2


image = np.zeros((400,400),dtype=np.uint8)

cv2.circle(image ,(100,100),30,255,-1)
cv2.circle(image ,(300,100),40,255,-1)
cv2.circle(image ,(200,300),50,255,-1)
# cv2.circle(image ,(200,200),25,255,-1)
# cv2.circle(image ,(100,200),35,255,-1)
cv2.ellipse(image, (200, 200), (25, 25), 0, 0, 180, 255, -1)
cv2.ellipse(image, (100, 200), (25, 25), 0, 0, 90, 255, -1)

contours,_ = cv2.findContours(image,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

image_color = cv2.cvtColor(image,cv2.COLOR_GRAY2BGR)
cv2.drawContours(image_color,contours,-1,(0,255,0),2)

print("Number of circles found:", len(contours))

plt.subplot(1, 2, 1)
plt.title("Original Image")
plt.imshow(image, cmap='gray')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.title("Contours Found")
plt.imshow(cv2.cvtColor(image_color, cv2.COLOR_BGR2RGB))
plt.axis('off')

plt.tight_layout()
plt.show()