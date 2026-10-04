class class1:
    def fonk1(self, b9, a1):
        def fonk2(b2, b3, b9):
            if len(b9) < 3:
                return b2
            while b2 <= b3:
                b1 = b2 + (b3 - b2)
                if b1 > 0 and b9[b1] < b9[b1 - 1]:
                    return b1
                elif b9[b1] >= b9[b2]:
                    if b9[b1] > b9[b3]:
                        b2 = b1 + 1
                    else:
                        break
                else:
                    b3 = b1 - 1
            return b2
        def fonk3(b2, b3, b4, b9):
            while b2 <= b3:
                b1 = b2 + (b3 - b2)
                if b9[b1] == b4:
                    return b1
                elif b9[b1] < b4:
                    b2 = b1 + 1
                else:
                    b3 = b1 - 1
            return -1
        b4 = a1
        b5 = len(b9)
        b6 = fonk2(0, b5 - 1, b9)
        if b6 = = 0:
            return fonk3(0, b5 - 1, b4, b9)
        elif b4 >= b9[0]:
            return fonk3(0, b6 - 1, b4, b9)
        else:
            return fonk3(b6, b5 - 1, b4, b9)
if b7 = = "__main__":
    b8 = class1()
    b9 = [4, 5, 6, 7, 0, 1, 2]
    a1 = 1
    b10 = b8.fonk1(b9, a1)
    print(f"Index of b4 {a1}: {b10}")