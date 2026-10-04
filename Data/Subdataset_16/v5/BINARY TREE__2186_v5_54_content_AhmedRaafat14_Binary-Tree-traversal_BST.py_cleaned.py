import queue
class class1:
    def fonk1(self, b1):
        self.b1 = b1
        self.b2 = None
        self.b3 = None
def fonk2(b9, b4):
    if b9 is None:
        return
    if b4 = = 0:
        print(b9.b1, b5 = ' ')
    else:
        fonk2(b9.b2, b4 - 1)
        fonk2(b9.b3, b4 - 1)
def fonk3(b9):
    if b9 is None:
        return
    b6 = queue.Queue()
    b6.put(b9)
    while not b6.empty():
        b7 = b6.qsize()
        while b7 > 0:
            b8 = b6.get()
            print(b8.b1, b5 = ' ')
            if b8.b2 is not None:
                b6.put(b8.b2)
            if b8.b3 is not None:
                b6.put(b8.b3)
            b7 -= 1
        print("")
b9 = class1(1)
b9.b2 = class1(4)
b9.b3 = class1(5)
b9.b2.b2 = class1(2)
b9.b2.b3 = class1(8)
b9.b3.b2 = class1(3)
b9.b3.b3 = class1(7)
b9.b2.b2.b2 = class1(0)
b9.b2.b2.b3 = class1(1)
b9.b2.b3.b2 = class1(3)
b9.b2.b3.b3 = class1(9)
b9.b3.b3.b2 = class1(1)
b9.b3.b3.b3 = class1(10)
fonk3(b9)