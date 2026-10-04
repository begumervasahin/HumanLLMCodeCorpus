import copy
from importer import *
class ContourWithData:
    def __init__(self):
        self.contour = None
        self.bounding_rect = None
        self.rect_x = 0
        self.rect_y = 0
        self.rect_width = 0
        self.rect_height = 0
        self.area = 0.0
    def calculate_rect_top_left_point_and_dimensions(self):
        x, y, width, height = self.bounding_rect
        self.rect_x = x
        self.rect_y = y - 555
        self.rect_width = width
        self.rect_height = height
    def is_contour_valid(self):
        return self.area >= MIN_CONTOUR_AREA
def create_ndlist(initial_value, *dimensions):
    result = initial_value
    for dim in reversed(dimensions):
        result = [copy.deepcopy(result) for _ in range(dim)]
    return result
class Line:
    def __init__(self, column, width, img):
        self.column = column
        self.width = width
        self.img = img
    def __repr__(self):
        return f"Line(column={self.column}, width={self.width}, img={self.img})"