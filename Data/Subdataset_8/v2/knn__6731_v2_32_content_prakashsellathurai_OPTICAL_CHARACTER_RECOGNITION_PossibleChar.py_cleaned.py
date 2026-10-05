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
contour = np.array([[0, 0], [0, 10], [10, 10], [10, 0]])
possible_char = PossibleChar(contour)
print("Bounding Rect: ", possible_char.bounding_rect)
print("Bounding Rect X: ", possible_char.bounding_rect_x)
print("Bounding Rect Y: ", possible_char.bounding_rect_y)
print("Bounding Rect Width: ", possible_char.bounding_rect_width)
print("Bounding Rect Height: ", possible_char.bounding_rect_height)
print("Bounding Rect Area: ", possible_char.bounding_rect_area)
print("Center X: ", possible_char.center_x)
print("Center Y: ", possible_char.center_y)
print("Diagonal Size: ", possible_char.diagonal_size)
print("Aspect Ratio: ", possible_char.aspect_ratio)