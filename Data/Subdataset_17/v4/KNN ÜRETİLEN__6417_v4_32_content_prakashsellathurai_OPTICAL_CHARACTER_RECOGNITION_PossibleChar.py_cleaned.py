import cv2
import numpy as np
import math
class PossibleChar:
    def __init__(self, contour):
        self.contour = contour
        self.bounding_rect = cv2.boundingRect(self.contour)
        self.intBoundingRectX, self.intBoundingRectY, self.intBoundingRectWidth, self.intBoundingRectHeight = self.bounding_rect
        self.intBoundingRectArea = self.intBoundingRectWidth * self.intBoundingRectHeight
        self.intCenterX = (self.intBoundingRectX * 2 + self.intBoundingRectWidth)
        self.intCenterY = (self.intBoundingRectY * 2 + self.intBoundingRectHeight)
        self.fltDiagonalSize = math.sqrt((self.intBoundingRectWidth ** 2) + (self.intBoundingRectHeight ** 2))
        self.fltAspectRatio = float(self.intBoundingRectWidth) / float(self.intBoundingRectHeight)
    def __repr__(self):
        return (f"PossibleChar(X={self.intBoundingRectX}, Y={self.intBoundingRectY}, "
                f"Width={self.intBoundingRectWidth}, Height={self.intBoundingRectHeight}, "
                f"Area={self.intBoundingRectArea}, Center=({self.intCenterX}, {self.intCenterY}), "
                f"Diagonal={self.fltDiagonalSize:.2f}, AspectRatio={self.fltAspectRatio:.2f})")
