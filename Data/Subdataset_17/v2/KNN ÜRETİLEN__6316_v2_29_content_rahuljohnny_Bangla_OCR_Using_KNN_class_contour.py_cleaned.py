import copy
MIN_CONTOUR_AREA = 100
class ContourWithData:
    def __init__(self):
        self.npaContour = None
        self.boundingRect = None
        self.intRectX = 0
        self.intRectY = 0
        self.intRectWidth = 0
        self.intRectHeight = 0
        self.fltArea = 0.0
    def calculateRectTopLeftPointAndWidthAndHeight(self):
        [intX, intY, intWidth, intHeight] = self.boundingRect
        self.intRectX = intX
        self.intRectY = intY
        self.intRectWidth = intWidth
        self.intRectHeight = intHeight
    def checkIfContourIsValid(self):
        return self.fltArea >= MIN_CONTOUR_AREA
    def adjustIntRectY(self, adjustment):
        self.intRectY -= adjustment
def ndlist(init, *args):
    dp = init
    for x in reversed(args):
        dp = [copy.deepcopy(dp) for _ in range(x)]
    return dp
if __name__ == "__main__":
    contour = ContourWithData()
    contour.boundingRect = [50, 100, 200, 300]
    contour.fltArea = 150.0
    contour.calculateRectTopLeftPointAndWidthAndHeight()
    print(f"Rectangle X: {contour.intRectX}, Y: {contour.intRectY}, Width: {contour.intRectWidth}, Height: {contour.intRectHeight}")
    is_valid = contour.checkIfContourIsValid()
    print(f"Is Contour Valid? {'Yes' if is_valid else 'No'}")
    contour.adjustIntRectY(555)
    print(f"Adjusted Rectangle Y: {contour.intRectY}")
    my_list = ndlist(0, 2, 3, 4)
    print(f"3D List: {my_list}")