
def draw_tub():
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
        inter = map(i, 497, 547, 0, 1)
        c = lerpColor(color(250, 250, 250), color(191, 193, 193), inter)
        stroke(c)
        line(112, i, 707, i)
    stroke(0)
    line(115, 497, 125, 547)
    line(705, 497, 690, 547)
    fill(250, 250, 250)
    noStroke()
    fill(170, 170, 170)
    arc(200, 312, 100, 70, -PI, 0, OPEN)
    ellipse(200, 312, 100, 20)
    for y in range(3):
        for i in range(-4, 5):
            if y == 0:
                ellipse(i * 10 + 200, 304 + (abs(i) ** 1.5) + y * 10, 5, 5)
            elif y == 1:
                ellipse(i * 10 + 200, 304 - (abs(i) ** 1.5) + y * 20, 5, 5)
            else:
                ellipse(i * 10 + 200, 315, 5, 5)
    fill(43, 149, 201, 100)
    rect(390, 558, 70, 30)
    line(394, 581, 456, 581)
    noStroke()
def draw_water(water_height):
    fill(0, 0, 255)
    noStroke()
    rect(107, 500, 715 - 107, 50, 6, 6, 50, 50)
    pushMatrix()
    translate(0, water_height)
    fill(0, 0, 255)
    rect(105, 505, 610, 35, 6, 6, 50, 50)
    stroke(33, 139, 300)
    stroke(0)
    for x in range(59):
        for y in range(4):
            ellipse(120 + x * 10, 502 + (y * 10), 20, 20)
            triangle(120 + (x * 10), 502 + (y * 10), 118 + (x * 10), 495 + (y * 10), 125 + (x * 10), 513 + (y * 10))
    popMatrix()
def draw_clouds(x, y, diameter, widths=5, lengths=2, transparency=100):
    if diameter < 60:
        fill(250, 250, 250, transparency)
    else:
        fill(250, 250, 250, 150)
    noStroke()
    for m in range(widths):
        for n in range(lengths):
            ellipse(x + 25 * m, y + 25 * n, diameter, diameter)
    noStroke()
def draw_pause_button():
    fill(255)
    rect(5, 5, 5, 15)
    rect(15, 5, 5, 15)
    textSize(20)
    fill(0)
    text("PAUSE", 25, 20)
def draw_sun(theme):
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
    else:
        pass
def set_gradient(x, y, w, h, c1, c2, axis):
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
    def __init__(self, rect_digits, rect_fill, text_fill, text_size, texts, selected, default):
        self.selected = False
        self.x = rect_digits[0]
        self.y = rect_digits[1]
        self.widths = rect_digits[2]
        self.heights = rect_digits[3]
        self.rect_fill = rect_fill
        self.rect_stroke = default
        self.text_box = texts
        self.text_size = text_size
        self.text_fill = text_fill
        self.selected_stroke = selected
        self.default_stroke = default
    def draw_box(self):
        if len(self.rect_fill) == 3:
            transparency = 200
        else:
            transparency = self.rect_fill[3]
        fill(self.rect_fill[0], self.rect_fill[1], self.rect_fill[2], transparency)
        if self.selected:
            self.rect_stroke = self.selected_stroke
        else:
            self.rect_stroke = self.default_stroke
        stroke(self.rect_stroke)
        rect(self.x, self.y, self.widths, self.heights)
        fill(self.text_fill)
        textSize(self.text_size)
        text(self.text_box, self.x + 5, self.y + 25)
def setup():
    size(800, 600)
    draw_tub()
    draw_water(20)
    draw_clouds(200, 100, 80)
    draw_pause_button()
    draw_sun("NOON")
    set_gradient(100, 200, 300, 200, color(255), color(0), "Y_AXIS")
    text_box = TextBox((100, 100, 200, 50), (255, 255, 255), (0, 0, 0), 20, "Hello", False, 0)
    text_box.draw_box()
def draw():
    pass