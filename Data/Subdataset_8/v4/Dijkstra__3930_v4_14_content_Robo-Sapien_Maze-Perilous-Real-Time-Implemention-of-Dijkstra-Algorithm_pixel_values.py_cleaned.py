
import cv2
import numpy as np
img = cv2.imread('newa4.jpg')
height, width, channels = img.shape
print("Image shape:", img.shape)
font = cv2.FONT_HERSHEY_SIMPLEX
for i in range(0, height, 100):
    for j in range(0, width, 100):
        color = img[j, i]
        cv2.putText(img, str(color), (i, j), font, 0.4, (255, 255, 255), 2)
        cv2.circle(img, (i, j), 3, (255, 255, 255), 1)
cv2.imshow('img', img)
cv2.waitKey(0) & 0xFF
cv2.destroyAllWindows()