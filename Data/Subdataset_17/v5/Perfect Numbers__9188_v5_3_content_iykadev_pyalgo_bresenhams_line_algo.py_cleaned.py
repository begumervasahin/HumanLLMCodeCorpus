class Bitmap:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.pixels = [[' ' for _ in range(width)] for _ in range(height)]
    def set_pixel(self, x, y):
        Draw a line from (x0, y0) to (x1, y1) using Bresenham's line algorithm.Display the bitmap in the console.Create a bitmap and draw specified lines."""
    bitmap = Bitmap(17, 17)
    lines_to_draw = [(1, 8, 8, 16), (8, 16, 16, 8), (16, 8, 8, 1), (8, 1, 1, 8)]
    for points in lines_to_draw:
        bitmap.draw_line(*points)
    bitmap.display()
if __name__ == '__main__':
    main()