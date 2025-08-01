import cv2
import matplotlib.pyplot as plt

image = cv2.imread("picture2.png")

avg_blur = cv2.blur(image , (5,5))

gaussian_blur = cv2.GaussianBlur(image , (5,5) , 0)

median_blur = cv2.medianBlur(image,5)

fig, axs = plt.subplots(2, 2, figsize=(10, 8))
fig.suptitle("Blur Comparison", fontsize=16)

axs[0, 0].imshow(image)
axs[0, 0].set_title("Original")
axs[0, 0].axis("off")

axs[0, 1].imshow(avg_blur)
axs[0, 1].set_title("Average Blur")
axs[0, 1].axis("off")


axs[1, 0].imshow(gaussian_blur)
axs[1, 0].set_title("Gaussian Blur")
axs[1, 0].axis("off")

axs[1, 1].imshow(median_blur)
axs[1, 1].set_title("Median Blur")
axs[1, 1].axis("off")

plt.tight_layout()
plt.show()