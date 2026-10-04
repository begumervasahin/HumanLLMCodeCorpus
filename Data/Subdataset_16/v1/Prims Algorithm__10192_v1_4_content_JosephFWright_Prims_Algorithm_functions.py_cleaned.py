
class class1:
    def fonk1(self, filename):
        self.b1 = set()
        self.b2 = {}
        with open(filename, 'r') as file:
            for line in file:
                v1, v2, b3 = line.split()
                b3 = int(b3)
                self.b1.add(v1)
                self.b1.add(v2)
                self.b2[(v1, v2)] = b3
                self.b2[(v2, v1)] = b3
    def fonk2(self):
        return self.b2
    def fonk3(self):
        return set(self.b2.keys())
    def fonk4(self):
        return self.b1
from class1 import class1
b4 = class1('test_graph.txt')
def fonk5(e, b4):
    return b4.fonk2()[e]
def fonk6(b11, b4):
    b2 = []
    for v in b11[0]:
        for e in b4.fonk3():
            if v in e and e not in b2:
                b2.append(e)
        for e in b2:
            if e in b11[1]:
                b2.remove(e)
    return b2
def fonk7(b11, b4):
    b2 = fonk6(b11, b4)
    b5 = fonk6(b11, b4)
    b6 = b4.fonk4().difference(set(b11[0]))
    for v in b11[0]:
        for x in b6:
            for e in b4.fonk3():
                if v in e and x in e and e in b2:
                    b5.remove(e)
    b2 = list(set(b2) - set(b5))
    return b2
def fonk8(b11, b4):
    b2 = fonk7(b11, b4)
    b7 = b2[0]
    for e in b2:
        if fonk5(e, b4) < fonk5(b7, b4):
            b7 = e
    return b7
def fonk9(b11, b4):
    b1 = set(b11[0])
    b2 = list(b11[1])
    b8 = fonk8(b11, b4)
    b2.append(b8)
    for v in b8:
        if v in b4.fonk4() and v not in b1:
            b1.add(v)
    b9 = [b1, b2]
    return b9
def fonk10(b11, b4):
    return sum([fonk5(e, b4) for e in b11[1]])
b10 = 'A'
b11 = ([b10], [])
while len(b11[0]) < len(b4.fonk4()):
    b11 = fonk9(b11, b4)
print("Total cost of MST:", fonk10(b11, b4))
print("Edges in MST:", b11[1])