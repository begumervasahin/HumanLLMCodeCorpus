class SelectionRectangle:
    def __init__(self, corner1, corner2):
        self.x_coords = [corner1[0], corner2[0]]
        self.y_coords = [corner1[1], corner2[1]]
        self.rectangle_ids = {}
    def hide(self, canvas):
        print(f'Trying to hide {canvas._name}')
        if canvas._name in self.rectangle_ids:
            print('Success')
            canvas.delete(self.rectangle_ids[canvas._name])
            del self.rectangle_ids[canvas._name]
        else:
            print('Not found')
    def show(self, canvas, scale=1.0, width=4, color='red', offset=(0, 0)):
        self.sort_coordinates()
        rectangle_tuple = self.as_tuple(scale, offset)
        self.rectangle_ids[canvas._name] = canvas.create_rectangle(
            rectangle_tuple, width=width, outline=color
        )
    def as_tuple(self, scale=1.0, offset=(0, 0)):
        coords = (self.x_coords[0], self.y_coords[0], self.x_coords[1], self.y_coords[1])
        result = tuple(int((coord - offset_val) * scale) for coord, offset_val in zip(coords, offset * 2))
        return result
    def sort_coordinates(self):
        self.x_coords = [min(self.x_coords), max(self.x_coords)]
        self.y_coords = [min(self.y_coords), max(self.y_coords)]
    def __str__(self):
        return '! ({},{})-({},{}) !'.format(*self.as_tuple())
    def is_on_edge(self, x, y, tolerance):
        x_min, x_max = min(self.x_coords), max(self.x_coords)
        y_min, y_max = min(self.y_coords), max(self.y_coords)
        if x_min - tolerance <= x <= x_max + tolerance:
            if y_min - tolerance <= y <= y_max + tolerance:
                return True
        return False
    def is_on_corner(self, x, y, tolerance):
        for corner_x, corner_y in [(0, 0), (0, 1), (1, 0), (1, 1)]:
            if abs(x - self.x_coords[corner_x]) <= tolerance and abs(y - self.y_coords[corner_y]) <= tolerance:
                return (corner_x, corner_y)
        return None