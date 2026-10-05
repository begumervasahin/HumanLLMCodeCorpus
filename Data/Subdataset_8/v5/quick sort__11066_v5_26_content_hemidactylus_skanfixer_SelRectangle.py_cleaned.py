class SelRectangle:
    def __init__(self, corner1, corner2):
        self.xs = [corner1[0], corner2[0]]
        self.ys = [corner1[1], corner2[1]]
        self.rectaID = {}
    def unshow(self, qcanvas):
        print('Trying to unshow', qcanvas._name, end=' ')
        if qcanvas._name in self.rectaID:
            print('OK')
            qcanvas.delete(self.rectaID[qcanvas._name])
            del self.rectaID[qcanvas._name]
        else:
            print('no')
    def show(self, qcanvas, factor=1.0, width=4, color='red', offset=(0, 0)):
        self.sort()
        self.rectaID[qcanvas._name] = qcanvas.create_rectangle(self.as_tuple(factor, offset), width=width, outline=color)
    def as_tuple(self, counter_factor=1.0, offset=(0, 0)):
        returnee = (self.xs[0], self.ys[0], self.xs[1], self.ys[1])
        result = tuple(int((x - dx) * counter_factor) for x, dx in zip(returnee, offset * 2))
        return result
    def sort(self):
        self.xs = [min(self.xs), max(self.xs)]
        self.ys = [min(self.ys), max(self.ys)]
    def __str__(self):
        return '! (%i,%i)-(%i,%i) !' % self.as_tuple()
    def has_on_edge(self, cx, cy, tol):
        min_x, max_x = min(self.xs), max(self.xs)
        min_y, max_y = min(self.ys), max(self.ys)
        if max_x >= cx + tol >= min_x and max_y >= cy >= min_y:
            if any(abs(cy - some_y) <= tol for some_y in (min_y, max_y)):
                return True
        if max_y >= cy + tol >= min_y and max_x >= cx >= min_x:
            if any(abs(cx - some_x) <= tol for some_x in (min_x, max_x)):
                return True
        return False
    def has_on_corner(self, cx, cy, tol):
        for cox, coy in [(a, b) for a in [0, 1] for b in [0, 1]]:
            if abs(cx - self.xs[cox]) <= tol and abs(cy - self.ys[coy]) <= tol:
                return (cox, coy)
        return None