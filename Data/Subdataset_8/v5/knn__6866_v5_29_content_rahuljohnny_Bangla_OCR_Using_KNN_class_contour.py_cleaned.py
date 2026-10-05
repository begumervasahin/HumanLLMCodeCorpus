import copy
from importer import *
class ContourWithData():
    def __init__(self):
        self.npaContour = None
        self.boundingRect = None
        self.intRectX = 0
        self.intRectY = 0
        self.intRectWidth = 0
        self.intRectHeight = 0
        self.fltArea = 0.0
    def calculateRectTopLeftPointAndWidthAndHeight(self):
        intX, intY, intWidth, intHeight = self.boundingRect
        self.intRectX = intX
        self.intRectY = intY
        self.intRectWidth = intWidth
        self.intRectHeight = intHeight
    def checkIfContourIsValid(self):
        return self.fltArea >= MIN_CONTOUR_AREA
    def adjustRectY(self):
        self.intRectY -= 555
def ndlist(init, *args):
    dp = init
    for x in reversed(args):
        dp = [copy.deepcopy(dp) for _ in range(x)]
    return dp
