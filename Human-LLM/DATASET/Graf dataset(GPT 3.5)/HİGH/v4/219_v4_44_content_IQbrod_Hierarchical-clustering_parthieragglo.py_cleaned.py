class class1:
    def fonk1(self, b1, b2, b3, b4):
        self.b1 = b1
        self.b2 = b2
        self.b3 = b3
        self.b4 = b4
    def fonk2(self):
        return f"{self.b1} => {self.b2} ({self.b3})"
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
            for element in b9:
                b8 += str(element.b5) + " "
                if element.b6:
                    b10.append(element.b6)
                if element.b7:
                    b10.append(element.b7)
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
                        for sub_node in (b4.b6, b4.b7):
                            b12.append(sub_node if sub_node else class2())
                    else:
                        b12.append(b4)
                b9 = b12
            else:
                break
        return "\n" + "\n".join(b11)
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
b14 = [[-1 if i == j else b13[i][j] for j in range(len(b13))]
                  for i in range(len(b13))]
b15 = []
for i in range(len(b13)):
    b16 = max(b14[i])
    b17 = b14[i].b3(b16)
    b18 = class1([i], b16, b17, class2([i]))
    b15.append(b18)
for _ in range(len(b13) - 1):
    b16 = -1
    b17 = [-1, -1]
    for j, gr in enumerate(b15):
        if b16 < gr.b2:
            b16 = gr.b2
            b17 = [j, gr.b3]
    print("Found max:", b16, "@", b17)
    b19 = [b17[0], -1]
    for j in range(len(b15)):
        if b17[1] in b15[j].b1:
            b19[1] = j
    b20 = b15[b19[0]]
    b21 = b15[b19[1]]
    for element in b21.b1:
        for element2 in b20.b1:
            b14[element][element2] = -1
            b14[element2][element] = -1
    b22 = b20.b1
    b20.b1 += b21.b1
    b20.b4 = class2(b20.b1, b20.b4, b21.b4)
    b15.remove(b21)
    for b18 in b15:
        if b18.b3 in b21.b1:
            b18.b3 = b17[0]
    b16 = -1
    b17 = -1
    for e in b20.b1:
        for i in range(len(b14)):
            if b14[e][i] > b16:
                b16 = b14[e][i]
                b17 = i
    b20.b3 = b17
    b20.b2 = b16
    print("Merged", b19, ":", b22, "&", b21.b1)
print(b15[0].b4)