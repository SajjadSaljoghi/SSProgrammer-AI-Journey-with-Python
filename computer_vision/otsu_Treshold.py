import cv2
import matplotlib.pyplot as plt

# خواندن تصویر به صورت خاکستری
image = cv2.imread("picture2.png", cv2.IMREAD_GRAYSCALE)

# اعمال آستانه‌گذاری با الگوریتم Otsu
_, otsu_thresh = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

# نمایش آستانه به‌دست‌آمده
print("Otsu Threshold Value:", _)

# نمایش نتایج
plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.title("Original (Grayscale)")
plt.imshow(image, cmap="gray")
plt.axis("off")

plt.subplot(1, 2, 2)
plt.title("Otsu Thresholding")
plt.imshow(otsu_thresh, cmap="gray")
plt.axis("off")

plt.tight_layout()
plt.show()
