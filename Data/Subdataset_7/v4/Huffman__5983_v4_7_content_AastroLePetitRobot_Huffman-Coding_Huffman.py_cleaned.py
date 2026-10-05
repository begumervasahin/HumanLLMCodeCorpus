from b5 import PriorityQueue
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
def fonk4(b16):
    b5 = PriorityQueue()
    b6 = []
    b7 = False
    b8 = False
    for b9 in b16:
        if b9 not in b6:
            b6.append(b9)
            b5.put(class1(b9, b16.count(b9)))
        elif b9 = = ' ' and not b7:
            b5.put(class1(b9, b16.count(b9)))
            b7 = True
        elif b9 = = ',' and not b8:
            b5.put(class1(b9, b16.count(b9)))
            b8 = True
    return b5
def fonk5(b5):
    while b5.qsize() > 1:
        b10 = b5.get()
        b11 = b5.get()
        b3 = b10.b3 + b11.b3
        b12 = class1(None, b3, b10, b11)
        b5.put(b12)
    return b5.get()
def fonk6(b12, code, b18):
    if b12.b1 is None and b12.b4 is None:
        b18.update({b12.b2: code})
        return b18
    if b12.b1 is not None:
        fonk6(b12.b1, code + "0", b18)
    if b12.b4 is not None:
        fonk6(b12.b4, code + "1", b18)
def fonk7(b16, b18):
    b13 = ""
    for b9 in b16:
        b13 += str(b18[b9])
    return b13
def fonk8(b16, b12):
    global a1
    if b12.b1 is None and b12.b4 is None:
        b14 = b12.b2
        return b14
    if b16[a1] == "0":
        a1 += 1
        return fonk8(b16, b12.b1)
    elif b16[a1] == "1":
        a1 += 1
        return fonk8(b16, b12.b4)
a1 = 0
b15 = open('texteEncode.txt', 'r')
b16 = b15.read()
b15.close()
b5 = fonk4(b16)
b17 = fonk5(b5)
print(b17)
b18 = {}
fonk6(b17, "", b18)
print(b18)
b13 = fonk7(b16, b18)
print(b13)
b15 = open('texteEncode.txt', 'w')
b15.write(str(b13))
b15.close()
b16 = fonk7(b16, b18)
b19 = ""
while a1 < len(b16):
    b19 += fonk8(b16, b17)
print(b19)
b15.close()