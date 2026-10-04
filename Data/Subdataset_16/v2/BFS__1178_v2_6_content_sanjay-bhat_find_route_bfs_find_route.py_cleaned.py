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
            for b16, distance in b6[b13]:
                b14 = b9[list(b6.keys()).index(b13)] + float(distance)
                b15 = list(b6.keys()).index(b16)
                if b9[b15] > b14:
                    b9[b15] = b14
                    b10[b15] = b13
                    b11[b15] = b16
                    b12[b15] = float(distance)
                    if b16 = = b3:
                        a1 = b14
        b17 = self.fonk3(b10, b11, b12, b9, b2, b3, a1)
        print(self.fonk4(b17, a1))
    def fonk2(self, b6, b2, b8, b4):
        b8[list(b6.keys()).index(b2)] = True
        if b2 in b6:
            for b16, _ in b6[b2]:
                if not b8[list(b6.keys()).index(b16)]:
                    self.fonk2(b6, b16, b8, b4)
        b4.append(b2)
    def fonk3(self, b10, b11, b12, b9, b2, b3, a1):
        a2 = 0
        b17 = []
        b18 = a1
        while a1 != 0:
            if b11[a2] == b3:
                b17.append((b10[a2], b11[a2], b12[a2]))
                a1 = b9[a2] - b12[a2]
                b3 = b10[a2]
                a2 = 0
            else:
                a2 += 1
        b17.reverse()
        return b17
    def fonk4(self, b17, a1):
        if a1 = = 0:
            return "distance: infinity\nroute:\nnone\n"
        else:
            b19 = f"distance: {a1} km\nroute:\n"
            for b10, b11, distance in b17:
                b19 += f"{b10} to {b11}, {distance} km\n"
            return b19
def fonk5():
    b20 = class1()
    b20.fonk1()
if b21 = = "__main__":
    fonk5()