import cv2
import numpy as np
img = cv2.imread('newa4.jpg')
height, width, channels = img.shape
print(f"Image dimensions: {img.shape}")
font = cv2.FONT_HERSHEY_SIMPLEX
for y in range(0, height, 100):
    for x in range(0, width, 100):
        color = img[y, x]
        color_str = str(tuple(color))
        cv2.putText(img, color_str, (x, y), font, 0.4, (255, 255, 255), 1)
        cv2.circle(img, (x, y), 3, (255, 255, 255), 1)
cv2.imshow('Annotated Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()