class class1:
    def fonk1(self, corner1, corner2):
        self.b1 = [corner1[0], corner2[0]]
        self.b2 = [corner1[1], corner2[1]]
        self.b3 = {}
    def fonk2(self, qcanvas):
        print('Trying to unshow', qcanvas._name, b4 = ' ')
        if qcanvas._name in self.b3:
            print('OK')
            qcanvas.delete(self.b3[qcanvas._name])
            del self.b3[qcanvas._name]
        else:
            print('no')
    def fonk3(self, qcanvas, b5 = 1.0, b6=4, color='red', offset=(0, 0)):
        self.fonk5()
        self.b3[qcanvas._name] = qcanvas.create_rectangle(self.fonk4(b5, offset), b6 = b6, outline=color)
    def fonk4(self, b7 = 1.0, offset=(0, 0)):
        b8 = (self.b1[0], self.b2[0], self.b1[1], self.b2[1])
        b9 = tuple(int((x - dx) * b7) for x, dx in zip(b8, offset * 2))
        return b9
    def fonk5(self):
        self.b1 = [min(self.b1), max(self.b1)]
        self.b2 = [min(self.b2), max(self.b2)]
    def fonk6(self):
        return '! (%i,%i)-(%i,%i) !' % self.fonk4()
    def fonk7(self, cx, cy, tol):
        min_x, b10 = min(self.b1), max(self.b1)
        min_y, b11 = min(self.b2), max(self.b2)
        if b10 >= cx + tol >= min_x and b11 >= cy >= min_y:
            if any(abs(cy - some_y) <= tol for some_y in (min_y, b11)):
                return True
        if b11 >= cy + tol >= min_y and b10 >= cx >= min_x:
            if any(abs(cx - some_x) <= tol for some_x in (min_x, b10)):
                return True
        return False
    def fonk8(self, cx, cy, tol):
        for cox, coy in [(a, b) for a in [0, 1] for b in [0, 1]]:
            if abs(cx - self.b1[cox]) <= tol and abs(cy - self.b2[coy]) <= tol:
                return (cox, coy)
        return None