import cv2
import numpy as np
import math
class class1:
    def fonk1(self, b1):
        self.b1 = b1
        self.b2 = cv2.boundingRect(self.b1)
        self.fonk2()
    def fonk2(self):
        x, y, width, b3 = self.b2
        self.b4 = x
        self.b5 = y
        self.b6 = width
        self.b7 = b3
        self.b8 = self.b6 * self.b7
        self.b9 = (self.b4 + self.b4 + self.b6) / 2
        self.b10 = (self.b5 + self.b5 + self.b7) / 2
        self.b11 = math.sqrt((self.b6 ** 2) + (self.b7 ** 2))
        self.b12 = float(self.b6) / float(self.b7)
b1 = np.array([[0, 0], [0, 10], [10, 10], [10, 0]])
b13 = class1(b1)
print("Bounding Rect: ", b13.b2)
print("Bounding Rect X: ", b13.b4)
print("Bounding Rect Y: ", b13.b5)
print("Bounding Rect Width: ", b13.b6)
print("Bounding Rect Height: ", b13.b7)
print("Bounding Rect Area: ", b13.b8)
print("Center X: ", b13.b9)
print("Center Y: ", b13.b10)
print("Diagonal Size: ", b13.b11)
print("Aspect Ratio: ", b13.b12)