import cv2
import numpy as np
import math
class PossibleChar:
    def __init__(self, _contour):
        self.contour = _contour
        self.boundingRect = cv2.boundingRect(self.contour)
        [intX, intY, intWidth, intHeight] = self.boundingRect
        self.intBoundingRectX = intX
        self.intBoundingRectY = intY
        self.intBoundingRectWidth = intWidth
        self.intBoundingRectHeight = intHeight
        self.intBoundingRectArea = self.intBoundingRectWidth * self.intBoundingRectHeight
        self.intCenterX = (self.intBoundingRectX + self.intBoundingRectX + self.intBoundingRectWidth) / 2
        self.intCenterY = (self.intBoundingRectY + self.intBoundingRectY + self.intBoundingRectHeight) / 2
        self.fltDiagonalSize = math.sqrt((self.intBoundingRectWidth ** 2) + (self.intBoundingRectHeight ** 2))
        self.fltAspectRatio = float(self.intBoundingRectWidth) / float(self.intBoundingRectHeight)
contour = np.array([[0, 0], [0, 10], [10, 10], [10, 0]])
possible_char = PossibleChar(contour)
print("Bounding Rect: ", possible_char.boundingRect)
print("Bounding Rect X: ", possible_char.intBoundingRectX)
print("Bounding Rect Y: ", possible_char.intBoundingRectY)
print("Bounding Rect Width: ", possible_char.intBoundingRectWidth)
print("Bounding Rect Height: ", possible_char.intBoundingRectHeight)
print("Bounding Rect Area: ", possible_char.intBoundingRectArea)
print("Center X: ", possible_char.intCenterX)
print("Center Y: ", possible_char.intCenterY)
print("Diagonal Size: ", possible_char.fltDiagonalSize)
print("Aspect Ratio: ", possible_char.fltAspectRatio)