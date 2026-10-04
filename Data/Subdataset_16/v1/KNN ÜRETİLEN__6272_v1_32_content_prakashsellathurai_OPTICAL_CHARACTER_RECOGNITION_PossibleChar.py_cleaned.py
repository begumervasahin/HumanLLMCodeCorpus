import cv2
import numpy as np
import math
class class1:
    def fonk1(self, _contour):
        self.b1 = _contour
        self.b2 = cv2.b2(self.b1)
        [intX, intY, intWidth, intHeight] = self.b2
        self.b3 = intX
        self.b4 = intY
        self.b5 = intWidth
        self.b6 = intHeight
        self.b7 = self.b5 * self.b6
        self.b8 = (self.b3 + self.b3 + self.b5) / 2
        self.b9 = (self.b4 + self.b4 + self.b6) / 2
        self.b10 = math.sqrt((self.b5 ** 2) + (self.b6 ** 2))
        self.b11 = float(self.b5) / float(self.b6)
if b12 = = "__main__":
    b13 = cv2.imread('example.png', cv2.IMREAD_GRAYSCALE)
    if b13 is None:
        print("Error: Image not read from file.")
        exit()
    b15, b14 = cv2.threshold(b13, 100, 255, cv2.THRESH_BINARY_INV)
    contours, b15 = cv2.findContours(b14, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    b16 = [class1(b1) for b1 in contours]
    b17 = cv2.cvtColor(b13, cv2.COLOR_GRAY2BGR)
    for possibleChar in b16:
        cv2.rectangle(b17, (possibleChar.b3, possibleChar.b4),
                      (possibleChar.b3 + possibleChar.b5, possibleChar.b4 + possibleChar.b6),
                      (0, 255, 0), 2)
    cv2.imshow('Bounding Rectangles', b17)
    cv2.waitKey(0)
    cv2.destroyAllWindows()