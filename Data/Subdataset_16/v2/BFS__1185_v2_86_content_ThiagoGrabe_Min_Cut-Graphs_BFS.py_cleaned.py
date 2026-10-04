from collections import defaultdict, deque
class class1:
    def fonk1(self, b1):
        self.b1 = b1
        self.b2 = len(b1)
    def fonk2(self, a2, b17, b7):
        b3 = [False] * self.b2
        b4 = deque([a2])
        b3[a2] = True
        while b4:
            b5 = b4.popleft()
            for b6 in range(self.b2):
                if not b3[b6] and self.b1[b5][b6] > 0:
                    b4.append(b6)
                    b3[b6] = True
                    b7[b6] = b5
                    if b6 = = b17:
                        return True
        return False
    def fonk3(self, a2, b17):
        b7 = [-1] * self.b2
        a1 = 0
        while self.fonk2(a2, b17, b7):
            b8 = float('Inf')
            b9 = b17
            while b9 != a2:
                b8 = min(b8, self.b1[b7[b9]][b9])
                b9 = b7[b9]
            a1 += b8
            b6 = b17
            while b6 != a2:
                b5 = b7[b6]
                self.b1[b5][b6] -= b8
                self.b1[b6][b5] += b8
                b6 = b7[b6]
        return a1
    def fonk4(self, a2):
        b3 = [False] * self.b2
        b4 = deque([a2])
        b3[a2] = True
        b10 = []
        while b4:
            b5 = b4.popleft()
            b10.append(b5)
            for b6 in range(self.b2):
                if not b3[b6] and self.b1[b5][b6] > 0:
                    b4.append(b6)
                    b3[b6] = True
        return b10
def fonk5(filename):
    b1 = defaultdict(lambda: defaultdict(int))
    with open(filename, 'r') as file:
        b11 = file.readline().strip().split()
        b2 = int(b11[0])
        b12 = int(b11[1])
        for _ in range(b12):
            b13 = file.readline().strip().split()
            b5 = int(b13[0])
            b6 = int(b13[1])
            b14 = int(b13[2])
            b1[b5][b6] = b14
            b1[b6][b5] = b14
    return b1, b2
def fonk6():
    b15 = 'mincut_input/XXXX.in'
    b16 = 'b16.txt'
    b1, b2 = fonk5(b15)
    a2 = 0
    b17 = b2 - 1
    b18 = class1(b1)
    a1 = b18.fonk3(a2, b17)
    b10 = b18.fonk4(a2)
    with open(b16, 'w') as file:
        file.write(f"{len(b10)}\n")
        file.write(" ".join(map(str, b10)) + "\n")
        file.write(f"{a1}\n")
    print("Successfully wrote output to", b16)
if b19 = = "__main__":
    fonk6()