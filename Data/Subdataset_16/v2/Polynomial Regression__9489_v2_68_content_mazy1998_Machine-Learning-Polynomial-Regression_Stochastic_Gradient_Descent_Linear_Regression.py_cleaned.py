import random
from tkinter import *
import time
class class1(Frame):
    def fonk1(self):
        Frame.fonk1(self)
        self.pack()
        a1 = 600
        self.b1 = Canvas(self, width=a1, height=a1, bg="black")
        self.b1.grid()
        b2 = random.uniform(-1, 1)
        b3 = random.uniform(-1, 1)
        def fonk2(x):
            return 0.5 * x + 250
        b4 = [(i, fonk2(i) + random.randint(-10, 10)) for i in range(a1)]
        for x, y in b4:
            self.b1.create_line(x, a1 - y, x + 1, a1 - y + 1, b5 = "green")
        b6 = len(b4)
        def fonk3():
            b7 = self.b1.create_line(
                0, a1 - b11,
                a1, a1 - (b10 * a1 + b11),
                b5 = "red"
            )
            self.b1.fonk3()
            time.sleep(0.1)
            self.b1.after(10, self.b1.delete, b7)
        for _ in range(120):
            b2 += (b4[0][1] - b2) * 0.05
            for x, y in b4:
                b8 = b3 * x + b2
                b9 = y - b8
                b3 += (1 / b6) * x * b9 * 0.001
            b10 = b3
            b11 = b2
            fonk3()
        self.b1.create_line(
            0, a1 - b11,
            a1, a1 - (b10 * a1 + b11),
            b5 = "red"
        )
        print(b10, b11)
b12 = class1()
b12.mainloop()