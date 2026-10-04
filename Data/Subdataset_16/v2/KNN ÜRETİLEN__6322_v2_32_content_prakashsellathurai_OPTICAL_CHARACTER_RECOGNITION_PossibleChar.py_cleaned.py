import cv2
import numpy as np
import math
class class1:
    def fonk1(self, b1):
        self.b1 = b1
        self.b2 = cv2.b2(self.b1)
        self.intBoundingRectX, self.intBoundingRectY, self.intBoundingRectWidth, self.b3 = self.b2
        self.b4 = self.intBoundingRectWidth * self.b3
        self.b5 = (self.intBoundingRectX * 2 + self.intBoundingRectWidth) / 2
        self.b6 = (self.intBoundingRectY * 2 + self.b3) / 2
        self.b7 = math.sqrt((self.intBoundingRectWidth ** 2) + (self.b3 ** 2))
        self.b8 = float(self.intBoundingRectWidth) / float(self.b3)
if b9 = = "__main__":
    b10 = cv2.imread('example.png', cv2.IMREAD_GRAYSCALE)
    if b10 is None:
        print("Error: Image not read from file.")
        exit()
    b12, b11 = cv2.threshold(b10, 100, 255, cv2.THRESH_BINARY_INV)
    contours, b12 = cv2.findContours(b11, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    b13 = [class1(b1) for b1 in contours]
    b14 = cv2.cvtColor(b10, cv2.COLOR_GRAY2BGR)
    for possibleChar in b13:
        cv2.rectangle(b14,
                      (possibleChar.intBoundingRectX, possibleChar.intBoundingRectY),
                      (possibleChar.intBoundingRectX + possibleChar.intBoundingRectWidth, possibleChar.intBoundingRectY + possibleChar.b3),
                      (0, 255, 0), 2)
    cv2.imshow('Bounding Rectangles', b14)
    cv2.waitKey(0)
    cv2.destroyAllWindows()