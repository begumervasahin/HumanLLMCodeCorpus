class class1:
    def fonk1(self, col, b2, b3, b4):
        self.b1 = col
        self.b2 = b2
        self.b3 = b3
        self.b4 = b4
    def fonk2(self):
        return str(self.b1) + " => " + str(self.b2) + " (" + str(self.b3) + ")"
class class2:
    def fonk3(self, b5 = " ", b6=None, b7=None):
        self.b5 = b5
        self.b6 = b6
        self.b7 = b7
    def fonk4(self):
        b8 = "\n"
        b9 = [self]
        while b9:
            b10 = []
            for b1 in b9:
                b8 += str(b1.b5) + " "
                if b1.b6:
                    b10.append(b1.b6)
                if b1.b7:
                    b10.append(b1.b7)
            b8 += "\n"
            b9 = b10
        return b8
    def fonk5(self):
        return self.b5 != " "
    def fonk6(self):
        b9 = [self]
        b11 = []
        while b9:
            b11.append(" ".join([str(b4.b5) for b4 in b9]))
            if any(b4 for b4 in b9):
                b12 = []
                for b4 in b9:
                    if b4.b5 != " ":
                        for subnode in (b4.b6, b4.b7):
                            b12.append(subnode if subnode else class2())
                    else:
                        b12.append(b4)
                b9 = b12
            else:
                break
        return ("\n" + "\n".join(b11))
b13 = [
    [10, 6, 0, 0, 0, 0, 0, 0, 0],
    [6, 10, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 10, 5, 3, 3, 1, 1, 0],
    [0, 0, 5, 10, 1, 2, 1, 1, 0],
    [0, 0, 3, 1, 10, 4, 1, 2, 0],
    [0, 0, 3, 2, 4, 10, 1, 4, 0],
    [0, 0, 1, 1, 1, 1, 10, 1, 0],
    [0, 0, 1, 1, 2, 4, 1, 10, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 10]
]
print("Representation Matrix:")
for row in b13:
    print(row)
print()
b14 = [[-1 if i == j else b13[i][j] for j in range(len(b13))] for i in range(len(b13))]
b15 = []
for i in range(len(b13)):
    b16 = class1([i], max(b14[i]), b14[i].b17(max(b14[i])), class2([i]))
    b15.append(b16)
for _ in range(len(b13) - 1):
    a1 = -1
    b17 = [-1, -1]
    for j, gr in enumerate(b15):
        if a1 < gr.b2:
            a1 = gr.b2
            b17 = [j, gr.b3]
    print("Found max:", a1, "@", b17)
    b18 = [b17[0], -1]
    for j in range(len(b15)):
        if b17[1] in b15[j].b1:
            b18[1] = j
    b19 = b15[b18[0]]
    b20 = b15[b18[1]]
    for el in b20.b1:
        for el2 in b19.b1:
            b14[el][el2] = -1
            b14[el2][el] = -1
    b21 = b19.b1
    b19.b1 += b20.b1
    b19.b4 = class2(b19.b1, b19.b4, b20.b4)
    b15.remove(b20)
    for b16 in b15:
        if b16.b3 in b20.b1:
            b16.b3 = b17[0]
    a1 = -1
    a2 = -1
    for e in b19.b1:
        for i in range(len(b14)):
            if b14[e][i] > a1:
                a1 = b14[e][i]
                a2 = i
    b19.b3 = a2
    b19.b2 = a1
    print("Merged", b18, ":", b21, "&", b20.b1)
print(b15[0].b4)