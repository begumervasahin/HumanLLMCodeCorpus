import random
import math
from tkinter import *
a1 = 25
a2 = 400
b1 = a2 / a1
b2 = {}
b3 = {}
b4 = []
for i in range(a1*a1):
    b3[i] = False
    if i - a1 >= 0:
        b2[i - a1, i] = 1
    if i + a1 < a1*a1:
        b2[i, i + a1] = 1
    if not (i + 1) % a1 = = 0:
        b2[i, i + 1] = 1
    if not i % a1 = = 0:
        b2[i - 1, i] = 1
a3 = 0
b3[0] = True
b4 += [[0, x] for x in range(a1*a1) if (0, x) in b2.keys()]
while len(b4) > 0:
    random.shuffle(b4)
    b5 = b4.pop()
    if b3[b5[0]] and not b3[b5[1]]:
        b2.pop((b5[0], b5[1]), None)
        b2.pop((b5[1], b5[0]), None)
        b3[b5[1]] = True
        b4 += [[b5[1], x] for x in range(a1*a1) if (b5[1], x) in b2.keys() or (x, b5[1]) in b2.keys()]
    if b3[b5[1]] and not b3[b5[0]]:
        b2.pop((b5[0], b5[1]), None)
        b2.pop((b5[1], b5[0]), None)
        b3[b5[0]] = True
        b4 += [[b5[0], x] for x in range(a1*a1) if (b5[0], x) in b2.keys() or (x, b5[0]) in b2.keys()]
b6 = Tk()
b7 = Canvas(b6, width=a2, height=a2)
b7.pack()
b7.create_rectangle(0, 0, a2, a2, b8 = "black")
b7.create_rectangle(3, 3, a2-3, a2-3, b8 = "white")
for b5 in b2:
    b9 = min(b5)
    b10 = max(b5)
    b11 = b9 % a1
    b12 = b10 % a1
    b13 = math.floor(min(b9 / a1, b10 / a1))
    b14 = math.floor(max(b10 / a1, b9 / a1))
    if b11 = = b12:
        b15 = b11 * b1
        b16 = b11 * b1 + b1
        b17 = b13 * b1 + b1 - 1
        b18 = b13 * b1 + b1 + 1
        b7.create_rectangle(b15, b17, b16, b18, b8 = "black")
    if b13 = = b14:
        b17 = b13 * b1
        b18 = b13 * b1 + b1
        b15 = b11 * b1 + b1 - 1
        b16 = b11 * b1 + b1 + 1
        b7.create_rectangle(b15, b17, b16, b18, b8 = "black")
b7.create_rectangle(0, 4, 3, b1 + 3, b8 = "yellow", outline="white")
b7.create_rectangle(a2 - 4, a2 - b1, a2, a2 - 4, b8 = "green", outline="white")
mainloop()