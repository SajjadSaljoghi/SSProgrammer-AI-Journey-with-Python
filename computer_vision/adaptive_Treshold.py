import cv2
import matplotlib.pyplot as plt

# تصویر رو خاکستری می‌کنیم
image = cv2.imread("picture2.png", cv2.IMREAD_GRAYSCALE)

# اعمال آستانه تطبیقی Gaussian
adaptive_thresh = cv2.adaptiveThreshold(
    image,                     # تصویر خاکستری
    255,                       # مقدار ماکزیمم برای سفید
    cv2.ADAPTIVE_THRESH_GAUSSIAN_C,  # نوع آستانه تطبیقی (Gaussian)
    cv2.THRESH_BINARY,         # نوع آستانه نهایی
    11,                        # اندازه بلوک (باید فرد باشه)
    2                          # مقدار کاهشی از مقدار میانگین
)

# نمایش تصویر اصلی و خروجی در کنار هم
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.title("Original (Grayscale)")
plt.imshow(image, cmap="gray")
plt.axis("off")

plt.subplot(1, 2, 2)
plt.title("Adaptive Thresholding")
plt.imshow(adaptive_thresh, cmap="gray")
plt.axis("off")

plt.tight_layout()
plt.show()
