def draw_line(self, x0, y0, x1, y1):
    dx = abs(x1 - x0)
    dy = abs(y1 - y0)
    x, y = x0, y0
    sx = 1 if x0 < x1 else -1
    sy = 1 if y0 < y1 else -1
    if dx > dy:
        error = dx / 2.0
        while x != x1:
            self.set_pixel(x, y)
            error -= dy
            if error < 0:
                y += sy
                error += dx
            x += sx
    else:
        error = dy / 2.0
        while y != y1:
            self.set_pixel(x, y)
            error -= dx
            if error < 0:
                x += sx
                error += dy
            y += sy
    self.set_pixel(x, y)
Bitmap.draw_line = draw_line
bitmap = Bitmap(17, 17)
points_list = [(1, 8, 8, 16), (8, 16, 16, 8), (16, 8, 8, 1), (8, 1, 1, 8)]
for points in points_list:
    bitmap.draw_line(*points)
bitmap.display()