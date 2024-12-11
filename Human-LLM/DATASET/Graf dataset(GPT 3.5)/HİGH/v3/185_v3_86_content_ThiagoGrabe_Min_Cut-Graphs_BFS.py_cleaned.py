class class1:
    def fonk1(self, b4, a2, b13, b5):
        b1 = [False] * len(b4)
        b2 = []
        b2.append(a2)
        b1[a2] = True
        while b2:
            b3 = b2.pop(0)
            for b9, b12 in enumerate(b4[b3]):
                if b12 > 0 and not b1[b9]:
                    b2.append(b9)
                    b1[b9] = True
                    b5[b9] = b3
        return b1[b13]
class class2:
    def fonk2(self, b4):
        self.b4 = b4
    def fonk3(self, a2, b13):
        a1 = 0
        b5 = [-1] * len(self.b4)
        b6 = class1()
        while b6.fonk1(self.b4, a2, b13, b5):
            b7 = float("inf")
            b8 = b13
            while b8 != a2:
                b7 = min(b7, self.b4[b5[b8]][b8])
                b8 = b5[b8]
            a1 += b7
            b9 = b13
            while b9 != a2:
                b3 = b5[b9]
                self.b4[b3][b9] -= b7
                self.b4[b9][b3] += b7
                b9 = b5[b9]
        return a1
def fonk4(file_path):
    with open(file_path, 'r') as file:
        b10 = file.readlines()
        num_vertices, b11 = map(int, b10[0].split())
        b4 = [[0] * num_vertices for _ in range(num_vertices)]
        for line in b10[1:]:
            b3, b9, b12 = map(int, line.split())
            b4[b3][b9] = b12
            b4[b9][b3] = b12
        return b4
def fonk5(b19, b15, b16, a1):
    with open(b19, 'w') as file:
        file.write(f"{b15}\n")
        file.write(' '.join(map(str, b16)) + '\n')
        file.write(f"{a1}\n")
def fonk6(b18, b19):
    b4 = fonk4(b18)
    a2 = 0
    b13 = len(b4) - 1
    b14 = class2(b4)
    a1 = b14.fonk3(a2, b13)
    b15 = sum(1 for flow in b4[a2] if flow > 0)
    b16 = [i for i, flow in enumerate(b4[a2]) if flow > 0]
    fonk5(b19, b15, b16, a1)
if b17 = = "__main__":
    b18 = "mincut_input/XXXX.in"
    b19 = "b19.txt"
    fonk6(b18, b19)