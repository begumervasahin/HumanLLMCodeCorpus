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
if __name__ == "__main__":
    img = cv2.imread('example.png', cv2.IMREAD_GRAYSCALE)
    if img is None:
        print("Error: Image not read from file.")
        exit()
    _, imgThresh = cv2.threshold(img, 100, 255, cv2.THRESH_BINARY_INV)
    contours, _ = cv2.findContours(imgThresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    possibleChars = [PossibleChar(contour) for contour in contours]
    imgContours = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
    for possibleChar in possibleChars:
        cv2.rectangle(imgContours, (possibleChar.intBoundingRectX, possibleChar.intBoundingRectY),
                      (possibleChar.intBoundingRectX + possibleChar.intBoundingRectWidth, possibleChar.intBoundingRectY + possibleChar.intBoundingRectHeight),
                      (0, 255, 0), 2)
    cv2.imshow('Bounding Rectangles', imgContours)
    cv2.waitKey(0)
    cv2.destroyAllWindows()