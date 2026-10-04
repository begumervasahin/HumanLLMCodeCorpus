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
        b2 = random.randint(-100, 100) / 100
        b3 = random.randint(-100, 100) / 100
        def fonk2(b8):
            return 0.5 * b8 + 250
        b4 = [(i, fonk2(i) + random.randint(-10, 10)) for i in range(0, a1)]
        for i in b4:
            self.b1.create_line(i[0], a1 - i[1], i[0] + 1, a1 - i[1] + 1, b5 = "green")
        b6 = len(b4)
        def fonk3():
            b7 = self.b1.create_line(0, a1 - b13, a1, a1 - (b12 * a1 + b13), b5="red")
            self.b1.fonk3()
            time.sleep(0.1)
            self.b1.after(10, self.b1.delete, b7)
        for z in range(120):
            b2 += (b4[0][1] - b2) * 0.05
            for i in range(len(b4)):
                b8 = b4[i][0]
                b9 = b4[i][1]
                b10 = b3 * b8 + b2
                b11 = b9 - b10
                b3 += (1 / b6) * b8 * b11 * 0.001
            b12 = b3
            b13 = b2
            fonk3()
        self.b1.create_line(0, a1 - b13, a1, a1 - (b12 * a1 + b13), b5 = "red")
        print(b12, b13)
b14 = class1()
b14.mainloop()