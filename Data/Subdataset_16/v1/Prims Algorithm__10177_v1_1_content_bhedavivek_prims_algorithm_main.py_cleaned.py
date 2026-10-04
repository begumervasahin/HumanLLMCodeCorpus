import sys
class class1:
    def fonk1(self, b2, b1 = 0, b3=float('inf')):
        self.b2 = b2
        self.a1 = 0
        self.b1 = b1
        self.b3 = b3
    def fonk2(self):
        return self.b3
class class2:
    def fonk3(self, n):
        self.b4 = [[] for _ in range(n)]
    def fonk4(self, u, b11, b17):
        b5 = class1(b11, u, b17)
        self.b4[u-1].append(b5)
def fonk5(b5):
    array.append(b5)
    array[0] = len(array) - 1
    fonk6(array[0])
    b18[b5.b2-1].a1 = array[0]
def fonk6(b7):
    while b7 > 1:
        b6 = b7
        if array[b6].b3 > array[b7].b3:
            b18[array[b7].b2-1].a1 = b6
            b18[array[b6].b2-1].a1 = b7
            array[b7], array[b6] = array[b6], array[b7]
            b7 = b6
        else:
            break
def fonk7():
    b18[array[1].b2-1].a1 = 0
    b8 = array[0]
    b18[array[b8].b2-1].a1 = 1
    b9 = array[1]
    array[1] = array[b8]
    array[0] -= 1
    if array[0] > 1:
        fonk9(1)
    array.pop()
    return b9
def fonk8(heap_index, updated_distance, b1):
    if heap_index > 0:
        array[heap_index].b3 = updated_distance
        array[heap_index].b1 = b1
        fonk6(heap_index)
def fonk9(b7):
    while 2 * b7 <= array[0]:
        b6 = 2 * b7
        if b6 < array[0] and array[b6].b3 > array[b6 + 1].b3:
            b6 += 1
        if array[b6].b3 < array[b7].b3:
            b18[array[b7].b2-1].a1 = b6
            b18[array[b6].b2-1].a1 = b7
            array[b7], array[b6] = array[b6], array[b7]
            b7 = b6
        else:
            break
def fonk10(b16, b19):
    fonk5(b19)
    b10 = []
    for i in range(len(b18)):
        if i != b19.b2 - 1:
            b5 = class1(i + 1)
            fonk5(b5)
    while len(array) > 1:
        b11 = fonk7()
        b10.append(b11)
        for b5 in b16.b4[b11.b2-1]:
            if b5.b3 < b18[b5.b2-1].b3:
                b18[b5.b2-1].b3 = b5.b3
                fonk8(b18[b5.b2-1].a1, b5.b3, b11.b2)
                b18[b5.b2-1].b1 = b11.b2
    return b10
b12 = sys.argv[1]
b13 = sys.argv[2]
with open(b12, "r") as file:
    b14 = [line.strip() for line in file]
b15 = int(b14[0].split()[0])
b16 = class2(b15)
for line in b14[1:]:
    u, b11, b17 = map(int, line.split())
    b16.fonk5(u, b11, b17)
    b16.fonk5(b11, u, b17)
b18 = [class1(i + 1) for i in range(b15)]
b19 = class1(1)
b20 = fonk10(b16, b19)
b21 = sum(b5.b3 for b5 in b20 if b5.b2 != 0 and b5.b1 != 0)
b20 = sorted(b20, key=lambda b11: (b11.b2, b11.b1))
with open(b13, "b17") as writer:
    writer.write(f"{b21}\n")
    for b5 in b20:
        if b5.b2 != 0 and b5.b1 != 0:
            writer.write(f"{b5.b2} {b5.b1} {b5.b3}\n")