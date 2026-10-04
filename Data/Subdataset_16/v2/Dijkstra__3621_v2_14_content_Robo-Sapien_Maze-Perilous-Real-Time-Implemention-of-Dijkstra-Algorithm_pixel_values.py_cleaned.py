import cv2
import numpy as np
b1 = cv2.imread('newa4.jpg')
height, width, b2 = b1.shape
print(f"Image dimensions: {b1.shape}")
b3 = cv2.FONT_HERSHEY_SIMPLEX
for y in range(0, height, 100):
    for x in range(0, width, 100):
        b4 = b1[y, x]
        b5 = str(tuple(b4))
        cv2.putText(b1, b5, (x, y), b3, 0.4, (255, 255, 255), 1)
        cv2.circle(b1, (x, y), 3, (255, 255, 255), 1)
cv2.imshow('Annotated Image', b1)
cv2.waitKey(0)
cv2.destroyAllWindows()