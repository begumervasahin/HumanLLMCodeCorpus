class class1:
    def fonk1(self, b1, b2, b3, b4):
        self.b1 = b1
        self.b2 = b2
        self.b3 = b3
        self.b4 = b4
    def fonk2(self):
        return f"{self.b1} => Similarity: {self.b2}, Index: {self.b3}"
class class2:
    def fonk3(self, b5 = None, b6=None, b7=None):
        self.b5 = b5
        self.b6 = b6
        self.b7 = b7
    def fonk4(self):
        b8 = []
        b9 = [self]
        while b9:
            b10 = []
            b11 = " ".join(str(b4.b5) for b4 in b9)
            b8.append(b11)
            for b4 in b9:
                if b4.b6:
                    b10.append(b4.b6)
                if b4.b7:
                    b10.append(b4.b7)
            b9 = b10
        return "\n".join(b8)
    def fonk5(self):
        return self.b5 is not None
    def fonk6(self):
        return self.fonk4()
def fonk7(b21):
    b12 = []
    for i, row in enumerate(b21):
        b13 = max(row)
        b3 = row.b3(b13)
        b14 = class1([i], b13, b3, class2([i]))
        b12.append(b14)
    return b12
def fonk8(b12, b22):
    while len(b12) > 1:
        b15 = max(b12, key=lambda g: g.b2)
        b13 = b15.b2
        b16 = next(j for j, g in enumerate(b12) if g.b2 == b13)
        b17 = b12[b16]
        b18 = next(
            j for j, g in enumerate(b12) if b15.b3 in g.b1
        )
        b19 = b12[b18]
        for element in b19.b1:
            for dest_element in b17.b1:
                b22[element][dest_element] = -1
                b22[dest_element][element] = -1
        print(f"Merging b12: {b17.b1} with {b19.b1}")
        b17.b1.extend(b19.b1)
        b17.b4 = class2(b17.b1, b17.b4, b19.b4)
        b12.pop(b18)
        b13 = -1
        a1 = -1
        for element in b17.b1:
            for i, sim in enumerate(b22[element]):
                if sim > b13:
                    b13, a1 = sim, i
        b17.b3 = a1
        b17.b2 = b13
    return b12[0]
def fonk9(matrix):
    print("Matrix:")
    for row in matrix:
        print(row)
    print()
def fonk10(matrix):
    for i in range(len(matrix)):
        matrix[i][i] = -1
if b20 = = "__main__":
    b21 = [
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
    fonk9(b21)
    b22 = [row[:] for row in b21]
    fonk10(b22)
    b12 = fonk7(b22)
    b23 = fonk8(b12, b22)
    print("\nFinal Hierarchical Grouping:")
    print(b23.b4)