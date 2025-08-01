import cv2
import matplotlib.pyplot as plt

image = cv2.imread("picture2.png")

gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

thresholds = [
    (50,100),
    (100,200),
    (150,250)
]

plt.figure(figsize=(15,5))


for i,(t1,t2) in enumerate(thresholds):
    edges = cv2.Canny(gray,t1,t2)
    plt.subplot(1,3,i+1)
    plt.imshow(edges , cmap="gray")
    plt.title(f"thresholds {t1} , {t2}")
    plt.axis('off')

plt.tight_layout()
plt.show()
