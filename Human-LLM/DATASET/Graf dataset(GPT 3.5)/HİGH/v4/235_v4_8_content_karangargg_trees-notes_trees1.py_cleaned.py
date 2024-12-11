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
    b6 = fonk2()
    b7 = fonk2()
    b5.b2 = b6
    b5.b3 = b7
    return b5
def fonk3(b5):
    if b5 is None:
        return
    if b5.b1 != -1:
        print(b5.b1, b8 = ":")
    if b5.b2 is not None:
        print(b5.b2.b1, b8 = ",")
    else:
        print("-1", b8 = ",")
    if b5.b3 is not None:
        print(b5.b3.b1, b8 = "")
    else:
        print("-1", b8 = "")
    print()
    fonk3(b5.b2)
    fonk3(b5.b3)
b5 = fonk2()
fonk3(b5)
def fonk4(b5):
    if b5 is None:
        return 0
    b9 = fonk4(b5.b2)
    b10 = fonk4(b5.b3)
    return b9 + b10 + 1
b11 = fonk4(b5)
print(b11)
def fonk5(b5):
    if b5 is None:
        return
    print(b5.b1, b8 = " ")
    fonk5(b5.b2)
    fonk5(b5.b3)
fonk5(b5)
def fonk6(b5):
    if b5 is None:
        return
    fonk6(b5.b2)
    print(b5.b1, b8 = " ")
    fonk6(b5.b3)
fonk6(b5)
def fonk7(b5):
    if b5 is None:
        return
    fonk7(b5.b2)
    fonk7(b5.b3)
    print(b5.b1, b8 = " ")
fonk7(b5)
def fonk8(b5):
    if b5 is None:
        return 0
    b12 = fonk8(b5.b2)
    b13 = fonk8(b5.b3)
    return max(b12, b13) + 1
b14 = fonk8(b5)
print(b14)
def fonk9(b5, b15):
    if b5 is None:
        return
    if b15 = = 0:
        print(b5.b1)
    fonk9(b5.b2, b15 - 1)
    fonk9(b5.b3, b15 - 1)
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
        return
    if b5.b2 is None and b5.b3 is None:
        return None
    b5.b2 = fonk11(b5.b2)
    b5.b3 = fonk11(b5.b3)
    return b5
def fonk12(b5):
    if b5 is None:
        return
    if b5.b2 is not None and b5.b3 is not None:
        b16 = b5.b2
        b5.b2 = b5.b3
        b5.b3 = b16
    fonk12(b5.b2)
    fonk12(b5.b3)
    return b5
b17 = fonk12(b5)
fonk3(b17)
class class2:
    def fonk13(self, b1):
        self.b1 = b1
        self.b2 = None
        self.b3 = None
import queue
def fonk14():
    b4 = int(input())
    if b4 = = -1 or b4 < 0:
        return None
    b5 = class2(b4)
    q.put(b5)
    while not q.empty():
        b18 = q.get()
        print("Enter the b2 child of:", b18.b1)
        b2 = int(input())
        if b2 != -1:
            b19 = class2(b2)
            b18.b2 = b19
            q.put(b19)
        print("Enter the b3 child of:", b18.b1)
        b3 = int(input())
        if b3 != -1:
            b20 = class2(b3)
            b18.b3 = b20
            q.put(b20)
    return b5
def fonk15(b5):
    if b5 is None:
        return None
    q.put(b5)
    while not q.empty():
        b18 = q.get()
        print(b18.b1, b8 = ":")
        if b18.b2 is not None:
            print(b18.b2.b1, b8 = ",")
            q.put(b18.b2)
        if b18.b3 is not None:
            print(b18.b3.b1, b8 = "")
            q.put(b18.b3)
        print()
b5 = fonk14()
fonk15(b5)
def fonk16(postorder, inorder):
    if len(postorder) == 0:
        return None
    b4 = postorder[len(postorder) - 1]
    postorder.pop()
    b5 = class2(b4)
    a1 = -1
    for i in range(len(inorder)):
        if inorder[i] == b4:
            a1 = i
            break
    b21 = inorder[0:a1]
    b22 = inorder[a1 + 1:]
    b23 = postorder[0:len(b21)]
    b24 = postorder[len(b21):]
    b25 = fonk16(b23, b21)
    b26 = fonk16(b24, b22)
    b5.b2 = b25
    b5.b3 = b26
    return b5
def fonk17(b5, max_diameter):
    if b5 is None:
        return max_diameter