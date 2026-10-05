import cv2
import numpy as np
import math
class PossibleChar:
    def __init__(self, contour):
        self.contour = contour
        self.bounding_rect = cv2.boundingRect(self.contour)
        self.calculate_features()
    def calculate_features(self):
        x, y, width, height = self.bounding_rect
        self.bounding_rect_x = x
        self.bounding_rect_y = y
        self.bounding_rect_width = width
        self.bounding_rect_height = height
        self.bounding_rect_area = self.bounding_rect_width * self.bounding_rect_height
        self.center_x = (self.bounding_rect_x + self.bounding_rect_x + self.bounding_rect_width) / 2
        self.center_y = (self.bounding_rect_y + self.bounding_rect_y + self.bounding_rect_height) / 2
        self.diagonal_size = math.sqrt((self.bounding_rect_width ** 2) + (self.bounding_rect_height ** 2))
        self.aspect_ratio = float(self.bounding_rect_width) / float(self.bounding_rect_height)
    def __str__(self):
        return (f"Bounding Rect: {self.bounding_rect}\n"
                f"Bounding Rect X: {self.bounding_rect_x}\n"
                f"Bounding Rect Y: {self.bounding_rect_y}\n"
                f"Bounding Rect Width: {self.bounding_rect_width}\n"
                f"Bounding Rect Height: {self.bounding_rect_height}\n"
                f"Bounding Rect Area: {self.bounding_rect_area}\n"
                f"Center X: {self.center_x}\n"
                f"Center Y: {self.center_y}\n"
                f"Diagonal Size: {self.diagonal_size}\n"
                f"Aspect Ratio: {self.aspect_ratio}")
contour = np.array([[0, 0], [0, 10], [10, 10], [10, 0]])
possible_char = PossibleChar(contour)
print(possible_char)