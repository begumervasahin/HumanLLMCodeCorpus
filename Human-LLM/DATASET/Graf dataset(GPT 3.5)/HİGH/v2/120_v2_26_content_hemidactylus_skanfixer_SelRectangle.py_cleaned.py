class class1:
    def fonk1(self, corner1, corner2):
        self.b1 = [corner1[0], corner2[0]]
        self.b2 = [corner1[1], corner2[1]]
        self.b3 = {}
    def fonk2(self, canvas):
        if canvas._name in self.b3:
            canvas.delete(self.b3[canvas._name])
            del self.b3[canvas._name]
    def fonk3(self, canvas, b4 = 1.0, b5=4, color='red', offset=(0, 0)):
        self.fonk5()
        self.b3[canvas._name] = canvas.create_rectangle(self.fonk4(b4, offset), b5 = b5, outline=color)
    def fonk4(self, b6 = 1.0, offset=(0, 0)):
        return tuple(int((x - dx) * b6) for x, dx in zip((self.b1[0], self.b2[0], self.b1[1], self.b2[1]), offset * 2))
    def fonk5(self):
        self.b1 = [min(self.b1), max(self.b1)]
        self.b2 = [min(self.b2), max(self.b2)]
    def fonk6(self):
        return '! (%i,%i)-(%i,%i) !' % self.fonk4()
    def fonk7(self, cx, cy, tolerance):
        min_x, b7 = [min(self.b1), max(self.b1)]
        min_y, b8 = [min(self.b2), max(self.b2)]
        if b7 >= cx + tolerance >= min_x and any(abs(cy - some_y) <= tolerance for some_y in [min_y, b8]):
            return True
        if b8 >= cy + tolerance >= min_y and any(abs(cx - some_x) <= tolerance for some_x in [min_x, b7]):
            return True
        return False
    def fonk8(self, cx, cy, tolerance):
        for cox, coy in [(a, b) for a in [0, 1] for b in [0, 1]]:
            if abs(cx - self.b1[cox]) <= tolerance and abs(cy - self.b2[coy]) <= tolerance:
                return (cox, coy)
        return None