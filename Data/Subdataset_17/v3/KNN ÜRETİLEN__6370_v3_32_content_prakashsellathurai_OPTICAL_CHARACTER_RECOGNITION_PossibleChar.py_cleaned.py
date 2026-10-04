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
def main():
    img = cv2.imread('example.png', cv2.IMREAD_GRAYSCALE)
    if img is None:
        print("Error: Image not read from file.")
        return
    _, img_thresh = cv2.threshold(img, 100, 255, cv2.THRESH_BINARY_INV)
    contours, _ = cv2.findContours(img_thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    possible_chars = [PossibleChar(contour) for contour in contours]
    img_contours = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
    for possible_char in possible_chars:
        cv2.rectangle(img_contours,
                      (possible_char.intBoundingRectX, possible_char.intBoundingRectY),
                      (possible_char.intBoundingRectX + possible_char.intBoundingRectWidth, possible_char.intBoundingRectY + possible_char.intBoundingRectHeight),
                      (0, 255, 0), 2)
    cv2.imshow('Bounding Rectangles', img_contours)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
if __name__ == "__main__":
    main()