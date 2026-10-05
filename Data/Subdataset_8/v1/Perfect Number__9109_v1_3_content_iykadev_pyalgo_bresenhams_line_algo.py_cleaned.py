class Bitmap:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.bitmap = [[' ' for _ in range(width)] for _ in range(height)]
    def set(self, x, y):
        if 0 <= x < self.width and 0 <= y < self.height:
            self.bitmap[y][x] = '*'
    def chardisplay(self):
        for row in self.bitmap:
            print(' '.join(row))
    def line(self, x0, y0, x1, y1):
        "Bresenham's line algorithm"
        dx = abs(x1 - x0)
        dy = abs(y1 - y0)
        x, y = x0, y0
        sx = -1 if x0 > x1 else 1
        sy = -1 if y0 > y1 else 1
        if dx > dy:
            err = dx / 2.0
            while x != x1:
                self.set(x, y)
                err -= dy
                if err < 0:
                    y += sy
                    err += dx
                x += sx
        else:
            err = dy / 2.0
            while y != y1:
                self.set(x, y)
                err -= dx
                if err < 0:
                    x += sx
                    err += dy
                y += sy
        self.set(x, y)
bitmap = Bitmap(17, 17)
for points in ((1, 8, 8, 16), (8, 16, 16, 8), (16, 8, 8, 1), (8, 1, 1, 8)):
    bitmap.line(*points)
bitmap.chardisplay()