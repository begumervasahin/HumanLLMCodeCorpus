from processing import *
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
def fonk5():
    size(800, 600)
    background(255)
    noLoop()
def fonk6():
    fonk7("start")
    fonk8(100)
    fonk9(100, 100, 50)
    fonk10()
    fonk11("NOON")
    b5 = class2((200, 200, 200, 50), (255, 255, 255), (0, 0, 0), 12, "Enter Text", False, "default")
    b5.fonk14()
def fonk7(startButton):
    noStroke()
    fill(250, 250, 250)
    rect(100, 495, 620, 100, 6, 6, 50, 50)
    stroke(0)
    rect(105, 497, 610, 55, 6, 6, 50, 50)
    fill(200)
    rect(105, 497, 610, 50, 6, 6, 50, 50)
    noFill()
    for i in range(500, 543):
        b6 = map(i, 497, 547, 0, 1)
        b7 = lerpColor(color(250, 250, 250), color(191, 193, 193), b6)
        stroke(b7)
        line(112, i, 707, i)
    stroke(0)
    line(115, 497, 125, 547)
    line(705, 497, 690, 547)
    fill(250, 250, 250)
    noStroke()
    fonk12(105, 305, 5, 205, color(173, 171, 171), color(134, 133, 133), "Y_AXIS")
    fonk12(105, 305, 45, 5, color(173, 171, 171), color(152, 150, 150), "X_AXIS")
    noStroke()
    fill(170, 170, 170)
    arc(200, 312, 100, 70, -PI, 0, OPEN)
    fill(100)
    ellipse(200, 312, 100, 20)
    fill(170)
    for b8 in range(3):
        for i in range(-4, 5):
            if b8 = = 0:
                ellipse(i * 10 + 200, 304 + (abs(i)**1.5) + b8 * 10, 5, 5)
            elif b8 = = 1:
                ellipse(i * 10 + 200, 304 - (abs(i)**1.5) + b8 * 20, 5, 5)
            else:
                ellipse(i * 10 + 200, 315, 5, 5)
    fill(43, 149, 201, 100)
    rect(390, 558, 70, 30)
    line(394, 581, 456, 581)
    noStroke()
def fonk8(waterH):
    fill(0, 0, 255, 100)
    noStroke()
    rect(107, 500, 715 - 107, 50, 6, 6, 50, 50)
    pushMatrix()
    translate(0, waterH)
    fill(0, 0, 255, 100)
    rect(105, 505, 610, 35, 6, 6, 50, 50)
    stroke(33, 139, 300)
    for x in range(59):
        for b8 in range(4):
            ellipse(120 + x * 10, 502 + (b8 * 10), 20, 20)
            triangle(120 + (x * 10), 502 + (b8 * 10), 118 + (x * 10), 495 + (b8 * 10), 125 + (x * 10), 513 + (b8 * 10))
    popMatrix()
def fonk9(x, b8, diameter, b9 = 5, lengths=2, b21=100):
    if diameter < 60:
        fill(250, 250, 250, b21)
    else:
        fill(250, 250, 250, 150)
    noStroke()
    for m in range(b9):
        for n in range(lengths):
            ellipse(x + 25 * m, b8 + 25 * n, diameter, diameter)
    noStroke()
def fonk10():
    fill(0)
    rect(5, 5, 5, 15)
    rect(15, 5, 5, 15)
    textSize(20)
    b17("PAUSE", 25, 20)
def fonk11(b10):
    if b10 = = "NOON":
        fill(240, 132, 24, 150)
        ellipse(400, 100, 150, 150)
        fill(247, 214, 47, 90)
        triangle(480, 100, 472, 125, 630, 180)
        triangle(470, 130, 460, 155, 620, 240)
        triangle(452, 154, 435, 175, 610, 280)
        triangle(425, 175, 395, 175, 560, 320)
    elif b10 = = "SUNRISE":
        fill(240, 132, 24, 150)
        ellipse(400, 520, 150, 150)
def fonk12(x, b8, w, h, c1, c2, b11):
    noFill()
    if b11 = = "Y_AXIS":
        for i in range(b8, b8 + h + 1):
            b6 = map(i, b8, b8 + h, 0, 1)
            b7 = lerpColor(c1, c2, b6)
            stroke(b7)
            line(x, i, x + w, i)
    elif b11 = = "X_AXIS":
        for i in range(x, x + w + 1):
            b6 = map(i, x, x + w, 0, 1)
            b7 = lerpColor(c1, c2, b6)
            stroke(b7)
            line(i, b8, i, b8 + h)
class class2:
    def fonk13(self, rect_params, b14, b15, b16, b17, b12, default):
        self.b12 = b12
        self.x, self.b8, self.width, self.b13 = rect_params
        self.b14 = b14
        self.b15 = b15
        self.b16 = b16
        self.b17 = b17
        self.b18 = b12
        self.b19 = default
        self.b20 = default
    def fonk14(self):
        b21 = 200 if len(self.b14) == 3 else self.b14[3]
        fill(self.b14[0], self.b14[1], self.b14[2], b21)
        self.b20 = self.b18 if self.b12 else self.b19
        stroke(self.b20)
        rect(self.x, self.b8, self.width, self.b13)
        fill(self.b15)
        textSize(self.b16)
        b17(self.b17, self.x + 5, self.b8 + 25)
if b22 = = "__main__":
    b23 = class1(14)
    b23.fonk2(6)
    b23.fonk2(18)
    b23.fonk2(3)
    print(b23.fonk3(7))
    print(b23.fonk3(14))
    b23.fonk4()
