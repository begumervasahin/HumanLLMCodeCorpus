import copy
from importer import *
class ContourWithData:
    def __init__(self):
        self.npaContour = None
        self.boundingRect = None
        self.intRectX = 0
        self.intRectY = 0
        self.intRectWidth = 0
        self.intRectHeight = 0
        self.fltArea = 0.0
    def calculate_rect_top_left_point_and_width_and_height(self):
        intX, intY, intWidth, intHeight = self.boundingRect
        self.intRectX = intX
        self.intRectY = intY - 555
        self.intRectWidth = intWidth
        self.intRectHeight = intHeight
    def is_contour_valid(self):
        return self.fltArea >= MIN_CONTOUR_AREA
def ndlist(init, *args):
    dp = init
    for x in reversed(args):
        dp = [copy.deepcopy(dp) for _ in range(x)]
    return dp
class Line:
    def __init__(self, column, width, img):
        self.column = column
        self.width = width
        self.img = img
    def __repr__(self):
        return f"Line(column={self.column}, width={self.width}, img={self.img})"