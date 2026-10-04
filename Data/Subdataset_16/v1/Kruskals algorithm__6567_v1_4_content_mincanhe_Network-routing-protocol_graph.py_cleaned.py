import random
class class1:
    def fonk1(self, b1):
        self.b1 = b1
        self.b2 = []
    def fonk2(self, connection):
        self.b2.append(connection)
    def fonk3(self, connection):
        self.b2.remove(connection)
    def fonk4(self, t):
        return any(c[0] == t for c in self.b2)
def fonk5(n, degree):
    b3 = [class1(i) for i in range(n)]
    b4 = []
    b5 = list(range(n))
    random.shuffle(b5)
    for i in range(n):
        b6 = i
        b7 = i
        for _ in range(degree
            b6 = (b6 + 1) % n
            b7 = (b7 - 1) % n
            if b6 > i:
                b8 = random.randint(0, 100)
                b3[b5[i]].fonk2([b5[b6], b8])
                b3[b5[b6]].fonk2([b5[i], b8])
                b4.append(sorted([b5[i], b5[b6]]) + [b8])
            if b7 > i:
                b8 = random.randint(0, 100)
                b3[b5[i]].fonk2([b5[b7], b8])
                b3[b5[b7]].fonk2([b5[i], b8])
                b4.append(sorted([b5[i], b5[b7]]) + [b8])
    with open('./b4.txt', 'a') as file:
        for edge in b4:
            file.write(f"{edge[0]} {edge[1]} {edge[2]}\n")
    return b3
fonk5(5000, 6)
fonk5(5000, 1000)