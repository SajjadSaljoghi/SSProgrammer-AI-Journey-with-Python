import cv2
import numpy as np

# بارگذاری تصویر
image = cv2.imread("shape.png")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
_, thresh = cv2.threshold(gray, 240, 255, cv2.THRESH_BINARY)

# پیدا کردن کانتور‌ها
contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

for contour in contours:
    approx = cv2.approxPolyDP(contour, 0.01 * cv2.arcLength(contour, True), True)
    cv2.drawContours(image, [approx], 0, (0, 255, 0), 3)

    x = approx.ravel()[0]
    y = approx.ravel()[1] - 10

    if len(approx) == 3:
        cv2.putText(image, "Triangle", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0))
    elif len(approx) == 4:
        x1, y1, w, h = cv2.boundingRect(approx)
        aspectRatio = float(w)/h
        if 0.95 < aspectRatio < 1.05:
            cv2.putText(image, "Square", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0))
        else:
            cv2.putText(image, "Rectangle", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0))
    elif len(approx) == 5:
        cv2.putText(image, "Pentagon", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0))
    elif len(approx) > 5:
        cv2.putText(image, "Circle", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0))

cv2.imshow("Shapes", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
