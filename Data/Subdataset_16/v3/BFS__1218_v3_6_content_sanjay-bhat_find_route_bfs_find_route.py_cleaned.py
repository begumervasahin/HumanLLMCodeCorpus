import romania
import sys
class class1:
    def fonk1(self):
        b1 = sys.argv[1]
        b2 = sys.argv[2]
        b3 = sys.argv[3]
        b4 = romania.romania(0).getDataRomania(b1)
        b5 = b4[0]
        b6 = b4[1]
        b7 = [False] * b6
        b8 = []
        for i in range(b6):
            if not b7[i]:
                self.fonk2(b5, list(b5.keys())[i], b7, b8)
        b9 = [float("Inf")] * b6
        b9[list(b5.keys()).index(b2)] = 0.0
        b10 = [None] * b6
        b11 = [None] * b6
        b12 = [0] * b6
        while b8:
            b13 = b8.pop()
            b14 = list(b5.keys()).index(b13)
            if b9[b14] != float("Inf"):
                for neighbor, distance in b5[b13]:
                    b15 = list(b5.keys()).index(neighbor)
                    b16 = b9[b14] + float(distance)
                    if b9[b15] > b16:
                        b9[b15] = b16
                        b10[b15] = b13
                        b11[b15] = neighbor
                        b12[b15] = float(distance)
        b17 = self.fonk3(b10, b11, b12, b9, b2, b3)
        print(self.fonk4(b17, b9[list(b5.keys()).index(b3)]))
    def fonk2(self, b5, city, b7, b8):
        b18 = list(b5.keys()).index(city)
        b7[b18] = True
        for neighbor, _ in b5.get(city, []):
            b15 = list(b5.keys()).index(neighbor)
            if not b7[b15]:
                self.fonk2(b5, neighbor, b7, b8)
        b8.append(city)
    def fonk3(self, b10, b11, b12, b9, b2, b3):
        b17 = []
        b19 = b3
        while b19 != b2:
            b14 = list(b11).index(b19)
            b17.append((b10[b14], b11[b14], b12[b14]))
            b19 = b10[b14]
        b17.reverse()
        return b17
    def fonk4(self, b17, b20):
        if b20 = = float("Inf"):
            return "distance: infinity\nroute:\nnone\n"
        else:
            b21 = f"distance: {b20} km\nroute:\n"
            for b10, b11, distance in b17:
                b21 += f"{b10} to {b11}, {distance} km\n"
            return b21
def fonk5():
    b22 = class1()
    b22.fonk1()
if b23 = = "__main__":
    fonk5()