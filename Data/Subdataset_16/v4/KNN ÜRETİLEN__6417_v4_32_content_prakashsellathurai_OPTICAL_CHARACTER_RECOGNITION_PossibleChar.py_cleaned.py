import cv2
import numpy as np
import math
class class1:
    def fonk1(self, b1):
        self.b1 = b1
        self.b2 = cv2.boundingRect(self.b1)
        self.intBoundingRectX, self.intBoundingRectY, self.intBoundingRectWidth, self.b3 = self.b2
        self.b4 = self.intBoundingRectWidth * self.b3
        self.b5 = (self.intBoundingRectX * 2 + self.intBoundingRectWidth)
        self.b6 = (self.intBoundingRectY * 2 + self.b3)
        self.b7 = math.sqrt((self.intBoundingRectWidth ** 2) + (self.b3 ** 2))
        self.b8 = float(self.intBoundingRectWidth) / float(self.b3)
    def fonk2(self):
        return (f"class1(b9 = {self.intBoundingRectX}, Y={self.intBoundingRectY}, "
                f"b10 = {self.intBoundingRectWidth}, Height={self.b3}, "
                f"b11 = {self.b4}, Center=({self.b5}, {self.b6}), "
                f"b12 = {self.b7:.2f}, AspectRatio={self.b8:.2f})")
