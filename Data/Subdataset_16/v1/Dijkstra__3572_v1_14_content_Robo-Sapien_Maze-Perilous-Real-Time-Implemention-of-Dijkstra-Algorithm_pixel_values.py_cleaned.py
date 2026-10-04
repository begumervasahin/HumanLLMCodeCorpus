import cv2
import numpy as np
b1 = cv2.imread('newa4.jpg')
ht, wt, b2 = b1.shape
print(b1.shape)
b3 = cv2.FONT_HERSHEY_SIMPLEX
for i in range(0, ht, 100):
    for j in range(0, wt, 100):
        b4 = b1[i, j]
        b5 = str(tuple(b4))
        cv2.putText(b1, b5, (j, i), b3, 0.4, (255, 255, 255), 1)
        cv2.circle(b1, (j, i), 3, (255, 255, 255), 1)
cv2.imshow('Image', b1)
cv2.waitKey(0)
cv2.destroyAllWindows()