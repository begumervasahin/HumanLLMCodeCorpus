class class1:
    def fonk1(self, b4, a2, b14, b5):
        b1 = [False] * len(b4)
        b2 = []
        b2.append(a2)
        b1[a2] = True
        while b2:
            b3 = b2.pop(0)
            for idx, value in enumerate(b4[b3]):
                if value > 0 and not b1[idx]:
                    b2.append(idx)
                    b1[idx] = True
                    b5[idx] = b3
        return b1[b14]
class class2:
    def fonk2(self, b4):
        self.b4 = b4
    def fonk3(self, a2, b14):
        a1 = 0
        b5 = [-1] * len(self.b4)
        b6 = class1()
        while b6.fonk1(self.b4, a2, b14, b5):
            b7 = float("inf")
            b8 = b14
            while b8 != a2:
                b7 = min(b7, self.b4[b5[b8]][b8])
                b8 = b5[b8]
            a1 += b7
            b9 = b14
            while b9 != a2:
                b10 = b5[b9]
                self.b4[b10][b9] -= b7
                self.b4[b9][b10] += b7
                b9 = b5[b9]
        return a1
def fonk4(file_path):
    with open(file_path, 'r') as file:
        b11 = file.readlines()
        num_vertices, b12 = map(int, b11[0].split())
        b4 = [[0] * num_vertices for _ in range(num_vertices)]
        for line in b11[1:]:
            b10, b9, b13 = map(int, line.split())
            b4[b10][b9] = b13
            b4[b9][b10] = b13
        return b4
def fonk5(b21, b17, b18, b16):
    with open(b21, 'w') as file:
        file.write(str(b17) + '\n')
        file.write(' '.join(map(str, b18)) + '\n')
        file.write(str(b16) + '\n')
def fonk6(b20, b21):
    b4 = fonk4(b20)
    a2 = 0
    b14 = len(b4) - 1
    b15 = class2(b4)
    b16 = b15.fonk3(a2, b14)
    b17 = sum(1 for a1 in b4[a2] if a1 > 0)
    b18 = [i for i, a1 in enumerate(b4[a2]) if a1 > 0]
    fonk5(b21, b17, b18, b16)
if b19 = = "__main__":
    b20 = "mincut_input/XXXX.in"
    b21 = "b21.txt"
    fonk6(b20, b21)
