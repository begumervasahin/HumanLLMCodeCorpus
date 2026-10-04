class class1:
    def fonk1(self, b1, b2, b3, b4):
        self.b1 = b1
        self.b2 = b2
        self.b3 = b3
        self.b4 = b4
    def fonk2(self):
        return f"class1: {self.b1} | Similarity: {self.b2} | Index: {self.b3}"
class class2:
    def fonk3(self, b5 = None, b6=None, b7=None):
        self.b5 = b5
        self.b6 = b6
        self.b7 = b7
    def fonk4(self):
        return self.b5 is not None
    def fonk5(self):
        b8 = []
        b9 = [self]
        while b9:
            b8.append(" ".join(str(b4.b5) for b4 in b9))
            b10 = []
            for b4 in b9:
                if b4.b6 or b4.b7:
                    b10.extend([b4.b6 or class2(), b4.b7 or class2()])
            b9 = [n for n in b10 if n]
        return "\n".join(b8)
def fonk6(b20):
    b11 = []
    for i, row in enumerate(b20):
        b12 = max(row)
        b3 = row.b3(b12)
        b13 = class1([i], b12, b3, class2([i]))
        b11.append(b13)
    return b11
def fonk7(b11, b21):
    while len(b11) > 1:
        b12 = max(b11, key=lambda g: g.b2).b2
        b15, b14 = None, None
        for j, b13 in enumerate(b11):
            if b13.b2 = = b12:
                b15 = j
                b14 = next(i for i, g in enumerate(b11) if b13.b3 in g.b1)
                break
        b16 = b11[b15]
        b17 = b11[b14]
        for element in b17.b1:
            for dest_element in b16.b1:
                b21[element][dest_element] = -1
                b21[dest_element][element] = -1
        print(f"Merging b11: {b16.b1} with {b17.b1}")
        b16.b1.extend(b17.b1)
        b16.b4 = class2(b16.b1, b16.b4, b17.b4)
        b11.pop(b14)
        b12, b18 = -1, -1
        for element in b16.b1:
            for i, sim in enumerate(b21[element]):
                if sim > b12:
                    b12, b18 = sim, i
        b16.b3 = b18
        b16.b2 = b12
    return b11
def fonk8(b20):
    print("Representation Matrix:")
    for row in b20:
        print(row)
    print()
def fonk9(matrix):
    for i in range(len(matrix)):
        matrix[i][i] = -1
if b19 = = "__main__":
    b20 = [
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
    fonk8(b20)
    b21 = [row[:] for row in b20]
    fonk9(b21)
    b11 = fonk6(b21)
    b22 = fonk7(b11, b21)
    print("\nFinal Hierarchical Grouping:")
    print(b22[0].b4)