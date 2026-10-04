class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data
    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data
    def findval(self, lkpval):
        if lkpval < self.data:
            if self.left is None:
                return str(lkpval) + " Not Found"
            return self.left.findval(lkpval)
        elif lkpval > self.data:
            if self.right is None:
                return str(lkpval) + " Not Found"
            return self.right.findval(lkpval)
        else:
            return str(self.data) + ' is found'
    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print(self.data, end=' ')
        if self.right:
            self.right.PrintTree()
if __name__ == "__main__":
    root = Node(14)
    root.insert(6)
    root.insert(18)
    root.insert(3)
    print(root.findval(7))
    print(root.findval(14))
    root.PrintTree()
def tub(startButton):
    noStroke()
    fill(250, 250, 250)
    rect(100, 495, 620, 100, 6, 6, 50, 50)
    stroke(0)
    rect(105, 497, 610, 55, 6, 6, 50, 50)
    fill(250, 250, 250)
    rect(105, 497, 610, 50, 6, 6, 50, 50)
    noFill()
    for i in range(500, 543):
        inter = map(i, 497, 547, 0, 1)
        c = lerpColor(color(250, 250, 250), color(191, 193, 193), inter)
        stroke(c)
        line(112, i, 707, i)
    stroke(0)
    line(115, 497, 125, 547)
    line(705, 497, 690, 547)
    fill(250, 250, 250)
    noStroke()
    setGradient(105, 305, 5, 205, color(173, 171, 171), color(134, 133, 133), "Y_AXIS")
    setGradient(105, 305, 45, 5, color(173, 171, 171), color(152, 150, 150), "X_AXIS")
    fill(170, 170, 170)
    arc(200, 312, 100, 70, -PI, 0, OPEN)
    ellipse(200, 312, 100, 20)
    for y in range(3):
        for i in range(-4, 5):
            if y == 0:
                ellipse(i * 10 + 200, 304 + (abs(i)**1.5) + y * 10, 5, 5)
            elif y == 1:
                ellipse(i * 10 + 200, 304 - (abs(i)**1.5) + y * 20, 5, 5)
            else:
                ellipse(i * 10 + 200, 315, 5, 5)
    stroke(0)
    fill(43, 149, 201, 100)
    rect(390, 558, 70, 30)
    line(394, 581, 456, 581)
    noStroke()
def water(waterH):
    fill(43, 149, 201, 150)
    noStroke()
    rect(107, 500, 608, 50, 6, 6, 50, 50)
    pushMatrix()
    translate(0, waterH)
    rect(105, 505, 610, 35, 6, 6, 50, 50)
    stroke(33, 139, 200)
    for x in range(59):
        for y in range(4):
            ellipse(120 + x * 10, 502 + (y * 10), 20, 20)
            triangle(120 + (x * 10), 502 + (y * 10), 118 + (x * 10), 495 + (y * 10), 125 + (x * 10), 513 + (y * 10))
    popMatrix()
def clouds(x, y, diameter, widths=5, lengths=2, transparency=100):
    fill(250, 250, 250, transparency if diameter < 60 else 150)
    noStroke()
    for m in range(widths):
        for n in range(lengths):
            ellipse(x + 25 * m, y + 25 * n, diameter, diameter)
def pause():
    fill(0)
    rect(5, 5, 5, 15)
    rect(15, 5, 5, 15)
    textSize(20)
    text("PAUSE", 25, 20)
def sun(theme):
    """
    Draw the sun.
    @param str theme: Theme of the game, either "NOON", "SUNSET", or "SUNRISE".
    @return None
    """
    if theme == "NOON":
        fill(240, 132, 24, 150)
        ellipse(0, 0, 150, 150)
        fill(247, 214, 47, 90)
        triangle(80, 0, 72, 25, 230, 80)
        triangle(70, 30, 60, 55, 220, 120)
        triangle(52, 54, 35, 75, 210, 160)
        triangle(25, 75, -5, 75, 160, 200)
    elif theme == "SUNRISE":
        fill(240, 132, 24, 150)
        ellipse(400, 520, 150, 150)
def setGradient(x, y, w, h, c1, c2, axis):
    """
    Draw a color gradient.
    @param int x: The x-coordinate of the gradient.
    @param int y: The y-coordinate of the gradient.
    @param int w: The width of the gradient.
    @param int h: The height of the gradient.
    @param color c1: The start color.
    @param color c2: The end color.
    @param str axis: The axis of the gradient ("X_AXIS" or "Y_AXIS").
    @return None
    """
    noFill()
    if axis == "Y_AXIS":
        for i in range(y, y + h + 1):
            inter = map(i, y, y + h, 0, 1)
            c = lerpColor(c1, c2, inter)
            stroke(c)
            line(x, i, x + w, i)
    elif axis == "X_AXIS":
        for i in range(x, x + w + 1):
            inter = map(i, x, x + w, 0, 1)
            c = lerpColor(c1, c2, inter)
            stroke(c)
            line(i, y, i, y + h)
class TextBox:
    def __init__(self, rect_digits, rect_fill, text_fill, text_size, texts, selected_stroke, default_stroke):
        self.x = rect_digits[0]
        self.y = rect_digits[1]
        self.width = rect_digits[2]
        self.height = rect_digits[3]
        self.rect_fill = rect_fill
        self.text_fill = text_fill
        self.text_size = text_size
        self.text_box = texts
        self.selected_stroke = selected_stroke
        self.default_stroke = default_stroke
        self.selected = False
    def draw_box(self):
        transparency = self.rect_fill[3] if len(self.rect_fill) == 4 else 200
        fill(self.rect_fill[0], self.rect_fill[1], self.rect_fill[2], transparency)
        stroke(self.selected_stroke if self.selected else self.default_stroke)
        rect(self.x, self.y, self.width, self.height)
        fill(self.text_fill)
        textSize(self.text_size)
        text(self.text_box, self.x + 5, self.y + 25)