import cv2
import numpy as np
import math
class PossibleChar:
    def __init__(self, contour):
        self.contour = contour
        self.boundingRect = cv2.boundingRect(self.contour)
        (x, y, w, h) = self.boundingRect
        self.intBoundingRectX = x
        self.intBoundingRectY = y
        self.intBoundingRectWidth = w
        self.intBoundingRectHeight = h
        self.intBoundingRectArea = w * h
        self.intCenterX = (x + x + w) / 2
        self.intCenterY = (y + y + h) / 2
        self.fltDiagonalSize = math.sqrt(w ** 2 + h ** 2)
        self.fltAspectRatio = w / h