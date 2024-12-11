import cv2
import numpy as np
def fonk1(image):
    b1 = cv2.FONT_HERSHEY_SIMPLEX
    a1 = 100
    height, width, b2 = image.shape
    print("Image shape:", image.shape)
    for i in range(0, height, a1):
        for j in range(0, width, a1):
            b3 = image[j, i]
            cv2.putText(image, str(b3), (i, j), b1, 0.4, (255, 255, 255), 2)
            cv2.circle(image, (i, j), 3, (255, 255, 255), 1)
    cv2.imshow('b5', image)
    cv2.waitKey(0) & 0xFF
    cv2.destroyAllWindows()
if b4 = = "__main__":
    b5 = cv2.imread('newa4.jpg')
    fonk1(b5)