import Queue
class class1:
    def fonk1(self, data):
        self.b1 = data
        self.b2 = None
        self.b3 = None
def fonk2(b4, b5):
    if b4 = = None:
        return
    if b5 = = 0:
        print b4.b1,
    fonk2(b4.b2, b5 - 1)
    fonk2(b4.b3, b5 - 1)
def fonk3(b4):
    if b4 = = None:
        return
    b6 = Queue.Queue()
    b6.put(b4)
    while 1:
        if b6.qsize() == 0:
            break
        b7 = b6.qsize()
        while b7 > 0:
            b8 = b6.get()
            print b8.b1,
            if b8.b2 != None:
                b6.put(b8.b2)
            if b8.b3 != None:
                b6.put(b8.b3)
            b7 -= 1
        print("")
'''
    Binary Tree used:
                    1
                /        \
               4          5
             /    \       /  \
            2      8      3   7
           /  \    /\         / \
           0   1  3  9        1  10
'''
b4 = class1(1)
b4.b2 = class1(4)
b4.b3 = class1(5)
b4.b2.b2 = class1(2)
b4.b2.b3 = class1(8)
b4.b3.b2 = class1(3)
b4.b3.b3 = class1(7)
b4.b2.b2.b2 = class1(0)
b4.b2.b2.b3 = class1(1)
b4.b2.b3.b2 = class1(3)
b4.b2.b3.b3 = class1(9)
b4.b3.b3.b2 = class1(1)
b4.b3.b3.b3 = class1(10)
fonk3(b4)