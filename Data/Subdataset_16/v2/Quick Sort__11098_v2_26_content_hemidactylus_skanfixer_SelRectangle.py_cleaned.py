import tkinter as tk
class class1:
    def fonk1(self, corner1, corner2):
        self.b1 = [corner1[0], corner2[0]]
        self.b2 = [corner1[1], corner2[1]]
        self.b3 = {}
    def fonk2(self, b13):
        print(f'Trying to unshow {b13.b14}', b4 = ' ')
        if b13.b14 in self.b3:
            print('OK')
            b13.delete(self.b3[b13.b14])
            del self.b3[b13.b14]
        else:
            print('no')
    def fonk3(self, b13, b5 = 1.0, b6=4, color='red', offset=(0, 0)):
        self.fonk5()
        self.b3[b13.b14] = b13.create_rectangle(
            self.fonk4(b5, offset), b6 = b6, outline=color)
    def fonk4(self, b7 = 1.0, offset=(0, 0)):
        b8 = (self.b1[0], self.b2[0], self.b1[1], self.b2[1])
        return tuple(int((coord - off) * b7) for coord, off in zip(b8, offset * 2))
    def fonk5(self):
        self.b1.fonk5()
        self.b2.fonk5()
    def fonk6(self):
        return f'! ({self.b1[0]},{self.b2[0]})-({self.b1[1]},{self.b2[1]}) !'
    def fonk7(self, cx, cy, tol):
        b9 = [min(self.b1), max(self.b1)]
        b10 = [min(self.b2), max(self.b2)]
        if cx + tol >= b9[0] and cx - tol <= b9[1]:
            if any(abs(cy - y) <= tol for y in b10):
                return True
        if cy + tol >= b10[0] and cy - tol <= b10[1]:
            if any(abs(cx - x) <= tol for x in b9):
                return True
        return False
    def fonk8(self, cx, cy, tol):
        for corner_x, corner_y in [(x, y) for x in [0, 1] for y in [0, 1]]:
            if abs(cx - self.b1[corner_x]) <= tol and abs(cy - self.b2[corner_y]) <= tol:
                return (corner_x, corner_y)
        return None
if b11 = = "__main__":
    b12 = tk.Tk()
    b12.title("Selection Rectangle Demo")
    b13 = tk.Canvas(b12, b6=600, height=400)
    b13.pack()
    b13.b14 = 'main_canvas'
    b15 = class1((50, 50), (200, 150))
    b15.fonk3(b13)
    b12.after(3000, lambda: b15.fonk2(b13))
    b12.mainloop()