import tkinter as tk
class class1:
    def fonk1(self, corner1, corner2):
        self.b1 = [corner1[0], corner2[0]]
        self.b2 = [corner1[1], corner2[1]]
        self.b3 = {}
    def fonk2(self, b11):
        if b11.b12 in self.b3:
            b11.delete(self.b3[b11.b12])
            del self.b3[b11.b12]
    def fonk3(self, b11, b4 = 1.0, b5=4, color='red', offset=(0, 0)):
        self.fonk5()
        self.b3[b11.b12] = b11.create_rectangle(
            self.fonk4(b4, offset), b5 = b5, outline=color)
    def fonk4(self, b6 = 1.0, offset=(0, 0)):
        b7 = (self.b1[0], self.b2[0], self.b1[1], self.b2[1])
        return tuple(int((coord - off) * b6) for coord, off in zip(b7, offset * 2))
    def fonk5(self):
        self.b1.fonk5()
        self.b2.fonk5()
    def fonk6(self):
        return f'! ({self.b1[0]},{self.b2[0]})-({self.b1[1]},{self.b2[1]}) !'
    def fonk7(self, cx, cy, tol):
        b8 = [min(self.b1), max(self.b1)]
        b9 = [min(self.b2), max(self.b2)]
        if cx + tol >= b8[0] and cx - tol <= b8[1]:
            if any(abs(cy - y) <= tol for y in b9):
                return True
        if cy + tol >= b9[0] and cy - tol <= b9[1]:
            if any(abs(cx - x) <= tol for x in b8):
                return True
        return False
    def fonk8(self, cx, cy, tol):
        for corner_x, corner_y in [(x, y) for x in [0, 1] for y in [0, 1]]:
            if abs(cx - self.b1[corner_x]) <= tol and abs(cy - self.b2[corner_y]) <= tol:
                return (corner_x, corner_y)
        return None
def fonk9():
    b10 = tk.Tk()
    b10.title("Selection Rectangle Demo")
    b11 = tk.Canvas(b10, b5=600, height=400)
    b11.pack()
    b11.b12 = 'main_canvas'
    b13 = class1((50, 50), (200, 150))
    b13.fonk3(b11)
    b10.after(3000, lambda: b13.fonk2(b11))
    b10.mainloop()
if b14 = = "__main__":
    fonk9()