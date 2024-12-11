import sys
import romania
class class1:
    def fonk1(self):
        self.b1 = {}
    def fonk2(self):
        b2 = sys.argv[1]
        b3 = sys.argv[2]
        b4 = sys.argv[3]
        a1 = 0
        b5 = []
        b6 = romania.romania(0).get_data_romania(b2)
        b1 = b6[0]
        b7 = b6[1]
        b8 = [False] * b7
        for i in range(b7):
            if not b8[i]:
                self.fonk3(b1, b3, b8, b5)
        b9 = [float("Inf")] * b7
        b9[b1.keys().index(b3)] = 0.0
        b10 = [0] * b7
        b11 = [0] * b7
        b12 = [0] * b7
        while b5:
            b13 = b5.pop()
            for b15, distance in b1[b13]:
                b14 = float(b9[b1.keys().index(b13)]) + float(distance)
                if float(b9[b1.keys().index(b15)]) > b14:
                    b9[b1.keys().index(b15)] = b14
                    b10[b1.keys().index(b15)] = b13
                    b11[b1.keys().index(b15)] = b15
                    b12[b1.keys().index(b15)] = float(distance)
                    if b15 = = b4:
                        a1 = b14
            b13 = 0
            b16 = []
            b17 = a1
        while a1 != 0:
            if b11[b13] == b4:
                    b16.append(b10[b13])
                    b16.append(b11[b13])
                    b16.append(str(b12[b13]))
                    a1 = b9[b13] - b12[b13]
                    b4 = b10[b13]
                    b13 = 0
            else:
                b13 += 1
        b16.reverse()
        if b17 = = 0:
            b18 = "distance: infinity\nroute:\nnone\n"
        else:
            b18 = f"distance: {b17} km\nroute:\n"
            b13 = 0
            while b13 < len(b16):
                b18 += f"{b16[b13 + 2]} to {b16[b13 + 1]}, {b16[b13]} km\n"
                b13 += 3
        print(b18)
    def fonk3(self, b1, b3, b8, b5):
        b8[b1.keys().index(b3)] = True
        if b3 in b1.keys():
            for dest, distance in b1[b3]:
                if not b8[b1.keys().index(dest)]:
                    self.fonk3(b1, dest, b8, b5)
        b5.append(b3)
def fonk4():
    b19 = class1()
    b19.fonk2()
if b20 = = "__main__":
    fonk4()