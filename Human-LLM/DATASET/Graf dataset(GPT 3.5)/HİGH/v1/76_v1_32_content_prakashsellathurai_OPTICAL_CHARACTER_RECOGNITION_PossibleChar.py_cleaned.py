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
b1 = np.array([[0, 0], [0, 10], [10, 10], [10, 0]])
b12 = class1(b1)
print("Bounding Rect: ", b12.b2)
print("Bounding Rect X: ", b12.b3)
print("Bounding Rect Y: ", b12.b4)
print("Bounding Rect Width: ", b12.b5)
print("Bounding Rect Height: ", b12.b6)
print("Bounding Rect Area: ", b12.b7)
print("Center X: ", b12.b8)
print("Center Y: ", b12.b9)
print("Diagonal Size: ", b12.b10)
print("Aspect Ratio: ", b12.b11)