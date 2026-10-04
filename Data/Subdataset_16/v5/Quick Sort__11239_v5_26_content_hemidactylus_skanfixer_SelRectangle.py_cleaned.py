class class1:
    def fonk1(self, corner1, corner2):
        self.b1 = [corner1[0], corner2[0]]
        self.b2 = [corner1[1], corner2[1]]
        self.b3 = {}
    def fonk2(self, canvas):
        print(f'Trying to hide {canvas._name}')
        if canvas._name in self.b3:
            print('Success')
            canvas.delete(self.b3[canvas._name])
            del self.b3[canvas._name]
        else:
            print('Not found')
    def fonk3(self, canvas, b4 = 1.0, b6=4, color='red', offset=(0, 0)):
        self.fonk5()
        b5 = self.fonk4(b4, offset)
        self.b3[canvas._name] = canvas.create_rectangle(
            b5, b6 = b6, outline=color
        )
    def fonk4(self, b4 = 1.0, offset=(0, 0)):
        b7 = (self.b1[0], self.b2[0], self.b1[1], self.b2[1])
        b8 = tuple(int((coord - offset_val) * b4) for coord, offset_val in zip(b7, offset * 2))
        return b8
    def fonk5(self):
        self.b1.sort()
        self.b2.sort()
    def fonk6(self):
        return '! ({},{})-({},{}) !'.format(*self.fonk4())
    def fonk7(self, x, y, tolerance):
        x_min, b9 = min(self.b1), max(self.b1)
        y_min, b10 = min(self.b2), max(self.b2)
        if x_min - tolerance <= x <= b9 + tolerance and y_min - tolerance <= y <= b10 + tolerance:
            return True
        return False
    def fonk8(self, x, y, tolerance):
        for corner_x, corner_y in [(0, 0), (0, 1), (1, 0), (1, 1)]:
            if abs(x - self.b1[corner_x]) <= tolerance and abs(y - self.b2[corner_y]) <= tolerance:
                return (corner_x, corner_y)
        return None