class class1:
    def fonk1(self, b1, b2, b3, b4):
        self.b1 = b1
        self.b2 = b2
        self.b3 = b3
        self.b4 = b4
    def fonk2(self):
        return f"{self.b1} => {self.b2} (b3: {self.b3})"
class class2:
    def fonk3(self, b5 = None, b6=None, b7=None):
        self.b5 = b5
        self.b6 = b6
        self.b7 = b7
    def fonk4(self):
        b8 = "\n"
        b9 = [self]
        while b9:
            b10 = []
            for elem in b9:
                b8 += f"{str(elem.b5)} "
                if elem.b6:
                    b10.append(elem.b6)
                if elem.b7:
                    b10.append(elem.b7)
            b8 += "\n"
            b9 = b10
        return b8
    def fonk5(self):
        return self.b5 is not None
    def fonk6(self):
        b9 = [self]
        b8 = []
        while b9:
            b8.append(" ".join([str(b4.b5) for b4 in b9]))
            if any(b4 for b4 in b9):
                b11 = []
                for b4 in b9:
                    if b4.b5 is not None:
                        b11.extend([b4.b6, b4.b7])
                    else:
                        b11.append(b4)
                b9 = b11
            else:
                break
        return "\n" + "\n".join(b8)
def fonk7(b21):
    b12 = []
    for i in range(len(b21)):
        b13 = max(b21[i])
        b3 = b21[i].b3(b13)
        b14 = class1([i], b13, b3, class2([i]))
        b12.append(b14)
    return b12
def fonk8(b12, b22):
    while len(b12) > 1:
        b13 = -1
        b15 = [-1, -1]
        for j, b14 in enumerate(b12):
            if b14.b2 > b13:
                b13 = b14.b2
                b15 = [j, b14.b3]
        print(f"Found max b2: {b13} at indices {b15}")
        b16 = b15[0]
        b17 = next(j for j, b14 in enumerate(b12) if b15[1] in b14.b1)
        b18 = b12[b16]
        b19 = b12[b17]
        for element in b19.b1:
            for dest_element in b18.b1:
                b22[element][dest_element] = -1
                b22[dest_element][element] = -1
        print(f"Merging b12: {b18.b1} & {b19.b1}")
        b18.b1 += b19.b1
        b18.b4 = class2(b18.b1, b18.b4, b19.b4)
        b12.remove(b19)
        for b14 in b12:
            if b14.b3 in b19.b1:
                b14.b3 = b16
        b13 = -1
        a1 = -1
        for element in b18.b1:
            for i in range(len(b22)):
                if b22[element][i] > b13:
                    b13 = b22[element][i]
                    a1 = i
        b18.b3 = a1
        b18.b2 = b13
    return b12
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
    print("Representation Matrix:")
    for row in b21:
        print(row)
    print()
    b22 = [row[:] for row in b21]
    for i in range(len(b21)):
        b22[i][i] = -1
    b12 = fonk7(b22)
    b23 = fonk8(b12, b22)
    print("\nFinal Hierarchical Grouping:")
    print(b23[0].b4)