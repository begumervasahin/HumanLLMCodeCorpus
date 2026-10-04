class Bitmap:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.pixels = [[' ' for _ in range(width)] for _ in range(height)]
    def set_pixel(self, x, y, color='
        if 0 <= x < self.width and 0 <= y < self.height:
            self.pixels[y][x] = color
    def draw_circle(self, x0, y0, radius, color='
        f = 1 - radius
        ddf_x = 1
        ddf_y = -2 * radius
        x = 0
        y = radius
        self.set_pixel(x0, y0 + radius, color)
        self.set_pixel(x0, y0 - radius, color)
        self.set_pixel(x0 + radius, y0, color)
        self.set_pixel(x0 - radius, y0, color)
        while x < y:
            if f >= 0:
                y -= 1
                ddf_y += 2
                f += ddf_y
            x += 1
            ddf_x += 2
            f += ddf_x
            self.set_pixel(x0 + x, y0 + y, color)
            self.set_pixel(x0 - x, y0 + y, color)
            self.set_pixel(x0 + x, y0 - y, color)
            self.set_pixel(x0 - x, y0 - y, color)
            self.set_pixel(x0 + y, y0 + x, color)
            self.set_pixel(x0 - y, y0 + x, color)
            self.set_pixel(x0 + y, y0 - x, color)
            self.set_pixel(x0 - y, y0 - x, color)
    def display(self):
        for row in self.pixels:
            print(''.join(row))
def main():
    bitmap = Bitmap(25, 25)
    bitmap.draw_circle(x0=12, y0=12, radius=12)
    bitmap.display()
if __name__ == "__main__":
    main()