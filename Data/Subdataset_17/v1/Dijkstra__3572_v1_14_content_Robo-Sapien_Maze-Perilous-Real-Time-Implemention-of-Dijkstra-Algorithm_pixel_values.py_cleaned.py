import cv2
import numpy as np
img = cv2.imread('newa4.jpg')
ht, wt, channels = img.shape
print(img.shape)
font = cv2.FONT_HERSHEY_SIMPLEX
for i in range(0, ht, 100):
    for j in range(0, wt, 100):
        color = img[i, j]
        color_str = str(tuple(color))
        cv2.putText(img, color_str, (j, i), font, 0.4, (255, 255, 255), 1)
        cv2.circle(img, (j, i), 3, (255, 255, 255), 1)
cv2.imshow('Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()