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
def fonk2():
    b9 = cv2.imread('example.png', cv2.IMREAD_GRAYSCALE)
    if b9 is None:
        print("Error: Image not read from file.")
        return
    b11, b10 = cv2.threshold(b9, 100, 255, cv2.THRESH_BINARY_INV)
    contours, b11 = cv2.findContours(b10, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    b12 = [class1(b1) for b1 in contours]
    b13 = cv2.cvtColor(b9, cv2.COLOR_GRAY2BGR)
    for possible_char in b12:
        cv2.rectangle(b13,
                      (possible_char.intBoundingRectX, possible_char.intBoundingRectY),
                      (possible_char.intBoundingRectX + possible_char.intBoundingRectWidth, possible_char.intBoundingRectY + possible_char.b3),
                      (0, 255, 0), 2)
    cv2.imshow('Bounding Rectangles', b13)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
if b14 = = "__main__":
    fonk2()