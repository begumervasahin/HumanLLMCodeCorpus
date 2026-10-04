import cv2
import numpy as np
import math
class PossibleChar:
    def __init__(self, contour):
        self.contour = contour
        self.boundingRect = cv2.boundingRect(self.contour)
        self.intBoundingRectX, self.intBoundingRectY, self.intBoundingRectWidth, self.intBoundingRectHeight = self.boundingRect
        self.intBoundingRectArea = self.intBoundingRectWidth * self.intBoundingRectHeight
        self.intCenterX = (self.intBoundingRectX * 2 + self.intBoundingRectWidth) / 2
        self.intCenterY = (self.intBoundingRectY * 2 + self.intBoundingRectHeight) / 2
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
        cv2.rectangle(imgContours,
                      (possibleChar.intBoundingRectX, possibleChar.intBoundingRectY),
                      (possibleChar.intBoundingRectX + possibleChar.intBoundingRectWidth, possibleChar.intBoundingRectY + possibleChar.intBoundingRectHeight),
                      (0, 255, 0), 2)
    cv2.imshow('Bounding Rectangles', imgContours)
    cv2.waitKey(0)
    cv2.destroyAllWindows()