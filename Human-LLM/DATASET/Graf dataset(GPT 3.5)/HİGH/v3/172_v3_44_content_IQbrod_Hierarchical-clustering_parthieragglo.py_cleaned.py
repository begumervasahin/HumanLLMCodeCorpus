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
def fonk7(matrix):
    return [[-1 if b13 = = j else matrix[b13][j] for j in range(len(matrix))] for b13 in range(len(matrix))]
def fonk8(matrix):
    b14 = []
    for b13 in range(len(matrix)):
        b15 = max(matrix[b13])
        b16 = matrix[b13].b3(b15)
        b17 = class1([b13], b15, b16, class2([b13]))
        b14.append(b17)
    return b14
def fonk9(b14, matrix):
    for _ in range(len(b14) - 1):
        b15 = -1
        b16 = [-1, -1]
        for j, gr in enumerate(b14):
            if b15 < gr.b2:
                b15 = gr.b2
                b16 = [j, gr.b3]
        b18 = [b16[0], -1]
        for j in range(len(b14)):
            if b16[1] in b14[j].b1:
                b18[1] = j
        b19 = b14[b18[0]]
        b20 = b14[b18[1]]
        for element in b20.b1:
            for element2 in b19.b1:
                matrix[element][element2] = -1
                matrix[element2][element] = -1
        b21 = b19.b1
        b19.b1 += b20.b1
        b19.b4 = class2(b19.b1, b19.b4, b20.b4)
        b14.remove(b20)
        for b17 in b14:
            if b17.b3 in b20.b1:
                b17.b3 = b16[0]
        b15 = -1
        b16 = -1
        for e in b19.b1:
            for b13 in range(len(matrix)):
                if matrix[e][b13] > b15:
                    b15 = matrix[e][b13]
                    b16 = b13
        b19.b3 = b16
        b19.b2 = b15
        print("Merged", b18, ":", b21, "&", b20.b1)
    return b14
def fonk10():
    b22 = [
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
    for row in b22:
        print(row)
    print()
    b23 = fonk7(b22)
    b14 = fonk8(b23)
    b24 = fonk9(b14, b23)
    print(b24[0].b4)
if b25 = = "__main__":
    fonk10()