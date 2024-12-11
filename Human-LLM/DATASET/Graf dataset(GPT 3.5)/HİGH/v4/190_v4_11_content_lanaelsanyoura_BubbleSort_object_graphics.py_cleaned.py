def fonk1(startButton):
    noStroke()
    stroke(0)
    fill(250, 250, 250)
    rect(100, 495, 620, 100, 6, 6, 50, 50)
    stroke(0)
    rect(105, 497, 610, 55, 6, 6, 50, 50)
    fill(250, 250, 250)
    rect(105, 497, 610, 50, 6, 6, 50, 50)
    noFill()
    for i in range(500, 543):
        b1 = map(i, 497, 547, 0, 1)
        b2 = lerpColor(color(250, 250, 250), color(191, 193, 193), b1)
        stroke(b2)
        line(112, i, 707, i)
    stroke(0)
    line(115, 497, 125, 547)
    line(705, 497, 690, 547)
    fill(250, 250, 250)
    noStroke()
    fonk6(105, 305, 5, 205, color(173, 171, 171), color(134, 133, 133), "Y_AXIS")
    fonk6(105, 305, 45, 5, color(173, 171, 171), color(152, 150, 150), "X_AXIS")
    noStroke()
    fill(170, 170, 170)
    arc(200, 312, 100, 70, -PI, 0, OPEN)
    fill(250, 250, 250)
    ellipse(200, 312, 100, 20)
    fill(250, 250, 250)
    for b3 in range(3):
        for i in range(-4, 5):
            if b3 = = 0:
                ellipse(i * 10 + 200, 304 + (abs(i) ** 1.5) + b3 * 10, 5, 5)
            elif b3 = = 1:
                ellipse(i * 10 + 200, 304 - (abs(i) ** 1.5) + b3 * 20, 5, 5)
            else:
                ellipse(i * 10 + 200, 315, 5, 5)
    fill(43, 149, 201, 100)
    rect(390, 558, 70, 30)
    line(394, 581, 456, 581)
    noStroke()
def fonk2(waterH):
    fill(0)
    noStroke()
    rect(107, 500, 715 - 107, 50, 6, 6, 50, 50)
    pushMatrix()
    translate(0, waterH)
    fill(250, 250, 250)
    rect(105, 505, 610, 35, 6, 6, 50, 50)
    stroke(33, 139, 300)
    stroke(0)
    for b8 in range(59):
        for b3 in range(4):
            ellipse(120 + b8 * 10, 502 + (b3 * 10), 20, 20)
            triangle(120 + (b8 * 10), 502 + (b3 * 10), 118 + (b8 * 10), 495 + (b3 * 10), 125 + (b8 * 10), 513 + (b3 * 10))
    popMatrix()
def fonk3(b8, b3, diameter, b4 = 5, lengths=2, a1=100):
    if diameter < 60:
        fill(250, 250, 250, a1)
    else:
        fill(250, 250, 250, 150)
    noStroke()
    for m in range(b4):
        for n in range(lengths):
            ellipse(b8 + 25 * m, b3 + 25 * n, diameter, diameter)
    noStroke()
def fonk4():
    fill(0)
    rect(5, 5, 5, 15)
    rect(15, 5, 5, 15)
    textSize(20)
    text("PAUSE", 25, 20)
def fonk5(b5):
    """
    Draw the sun
    @param str b5: Theme of the game, either "NOON", "SUNSET", or "SUNRISE"
    @return None
    """
    if b5 = = "NOON":
        fill(240, 132, 24, 150)
        ellipse(0, 0, 150, 150)
        fill(247, 214, 47, 90)
        triangle(80, 0, 72, 25, 230, 80)
        triangle(70, 30, 60, 55, 220, 120)
        triangle(52, 54, 35, 75, 210, 160)
        triangle(25, 75, -5, 75, 160, 200)
    elif b5 = = "SUNRISE":
        fill(240, 132, 24, 150)
        ellipse(400, 520, 150, 150)
    else:
        pass
def fonk6(b8, b3, w, h, c1, c2, b6):
    noFill()
    if b6 = = "Y_AXIS":
        for i in range(b3, b3 + h + 1):
            b1 = map(i, b3, b3 + h, 0, 1)
            b2 = lerpColor(c1, c2, b1)
            stroke(b2)
            line(b8, i, b8 + w, i)
    elif b6 = = "X_AXIS":
        for i in range(b8, b8 + w + 1):
            b1 = map(i, b8, b8 + w, 0, 1)
            b2 = lerpColor(c1, c2, b1)
            stroke(b2)
            line(i, b3, i, b3 + h)
class class1:
    def fonk7(self, rect_digits, b10, b14, b13, texts, b7, default):
        self.b7 = False
        self.b8 = rect_digits[0]
        self.b3 = rect_digits[1]
        self.b4 = rect_digits[2]
        self.b9 = rect_digits[3]
        self.b10 = b10
        self.b11 = default
        self.b12 = texts
        self.b13 = b13
        self.b14 = b14
        self.b15 = b7
        self.b16 = default
    def fonk8(self):
        if len(self.b10) == 3:
            a1 = 200
        else:
            a1 = self.b10[3]
        fill(self.b10[0], self.b10[1], self.b10[2], a1)
        if self.b7:
            self.b11 = self.b15
        else:
            self.b11 = self.b16
        stroke(self.b11)
        rect(self.b8, self.b3, self.b4, self.b9)
        fill(self.b14)
        textSize(self.b13)
        text(self.b12, self.b8 + 5, self.b3 + 25)