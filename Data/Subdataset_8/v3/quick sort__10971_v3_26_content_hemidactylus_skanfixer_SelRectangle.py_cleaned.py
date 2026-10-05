class SelectableRectangle:
    def __init__(self, corner1, corner2):
        self.x_coords = [corner1[0], corner2[0]]
        self.y_coords = [corner1[1], corner2[1]]
        self.rectangle_ids = {}
    def unshow(self, canvas):
        if canvas._name in self.rectangle_ids:
            canvas.delete(self.rectangle_ids[canvas._name])
            del self.rectangle_ids[canvas._name]
    def show(self, canvas, factor=1.0, width=4, color='red', offset=(0, 0)):
        self.sort_coordinates()
        self.rectangle_ids[canvas._name] = canvas.create_rectangle(self.as_tuple(factor, offset), width=width, outline=color)
    def as_tuple(self, counter_factor=1.0, offset=(0, 0)):
        return tuple(int((x - dx) * counter_factor) for x, dx in zip((self.x_coords[0], self.y_coords[0], self.x_coords[1], self.y_coords[1]), offset * 2))
    def sort_coordinates(self):
        self.x_coords = [min(self.x_coords), max(self.x_coords)]
        self.y_coords = [min(self.y_coords), max(self.y_coords)]
    def __str__(self):
        return '! (%i,%i)-(%i,%i) !' % self.as_tuple()
    def has_on_edge(self, cx, cy, tolerance):
        min_x, max_x = [min(self.x_coords), max(self.x_coords)]
        min_y, max_y = [min(self.y_coords), max(self.y_coords)]
        if max_x >= cx + tolerance >= min_x and any(abs(cy - some_y) <= tolerance for some_y in [min_y, max_y]):
            return True
        if max_y >= cy + tolerance >= min_y and any(abs(cx - some_x) <= tolerance for some_x in [min_x, max_x]):
            return True
        return False
    def has_on_corner(self, cx, cy, tolerance):
        for cox, coy in [(a, b) for a in [0, 1] for b in [0, 1]]:
            if abs(cx - self.x_coords[cox]) <= tolerance and abs(cy - self.y_coords[coy]) <= tolerance:
                return (cox, coy)
        return None