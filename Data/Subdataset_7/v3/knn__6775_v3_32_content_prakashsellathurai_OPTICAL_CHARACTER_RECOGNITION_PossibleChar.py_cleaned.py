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
    def fonk3(self):
        return (f"Bounding Rect: {self.b2}\n"
                f"Bounding Rect X: {self.b4}\n"
                f"Bounding Rect Y: {self.b5}\n"
                f"Bounding Rect Width: {self.b6}\n"
                f"Bounding Rect Height: {self.b7}\n"
                f"Bounding Rect Area: {self.b8}\n"
                f"Center X: {self.b9}\n"
                f"Center Y: {self.b10}\n"
                f"Diagonal Size: {self.b11}\n"
                f"Aspect Ratio: {self.b12}")
b1 = np.array([[0, 0], [0, 10], [10, 10], [10, 0]])
b13 = class1(b1)
print(b13)