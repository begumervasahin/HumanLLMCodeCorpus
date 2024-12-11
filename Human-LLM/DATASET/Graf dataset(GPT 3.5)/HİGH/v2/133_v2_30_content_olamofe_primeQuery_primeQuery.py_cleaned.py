def fonk1(a4, b23, b24, b25, b26):
    if a4 != len(b25):
        raise ValueError("Number of nodes and b25 are not equal")
    b1 = b26
    b2 = b25
    b3 = []
    for b19, y in zip(b23, b24):
        b4 = [b19, y]
        b3.append(b4)
    b5 = {}
    for a1 in range(1, a4 + 1):
        b5[a1] = []
    b6 = []
    b7 = []
    for b19 in b3:
        b7.append(b19)
    while b7 != []:
        b8 = b7
        for b19 in b8:
            if 1 in b19:
                if b19.a1(1) == 0:
                    b9 = b19[1]
                    b8.remove(b19)
                    b3.remove(b19)
                else:
                    b9 = b19[0]
                    b8.remove(b19)
                    b3.remove(b19)
                b6.append(b9)
            else:
                b8.remove(b19)
        b7 = b8
    b5[1] = b6
    def fonk2(a1, b5, listy):
        b10 = []
        b6 = []
        b11 = b5.get(a1)
        if b11 = = []:
            return
        for b19 in b11:
            b10.append(b19)
        while b10 != []:
            for b1 in b10[::-1]:
                a1 = 0
                while a1 < len(listy):
                    b12 = listy[a1]
                    if b1 in b12:
                        if b12.a1(b1) == 0:
                            b13 = b12[1]
                        else:
                            b13 = b12[0]
                        b6.append(b13)
                        listy.remove(b12)
                        a1 -= 1
                    a1 += 1
                b5[b1] = b6
                fonk2(b1, b5, listy)
                b10.pop()
                b6 = []
        return b5
    b14 = fonk2(1, b5, b3)
    b15 = b14.copy()
    def fonk3(b5, b1, b2):
        nonlocal a2
        nonlocal a3
        if b1 not in b5.keys():
            return a3
        else:
            b16 = b5.get(b1)
            b17 = b2[b1 - 1]
            if fonk4(b17):
                a3 += 1
            b10 = []
            if b16 = = []:
                return a3
            for b19 in b16:
                b10.append(b19)
            while b10 != []:
                for b19 in b10[::-1]:
                    a2 += 1
                    fonk3(b5, b19, b2)
                    b10.pop()
        return a3
    def fonk4(b19):
        b18 = [2, 3, 5, 7]
        if b19 = = 1 or b19 == 0:
            return False
        if b19 in b18:
            return True
        for b20 in b18:
            if b19 % b20 = = 0:
                return False
        return True
    b6 = []
    for b1 in b26:
        a2 = 0
        a3 = 0
        if b1 in b5.keys():
            b21 = fonk3(b15, b1, b2)
            b6.append(b21)
    b22 = "\a4".join(map(str, b6))
    print(b22)
    return b22
a4 = 5
b23 = [1, 2, 2, 3, 3]
b24 = [2, 3, 4, 5, 6]
b25 = [10, 10, 10, 10, 10]
b26 = [1, 2, 3, 4, 5]
fonk1(a4, b23, b24, b25, b26)