import romania
import sys
class class1:
    def fonk1(self):
        b1 = sys.argv[1]
        b2 = sys.argv[2]
        b3 = sys.argv[3]
        a1 = 0
        b4 = []
        b5 = romania.romania(0).getDataRomania(b1)
        b6 = b5[0]
        b7 = b5[1]
        b8 = [False] * b7
        for i in range(b7):
            if not b8[i]:
                self.fonk2(b6, b2, b8, b4)
        b9 = [float("Inf")] * b7
        b9[list(b6.keys()).index(b2)] = 0.0
        b10 = [0] * b7
        b11 = [0] * b7
        b12 = [0] * b7
        while b4:
            b13 = b4.pop()
            for b15, distance in b6[b13]:
                b14 = float(b9[list(b6.keys()).index(b13)]) + float(distance)
                if float(b9[list(b6.keys()).index(b15)]) > b14:
                    b9[list(b6.keys()).index(b15)] = b14
                    b10[list(b6.keys()).index(b15)] = b13
                    b11[list(b6.keys()).index(b15)] = b15
                    b12[list(b6.keys()).index(b15)] = float(distance)
                    if b15 = = b3:
                        a1 = b14
        b13 = 0
        b16 = []
        b17 = a1
        while a1 != 0:
            if b11[b13] == b3:
                b16.append(b10[b13])
                b16.append(b11[b13])
                b16.append(str(b12[b13]))
                a1 = b9[b13] - b12[b13]
                b3 = b10[b13]
                b13 = 0
            else:
                b13 += 1
        b16.reverse()
        if b17 = = 0:
            b18 = "distance: infinity\nroute:\nnone\n"
        else:
            b18 = "distance: " + str(b17) + " km\n" + "route:\n"
            b13 = 0
            while b13 < len(b16):
                b18 += b16[b13 + 2] + " to " + b16[b13 + 1] + ", " + b16[b13] + " km\n"
                b13 += 3
        print(b18)
    def fonk2(self, b6, b2, b8, b4):
        b8[list(b6.keys()).index(b2)] = True
        if b2 in b6.keys():
            for d, distance in b6[b2]:
                if not b8[list(b6.keys()).index(d)]:
                    self.fonk2(b6, d, b8, b4)
        b4.append(b2)
def fonk3():
    b19 = class1()
    b19.fonk1()
if b20 = = "__main__":
    fonk3()