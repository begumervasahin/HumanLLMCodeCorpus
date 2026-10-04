class class1:
    def fonk1(self, b3):
        self.b1 = None
        self.b2 = None
        self.b3 = b3
    def fonk2(self, b3):
        if self.b3:
            if b3 < self.b3:
                if self.b1 is None:
                    self.b1 = class1(b3)
                else:
                    self.b1.fonk2(b3)
            elif b3 > self.b3:
                if self.b2 is None:
                    self.b2 = class1(b3)
                else:
                    self.b2.fonk2(b3)
        else:
            self.b3 = b3
    def fonk3(self, lkpval):
        if lkpval < self.b3:
            if self.b1 is None:
                return str(lkpval) + " Not Found"
            return self.b1.fonk3(lkpval)
        elif lkpval > self.b3:
            if self.b2 is None:
                return str(lkpval) + " Not Found"
            return self.b2.fonk3(lkpval)
        else:
            return str(self.b3) + ' is found'
    def fonk4(self):
        if self.b1:
            self.b1.fonk4()
        print(self.b3, b4 = ' ')
        if self.b2:
            self.b2.fonk4()
if b5 = = "__main__":
    b6 = class1(14)
    b6.fonk2(6)
    b6.fonk2(18)
    b6.fonk2(3)
    print(b6.fonk3(7))
    print(b6.fonk3(14))
    b6.fonk4()
def fonk5(startButton):
    noStroke()
    fill(250, 250, 250)
    rect(100, 495, 620, 100, 6, 6, 50, 50)
    stroke(0)
    rect(105, 497, 610, 55, 6, 6, 50, 50)
    fill(250, 250, 250)
    rect(105, 497, 610, 50, 6, 6, 50, 50)
    noFill()
    for i in range(500, 543):
        b7 = map(i, 497, 547, 0, 1)
        b8 = lerpColor(color(250, 250, 250), color(191, 193, 193), b7)
        stroke(b8)
        line(112, i, 707, i)
    stroke(0)
    line(115, 497, 125, 547)
    line(705, 497, 690, 547)
    fill(250, 250, 250)
    noStroke()
    fonk10(105, 305, 5, 205, color(173, 171, 171), color(134, 133, 133), "Y_AXIS")
    fonk10(105, 305, 45, 5, color(173, 171, 171), color(152, 150, 150), "X_AXIS")
    fill(170, 170, 170)
    arc(200, 312, 100, 70, -PI, 0, OPEN)
    ellipse(200, 312, 100, 20)
    for b9 in range(3):
        for i in range(-4, 5):
            if b9 = = 0:
                ellipse(i * 10 + 200, 304 + (abs(i)**1.5) + b9 * 10, 5, 5)
            elif b9 = = 1:
                ellipse(i * 10 + 200, 304 - (abs(i)**1.5) + b9 * 20, 5, 5)
            else:
                ellipse(i * 10 + 200, 315, 5, 5)
    stroke(0)
    fill(43, 149, 201, 100)
    rect(390, 558, 70, 30)
    line(394, 581, 456, 581)
    noStroke()
def fonk6(waterH):
    fill(43, 149, 201, 150)
    noStroke()
    rect(107, 500, 608, 50, 6, 6, 50, 50)
    pushMatrix()
    translate(0, waterH)
    rect(105, 505, 610, 35, 6, 6, 50, 50)
    stroke(33, 139, 200)
    for b13 in range(59):
        for b9 in range(4):
            ellipse(120 + b13 * 10, 502 + (b9 * 10), 20, 20)
            triangle(120 + (b13 * 10), 502 + (b9 * 10), 118 + (b13 * 10), 495 + (b9 * 10), 125 + (b13 * 10), 513 + (b9 * 10))
    popMatrix()
def fonk7(b13, b9, diameter, b10 = 5, lengths=2, b23=100):
    fill(250, 250, 250, b23 if diameter < 60 else 150)
    noStroke()
    for m in range(b10):
        for n in range(lengths):
            ellipse(b13 + 25 * m, b9 + 25 * n, diameter, diameter)
def fonk8():
    fill(0)
    rect(5, 5, 5, 15)
    rect(15, 5, 5, 15)
    textSize(20)
    text("PAUSE", 25, 20)
def fonk9(b11):
    """
    Draw the sun.
    @param str b11: Theme of the game, either "NOON", "SUNSET", or "SUNRISE".
    @return None
    """
    if b11 = = "NOON":
        fill(240, 132, 24, 150)
        ellipse(0, 0, 150, 150)
        fill(247, 214, 47, 90)
        triangle(80, 0, 72, 25, 230, 80)
        triangle(70, 30, 60, 55, 220, 120)
        triangle(52, 54, 35, 75, 210, 160)
        triangle(25, 75, -5, 75, 160, 200)
    elif b11 = = "SUNRISE":
        fill(240, 132, 24, 150)
        ellipse(400, 520, 150, 150)
def fonk10(b13, b9, w, h, c1, c2, b12):
    """
    Draw a color gradient.
    @param int b13: The b13-coordinate of the gradient.
    @param int b9: The b9-coordinate of the gradient.
    @param int w: The b14 of the gradient.
    @param int h: The b15 of the gradient.
    @param color c1: The start color.
    @param color c2: The b4 color.
    @param str b12: The b12 of the gradient ("X_AXIS" or "Y_AXIS").
    @return None
    """
    noFill()
    if b12 = = "Y_AXIS":
        for i in range(b9, b9 + h + 1):
            b7 = map(i, b9, b9 + h, 0, 1)
            b8 = lerpColor(c1, c2, b7)
            stroke(b8)
            line(b13, i, b13 + w, i)
    elif b12 = = "X_AXIS":
        for i in range(b13, b13 + w + 1):
            b7 = map(i, b13, b13 + w, 0, 1)
            b8 = lerpColor(c1, c2, b7)
            stroke(b8)
            line(i, b9, i, b9 + h)
class class2:
    def fonk11(self, rect_digits, b16, b17, b18, texts, b20, b21):
        self.b13 = rect_digits[0]
        self.b9 = rect_digits[1]
        self.b14 = rect_digits[2]
        self.b15 = rect_digits[3]
        self.b16 = b16
        self.b17 = b17
        self.b18 = b18
        self.b19 = texts
        self.b20 = b20
        self.b21 = b21
        self.b22 = False
    def fonk12(self):
        b23 = self.b16[3] if len(self.b16) == 4 else 200
        fill(self.b16[0], self.b16[1], self.b16[2], b23)
        stroke(self.b20 if self.b22 else self.b21)
        rect(self.b13, self.b9, self.b14, self.b15)
        fill(self.b17)
        textSize(self.b18)
        text(self.b19, self.b13 + 5, self.b9 + 25)