import random
from tkinter import *
import time
class class1(Frame):
    def fonk1(self):
        super().fonk1()
        self.pack()
        self.a1 = 600
        self.b1 = Canvas(self, width=self.a1, height=self.a1, bg="black")
        self.b1.grid()
        self.b2 = random.uniform(-1, 1)
        self.b3 = random.uniform(-1, 1)
        self.b4 = self.fonk2()
        self.fonk4()
        self.b5 = self.b2
        self.b6 = self.b3
        self.fonk6()
    def fonk2(self):
        def fonk3(x):
            return 0.5 * x + 250
        return [(i, fonk3(i) + random.randint(-10, 10)) for i in range(self.a1)]
    def fonk4(self):
        for x, y in self.b4:
            self.b1.create_line(x, self.a1 - y, x + 1, self.a1 - y + 1, b7 = "green")
    def fonk5(self, slope, intercept, b8 = "red"):
        return self.b1.create_line(
            0, self.a1 - intercept,
            self.a1, self.a1 - (slope * self.a1 + intercept),
            b7 = b8
        )
    def fonk6(self):
        a2 = 120
        a3 = 0.001
        for _ in range(a2):
            self.b6 += (self.b4[0][1] - self.b6) * 0.05
            for x, y in self.b4:
                b9 = self.b5 * x + self.b6
                b10 = y - b9
                self.b5 += (1 / len(self.b4)) * x * b10 * a3
            b11 = self.fonk5(self.b5, self.b6)
            self.fonk7(b11)
        b12 = self.fonk5(self.b5, self.b6)
        print(self.b5, self.b6)
    def fonk7(self, line_id):
        self.b1.update()
        time.sleep(0.1)
        self.b1.after(10, self.b1.delete, line_id)
if b13 = = "__main__":
    b14 = class1()
    b14.mainloop()