
import cv2
import numpy as np

# بارگذاری تصویر
image = cv2.imread("shape.png")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
_, threshold = cv2.threshold(gray, 240, 255, cv2.THRESH_BINARY)

# یافتن کانتورها
contours, _ = cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

for contour in contours:
    area = cv2.contourArea(contour)
    if area < 500:
        continue

    approx = cv2.approxPolyDP(contour, 0.01 * cv2.arcLength(contour, True), True)
    x, y, w, h = cv2.boundingRect(approx)
    center_x = x + w // 2
    center_y = y + h // 2

    if len(approx) == 3:
        shape_name = "Triangle"
    elif len(approx) == 4:
        aspect_ratio = float(w) / h
        if 0.95 <= aspect_ratio <= 1.05:
            shape_name = "Square"
        else:
            shape_name = "Rectangle"
    elif len(approx) == 5:
        shape_name = "Pentagon"
    elif len(approx) == 6:
        shape_name = "Hexagon"
    else:
        shape_name = "Circle"

    cv2.drawContours(image, [approx], 0, (0, 0, 0), 2)
    cv2.putText(image, shape_name, (center_x - 40, center_y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1)

cv2.imshow("Shapes", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
