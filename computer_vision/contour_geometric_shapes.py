import cv2
import numpy as np
import matplotlib.pyplot as plt

# خواندن تصویر
image = cv2.imread("shape.png")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
_, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY_INV)

# پیدا کردن کانتورها
contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

for cnt in contours:
    # به دست آوردن محیط کانتور
    peri = cv2.arcLength(cnt, True)

    # تقریب چندضلعی
    approx = cv2.approxPolyDP(cnt, 0.01 * peri, True)
    
    # پیدا کردن مرکز شکل برای نوشتن اسم
    M = cv2.moments(cnt)
    if M["m00"] != 0:
        cx = int(M["m10"] / M["m00"])
        cy = int(M["m01"] / M["m00"])
    else:
        cx, cy = 0, 0

    # مشخص کردن نوع شکل
    sides = len(approx)
    if sides == 3:
        shape = "Triangle"
    elif sides == 4:
        x, y, w, h = cv2.boundingRect(approx)
        aspect_ratio = float(w) / h
        shape = "Square" if 0.95 < aspect_ratio < 1.05 else "Rectangle"
    elif sides >= 5 and sides <= 6:
        shape = "Polygon"
    elif sides > 8:
        shape = "Circle"
    else:
        shape = "Unknown"

    # نمایش اسم شکل
    cv2.putText(image, shape, (cx, cy), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2)
    cv2.drawContours(image, [approx], 0, (0, 255, 0), 2)

plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
plt.title("Original Image")
plt.imshow(gray, cmap='gray')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.title("Contours Found")
plt.imshow(image, cmap='gray')
plt.axis('off')

plt.tight_layout()
plt.show()

