class class1:
    def fonk1(self, b1):
        self.b1 = b1
        self.b2 = None
        self.b3 = None
def fonk2():
    b4 = int(input("Enter node value (-1 for no node): "))
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
def fonk5(b5):
    if b5 is None:
        return
    print(b5.b1, b8 = " ")
    fonk5(b5.b2)
    fonk5(b5.b3)
def fonk6(b5):
    if b5 is None:
        return
    fonk6(b5.b2)
    print(b5.b1, b8 = " ")
    fonk6(b5.b3)
def fonk7(b5):
    if b5 is None:
        return
    fonk7(b5.b2)
    fonk7(b5.b3)
    print(b5.b1, b8 = " ")
def fonk8(b5):
    if b5 is None:
        return 0
    b11 = fonk8(b5.b2)
    b12 = fonk8(b5.b3)
    return max(b11, b12) + 1
def fonk9(b5, b13):
    if b5 is None:
        return
    if b13 = = 0:
        print(b5.b1, b8 = " ")
        return
    fonk9(b5.b2, b13 - 1)
    fonk9(b5.b3, b13 - 1)
def fonk10(b5, count):
    if b5 is None:
        return
    b5.b1 = count
    fonk10(b5.b2, count + 1)
    fonk10(b5.b3, count + 1)
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
import queue
class class2:
    def fonk13(self, b1):
        self.b1 = b1
        self.b2 = None
        self.b3 = None
def fonk14():
    b4 = int(input("Enter b5 node value: "))
    if b4 = = -1:
        return None
    b5 = class2(b4)
    b14 = queue.Queue()
    b14.put(b5)
    while not b14.empty():
        b15 = b14.get()
        b16 = int(input(f"Enter b2 child of {b15.b1}: "))
        if b16 != -1:
            b17 = class2(b16)
            b15.b2 = b17
            b14.put(b17)
        b18 = int(input(f"Enter b3 child of {b15.b1}: "))
        if b18 != -1:
            b19 = class2(b18)
            b15.b3 = b19
            b14.put(b19)
    return b5
def fonk15(b5):
    if b5 is None:
        return
    b14 = queue.Queue()
    b14.put(b5)
    while not b14.empty():
        b15 = b14.get()
        print(f"{b15.b1}:", b8 = "")
        if b15.b2 is not None:
            print(f"{b15.b2.b1},", b8 = "")
            b14.put(b15.b2)
        else:
            print("-1,", b8 = "")
        if b15.b3 is not None:
            print(b15.b3.b1)
            b14.put(b15.b3)
        else:
            print("-1")
def fonk16(post, inorder):
    if len(post) == 0:
        return None
    b20 = post.pop()
    b5 = class2(b20)
    b21 = inorder.b21(b20)
    b22 = inorder[:b21]
    b23 = inorder[b21 + 1:]
    b24 = post[:len(b22)]
    b25 = post[len(b22):]
    b5.b2 = fonk16(b24, b22)
    b5.b3 = fonk16(b25, b23)
    return b5
