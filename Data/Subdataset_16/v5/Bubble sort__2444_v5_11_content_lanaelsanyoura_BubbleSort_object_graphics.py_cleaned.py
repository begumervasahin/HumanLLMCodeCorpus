class class1:
    def fonk1(self, b3):
        self.b1 = None
        self.b2 = None
        self.b3 = b3
    def fonk2(self, b3):
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
    def fonk3(self, value):
        if value < self.b3:
            if self.b1 is None:
                return f"{value} Not Found"
            return self.b1.fonk3(value)
        elif value > self.b3:
            if self.b2 is None:
                return f"{value} Not Found"
            return self.b2.fonk3(value)
        else:
            return f"{self.b3} is found"
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
def fonk5(start_button):
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
    for y in range(3):
        for i in range(-4, 5):
            ellipse(i * 10 + 200, 304 + (abs(i)**1.5) + y * 10, 5, 5)
    stroke(0)
    fill(43, 149, 201, 100)
    rect(390, 558, 70, 30)
    line(394, 581, 456, 581)
    noStroke()
def fonk6(b12):
    fill(43, 149, 201, 150)
    noStroke()
    rect(107, 500, 608, 50, 6, 6, 50, 50)
    pushMatrix()
    translate(0, b12)
    rect(105, 505, 610, 35, 6, 6, 50, 50)
    stroke(33, 139, 200)
    for x in range(59):
        for y in range(4):
            ellipse(120 + x * 10, 502 + (y * 10), 20, 20)
            triangle(120 + (x * 10), 502 + (y * 10), 118 + (x * 10), 495 + (y * 10), 125 + (x * 10), 513 + (y * 10))
    popMatrix()
def fonk7(x, y, diameter, b9 = 5, lengths=2, b20=100):
    fill(250, 250, 250, b20 if diameter < 60 else 150)
    noStroke()
    for m in range(b9):
        for n in range(lengths):
            ellipse(x + 25 * m, y + 25 * n, diameter, diameter)
def fonk8():
    fill(0)
    rect(5, 5, 5, 15)
    rect(15, 5, 5, 15)
    textSize(20)
    b16("PAUSE", 25, 20)
def fonk9(b10):
    if b10 = = "NOON":
        fill(240, 132, 24, 150)
        ellipse(0, 0, 150, 150)
        fill(247, 214, 47, 90)
        triangle(80, 0, 72, 25, 230, 80)
        triangle(70, 30, 60, 55, 220, 120)
        triangle(52, 54, 35, 75, 210, 160)
        triangle(25, 75, -5, 75, 160, 200)
    elif b10 = = "SUNRISE":
        fill(240, 132, 24, 150)
        ellipse(400, 520, 150, 150)
def fonk10(x, y, w, h, c1, c2, b11):
    noFill()
    if b11 = = "Y_AXIS":
        for i in range(y, y + h + 1):
            b7 = map(i, y, y + h, 0, 1)
            b8 = lerpColor(c1, c2, b7)
            stroke(b8)
            line(x, i, x + w, i)
    elif b11 = = "X_AXIS":
        for i in range(x, x + w + 1):
            b7 = map(i, x, x + w, 0, 1)
            b8 = lerpColor(c1, c2, b7)
            stroke(b8)
            line(i, y, i, y + h)
class class2:
    def fonk11(self, rect_params, b13, b14, b15, b16, b17, b18):
        self.x, self.y, self.width, self.b12 = rect_params
        self.b13 = b13
        self.b14 = b14
        self.b15 = b15
        self.b16 = b16
        self.b17 = b17
        self.b18 = b18
        self.b19 = False
    def fonk12(self):
        b20 = self.b13[3] if len(self.b13) == 4 else 200
        fill(self.b13[0], self.b13[1], self.b13[2], b20)
        stroke(self.b17 if self.b19 else self.b18)
        rect(self.x, self.y, self.width, self.b12)
        fill(self.b14)
        textSize(self.b15)
        b16(self.b16, self.x + 5, self.y + 25)