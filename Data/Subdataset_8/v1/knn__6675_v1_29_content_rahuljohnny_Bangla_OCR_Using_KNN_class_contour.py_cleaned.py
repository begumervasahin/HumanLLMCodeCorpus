import copy
MIN_CONTOUR_AREA = 100
class ContourWithData():
    npaContour = None
    boundingRect = None
    intRectX = 0
    intRectY = 0
    intRectWidth = 0
    intRectHeight = 0
    fltArea = 0.0
    def calculateRectTopLeftPointAndWidthAndHeight(self):
        [intX, intY, intWidth, intHeight] = self.boundingRect
        self.intRectX = intX
        self.intRectY = intY
        self.intRectWidth = intWidth
        self.intRectHeight = intHeight
    def checkIfContourIsValid(self):
        if self.fltArea < MIN_CONTOUR_AREA:
            return False
        return True
    def adjustIntRectY(self):
        self.intRectY -= 555
def ndlist(init, *args):
    dp = init
    for x in reversed(args):
        dp = [copy.deepcopy(dp) for _ in range(x)]
    return dp
if __name__ == "__main__":
    contour = ContourWithData()
    contour.boundingRect = [10, 20, 30, 40]
    contour.fltArea = 200.0
    contour.calculateRectTopLeftPointAndWidthAndHeight()
    print("Initial intRectY:", contour.intRectY)
    contour.adjustIntRectY()
    print("Adjusted intRectY:", contour.intRectY)
    nested_list = ndlist(0, 3, 4, 2)
    print("Nested list:", nested_list)