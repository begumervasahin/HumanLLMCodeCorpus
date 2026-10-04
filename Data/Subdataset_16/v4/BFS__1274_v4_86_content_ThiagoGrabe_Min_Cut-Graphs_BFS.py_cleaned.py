class class1:
    def fonk1(self, b5, a1, a2, b6):
        b1 = [False] * len(b5)
        b2 = []
        b2.append(a1)
        b1[a1] = True
        while b2:
            b3 = b2.pop(0)
            for idx, capacity in enumerate(b5[b3]):
                if capacity > 0 and not b1[idx]:
                    b2.append(idx)
                    b1[idx] = True
                    b6[idx] = b3
        return b1[a2]
if b4 = = "__main__":
    b5 = [
        [0, 16, 13, 0, 0, 0],
        [0, 0, 10, 12, 0, 0],
        [0, 4, 0, 0, 14, 0],
        [0, 0, 9, 0, 0, 20],
        [0, 0, 0, 7, 0, 4],
        [0, 0, 0, 0, 0, 0]
    ]
    a1 = 0
    a2 = 5
    b6 = [-1] * len(b5)
    b7 = class1()
    if b7.fonk1(b5, a1, a2, b6):
        print("There is a path from a1 to a2")
    else:
        print("No path from a1 to a2")