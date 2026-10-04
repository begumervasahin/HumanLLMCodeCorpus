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
            for elem in b9:
                b8 += str(elem.b5) + " "
                if elem.b6:
                    b10.append(elem.b6)
                if elem.b7:
                    b10.append(elem.b7)
            b8 += "\n"
            b9 = b10
        return b8
    def fonk5(self):
        return self.b5 != " "
    def fonk6(self):
        b9 = [self]
        b8 = []
        while b9:
            b8.append(" ".join([str(b4.b5) for b4 in b9]))
            if any(b4 for b4 in b9):
                b11 = []
                for b4 in b9:
                    if b4.b5 != " ":
                        for subnode in (b4.b6, b4.b7):
                            b11.append(subnode if subnode else class2())
                    else:
                        b11.append(b4)
                b9 = b11
            else:
                break
        return "\n" + "\n".join(b8)
b12 = [
    [10, 6, 0, 0, 0, 0, 0, 0, 0],
    [6, 10, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 10, 5, 3, 3, 1, 1, 0],
    [0, 0, 5, 10, 1, 2, 1, 1, 0],
    [0, 0, 3, 1, 10, 4, 1, 2, 0],
    [0, 0, 3, 2, 4, 10, 1, 4, 0],
    [0, 0, 1, 1, 1, 1, 10, 1, 0],
    [0, 0, 1, 1, 2, 4, 1, 10, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 10],
]
print("Representation Matrix:")
for row in b12:
    print(row)
print()
b13 = b12
for i in range(len(b12)):
    b13[i][i] = -1
b14 = []
for i in range(len(b12)):
    b15 = max(b13[i])
    b3 = b13[i].b3(b15)
    b16 = class1([i], b15, b3, class2([i]))
    b14.append(b16)
for _ in range(len(b12) - 1):
    b15 = -1
    b17 = [-1, -1]
    for j, group in enumerate(b14):
        if group.b2 > b15:
            b15 = group.b2
            b17 = [j, group.b3]
    print(f"Found max: {b15} @{b17}")
    b18 = b17[0]
    b19 = next(j for j, group in enumerate(b14) if b17[1] in group.b1)
    b20 = b14[b18]
    b21 = b14[b19]
    for element in b21.b1:
        for dest_element in b20.b1:
            b13[element][dest_element] = -1
            b13[dest_element][element] = -1
    print(f"Merging b14: {b20.b1} & {b21.b1}")
    b20.b1 += b21.b1
    b20.b4 = class2(b20.b1, b20.b4, b21.b4)
    b14.remove(b21)
    for group in b14:
        if group.b3 in b21.b1:
            group.b3 = b18
    b15 = -1
    a1 = -1
    for element in b20.b1:
        for i in range(len(b13)):
            if b13[element][i] > b15:
                b15 = b13[element][i]
                a1 = i
    b20.b3 = a1
    b20.b2 = b15
print("\nFinal Hierarchical Grouping:")
print(b14[0].b4)