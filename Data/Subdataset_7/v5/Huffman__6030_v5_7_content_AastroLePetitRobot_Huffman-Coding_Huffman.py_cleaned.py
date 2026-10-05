from queue import PriorityQueue
class class1:
    def fonk1(self, b2, b3, b1 = None, b4=None):
        self.b2 = b2
        self.b3 = b3
        self.b1 = b1
        self.b4 = b4
    def fonk2(self, other):
        return self.b3 < other.b3
    def fonk3(self):
        return "class1: value ({}), b3 ({}), b1(), b4()\n".format(self.b2, self.b3)
def fonk4(b14):
    b5 = PriorityQueue()
    b6 = set()
    for char in b14:
        if char not in b6:
            b5.put(class1(char, b14.count(char)))
            b6.add(char)
    return b5
def fonk5(b5):
    while b5.qsize() > 1:
        b7 = b5.get()
        b8 = b5.get()
        b3 = b7.b3 + b8.b3
        b9 = class1(None, b3, b7, b8)
        b5.put(b9)
    return b5.get()
def fonk6(b9, b10 = "", b11=None):
    if b11 is None:
        b11 = {}
    if b9 is not None:
        if b9.b1 is None and b9.b4 is None:
            b11[b9.b2] = b10
        else:
            fonk6(b9.b1, b10 + "0", b11)
            fonk6(b9.b4, b10 + "1", b11)
    return b11
def fonk7(b14, b11):
    b12 = ""
    for char in b14:
        b12 += b11[char]
    return b12
def fonk8(b14, b9):
    global a1
    if b9.b1 is None and b9.b4 is None:
        b13 = b9.b2
        return b13
    if b14[a1] == "0":
        a1 += 1
        return fonk8(b14, b9.b1)
    elif b14[a1] == "1":
        a1 += 1
        return fonk8(b14, b9.b4)
with open('texteEncode.txt', 'r') as file:
    b14 = file.read()
b5 = fonk4(b14)
b15 = fonk5(b5)
print(b15)
b11 = fonk6(b15)
print(b11)
b12 = fonk7(b14, b11)
print(b12)
with open('texteEncode.txt', 'w') as file:
    file.write(str(b12))
a1 = 0
b16 = ""
while a1 < len(b12):
    b16 += fonk8(b12, b15)
print(b16)