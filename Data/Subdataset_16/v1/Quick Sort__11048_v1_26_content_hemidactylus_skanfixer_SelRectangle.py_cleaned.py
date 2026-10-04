import tkinter as tk
class class1:
    def fonk1(self, corner1, corner2):
        self.b1 = [corner1[0], corner2[0]]
        self.b2 = [corner1[1], corner2[1]]
        self.b3 = {}
    def fonk2(self, qcanvas):
        print('TryingToUnshow', qcanvas.b15, b4 = ' ')
        if qcanvas.b15 in self.b3:
            print('OK')
            qcanvas.delete(self.b3[qcanvas.b15])
            del self.b3[qcanvas.b15]
        else:
            print('no')
    def fonk3(self, qcanvas, b5 = 1.0, b6=4, color='red', offset=(0, 0)):
        self.fonk5()
        self.b3[qcanvas.b15] = qcanvas.create_rectangle(
            self.fonk4(b5, offset), b6 = b6, outline=color)
    def fonk4(self, b7 = 1.0, offset=(0, 0)):
        b8 = (self.b1[0], self.b2[0], self.b1[1], self.b2[1])
        b9 = tuple(int((x - dx) * b7) for x, dx in zip(b8, offset * 2))
        return b9
    def fonk5(self):
        '''in-place shuffling of coordinates, ensures proper ordering'''
        self.b1 = [min(self.b1), max(self.b1)]
        self.b2 = [min(self.b2), max(self.b2)]
    def fonk6(self):
        return '! (%i,%i)-(%i,%i) !' % self.fonk4()
    def fonk7(self, cx, cy, tol):
        '''return True if the given point lies within TOL (max in either dir) from the rectangle's edge'''
        b10 = [min(self.b1), max(self.b1)]
        b11 = [min(self.b2), max(self.b2)]
        if cx + tol >= b10[0] and cx - tol <= b10[1]:
            if any(abs(cy - somey) <= tol for somey in b11):
                return True
        if cy + tol >= b11[0] and cy - tol <= b11[1]:
            if any(abs(cx - somex) <= tol for somex in b10):
                return True
        return False
    def fonk8(self, cx, cy, tol):
        '''return a 2uple marking the corner (0/1,0/1) if the rectangle has an edge close to the given point, or None,None if nothing matches'''
        for cox, coy in [(a, b) for a in [0, 1] for b in [0, 1]]:
            if abs(cx - self.b1[cox]) <= tol and abs(cy - self.b2[coy]) <= tol:
                return (cox, coy)
        return None
if b12 = = "__main__":
    b13 = tk.Tk()
    b13.title("Selection Rectangle Demo")
    b14 = tk.Canvas(b13, b6=600, height=400)
    b14.pack()
    b14.b15 = 'main_canvas'
    b16 = class1((50, 50), (200, 150))
    b16.fonk3(b14)
    b13.after(3000, lambda: b16.fonk2(b14))
    b13.mainloop()