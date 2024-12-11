import queue
class class1:
    def fonk1(self, b1):
        self.b1 = b1
        self.b2 = None
        self.b3 = None
def fonk2():
    b4 = int(input())
    if b4 = = -1:
        return None
    b5 = class1(b4)
    b5.b2 = fonk2()
    b5.b3 = fonk2()
    return b5
def fonk3(b5):
    if b5 is None:
        return
    print(b5.b1, b6 = ":")
    print(b5.b2.b1 if b5.b2 else -1, b6 = ",")
    print(b5.b3.b1 if b5.b3 else -1)
    fonk3(b5.b2)
    fonk3(b5.b3)
b5 = fonk2()
fonk3(b5)
def fonk4(b5):
    if b5 is None:
        return 0
    b7 = fonk4(b5.b2)
    b8 = fonk4(b5.b3)
    return b7 + b8 + 1
b9 = fonk4(b5)
print(b9)
def fonk5(b5):
    if b5 is None:
        return
    print(b5.b1, b6 = " ")
    fonk5(b5.b2)
    fonk5(b5.b3)
fonk5(b5)
def fonk6(b5):
    if b5 is None:
        return
    fonk6(b5.b2)
    print(b5.b1, b6 = " ")
    fonk6(b5.b3)
fonk6(b5)
def fonk7(b5):
    if b5 is None:
        return
    fonk7(b5.b2)
    fonk7(b5.b3)
    print(b5.b1, b6 = " ")
fonk7(b5)
def fonk8(b5):
    if b5 is None:
        return 0
    b10 = fonk8(b5.b2)
    b11 = fonk8(b5.b3)
    return max(b10, b11) + 1
b12 = fonk8(b5)
print(b12)
def fonk9(b5, b13):
    if b5 is None:
        return
    if b13 = = 0:
        print(b5.b1)
    fonk9(b5.b2, b13 - 1)
    fonk9(b5.b3, b13 - 1)
fonk9(b5, 2)
def fonk10(b5, count):
    if b5 is None:
        return
    b5.b1 = count
    fonk10(b5.b2, count + 1)
    fonk10(b5.b3, count + 1)
fonk10(b5, 0)
fonk3(b5)
def fonk11(b5):
    if b5 is None:
        return None
    if b5.b2 is None and b5.b3 is None:
        return None
    b5.b2 = fonk11(b5.b2)
    b5.b3 = fonk11(b5.b3)
    return b5
def fonk12(b5):
    if b5 is None:
        return
    b5.b2, b5.b3 = b5.b3, b5.b2
    fonk12(b5.b2)
    fonk12(b5.b3)
    return b5
b14 = fonk12(b5)
fonk3(b14)
class class2:
    def fonk13(self, b1):
        self.b1 = b1
        self.b2 = None
        self.b3 = None
def fonk14():
    b4 = int(input())
    if b4 = = -1 or b4 < 0:
        return None
    b5 = class2(b4)
    b15 = queue.Queue()
    b15.put(b5)
    while not b15.empty():
        b16 = b15.get()
        b2 = int(input())
        if b2 != -1:
            b17 = class2(b2)
            b16.b2 = b17
            b15.put(b17)
        b3 = int(input())
        if b3 != -1:
            b18 = class2(b3)
            b16.b3 = b18
            b15.put(b18)
    return b5
def fonk15(b5):
    if b5 is None:
        return None
    b15 = queue.Queue()
    b15.put(b5)
    while not b15.empty():
        b16 = b15.get()
        print(b16.b1, b6 = ":")
        if b16.b2 is not None:
            print(b16.b2.b1, b6 = ",")
            b15.put(b16.b2)
        if b16.b3 is not None:
            print(b16.b3.b1, b6 = "")
            b15.put(b16.b3)
        print()
b5 = fonk14()
fonk15(b5)
def fonk16(postorder, inorder):
    if len(postorder) == 0:
        return None
    b4 = postorder.pop()
    b5 = class2(b4)
    b19 = inorder.b19(b4)
    b20 = inorder[:b19]
    b21 = inorder[b19 + 1:]
    b22 = postorder[:len(b20)]
    b23 = postorder[len(b20):]
    b24 = fonk16(b22, b20)
    b25 = fonk16(b23, b21)
    b5.b2 = b24
    b5.b3 = b25
    return b5
def fonk17(b5):
    if b5 is None:
        return 0
