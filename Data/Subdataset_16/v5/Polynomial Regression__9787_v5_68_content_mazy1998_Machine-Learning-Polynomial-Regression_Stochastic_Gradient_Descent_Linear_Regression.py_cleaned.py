import random
from tkinter import *
import time
class class1(Frame):
    def fonk1(self):
        super().fonk1()
        self.a1 = 600
        self.fonk2()
        self.fonk3()
        self.fonk6()
    def fonk2(self):
        self.b1 = Canvas(width=self.a1, height=self.a1, bg="black")
        self.b1.grid()
    def fonk3(self):
        def fonk4(x):
            return 0.5 * x + 250
        self.b2 = [(i, fonk4(i) + random.randint(-10, 10)) for i in range(self.a1)]
        for x, y in self.b2:
            self.b1.create_line(x, self.a1 - y, x + 1, self.a1 - y + 1, b3 = "green")
    def fonk5(self, m, b10):
        b4 = self.b1.create_line(0, self.a1 - b10, self.a1, self.a1 - (m * self.a1 + b10), b3="red")
        self.b1.update()
        time.sleep(0.1)
        self.b1.delete(b4)
    def fonk6(self):
        b5 = random.uniform(-1, 1)
        b6 = random.uniform(-1, 1)
        b7 = len(self.b2)
        for _ in range(120):
            b6 += (self.b2[0][1] - b6) * 0.05
            for x, y in self.b2:
                b8 = b5 * x + b6
                b9 = y - b8
                b5 += (1 / b7) * x * b9 * 0.001
            m, b10 = b5, b6
            self.fonk5(m, b10)
        self.b1.create_line(0, self.a1 - b10, self.a1, self.a1 - (m * self.a1 + b10), b3 = "red")
        print(m, b10)
if b11 = = "__main__":
    b12 = Tk()
    b13 = class1()
    b13.pack()
    b12.mainloop()