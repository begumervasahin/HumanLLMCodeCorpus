class class1:
    def fonk1(self, b1):
        self.b1 = b1
        self.b2 = None
        self.b3 = None
def fonk2():
    b4 = int(input("Enter b5 b1 (-1 to exit): "))
    if b4 = = -1:
        return None
    b5 = class1(b4)
    print("Enter b2 child of", b5.b1)
    b5.b2 = fonk2()
    print("Enter b3 child of", b5.b1)
    b5.b3 = fonk2()
    return b5
def fonk3(b5):
    if b5 is None:
        return
    print(b5.b1, b6 = ":")
    if b5.b2:
        print(b5.b2.b1, b6 = ",")
    else:
        print("-1", b6 = ",")
    if b5.b3:
        print(b5.b3.b1, b6 = "")
    else:
        print("-1", b6 = "")
    print()
    fonk3(b5.b2)
    fonk3(b5.b3)
b5 = fonk2()
print("Binary Tree:")
fonk3(b5)
def fonk4(b5):
    if b5 is None:
        return 0
    return fonk4(b5.b2) + fonk4(b5.b3) + 1
print("Number of nodes in the tree:", fonk4(b5))
def fonk5(b5):
    if b5:
        print(b5.b1, b6 = " ")
        fonk5(b5.b2)
        fonk5(b5.b3)
print("Preorder Traversal:")
fonk5(b5)
def fonk6(b5):
    if b5:
        fonk6(b5.b2)
        print(b5.b1, b6 = " ")
        fonk6(b5.b3)
print("\nInorder Traversal:")
fonk6(b5)
def fonk7(b5):
    if b5:
        fonk7(b5.b2)
        fonk7(b5.b3)
        print(b5.b1, b6 = " ")
print("\nPostorder Traversal:")
fonk7(b5)
def fonk8(b5):
    if b5 is None:
        return 0
    return max(fonk8(b5.b2), fonk8(b5.b3)) + 1
print("\nHeight of the tree:", fonk8(b5))
def fonk9(b5, b7):
    if b5 is None:
        return
    if b7 = = 0:
        print(b5.b1)
    fonk9(b5.b2, b7 - 1)
    fonk9(b5.b3, b7 - 1)
print("Elements at depth 2:")
fonk9(b5, 2)
def fonk10(b5, depth):
    if b5 is None:
        return
    b5.b1 = depth
    fonk10(b5.b2, depth + 1)
    fonk10(b5.b3, depth + 1)
fonk10(b5, 0)
print("Replaced tree:")
fonk3(b5)
def fonk11(b5):
    if b5 is None:
        return None
    if b5.b2 is None and b5.b3 is None:
        return None
    b5.b2 = fonk11(b5.b2)
    b5.b3 = fonk11(b5.b3)
    return b5
print("Tree after removing leaves:")
fonk3(fonk11(b5))
def fonk12(b5):
    if b5 is None:
        return None
    b5.b2, b5.b3 = fonk12(b5.b3), fonk12(b5.b2)
    return b5
b5 = fonk12(b5)
print("Mirrored Tree:")
fonk3(b5)
class class2:
    def fonk13(self, b1):
        self.b1 = b1
        self.b2 = None
        self.b3 = None
def fonk14():
    b8 = queue.Queue()
    b4 = int(input("Enter b5 b1 (-1 to exit): "))
    if b4 = = -1:
        return None
    b5 = class2(b4)
    b8.put(b5)
    while not b8.empty():
        b9 = b8.get()
        b10 = int(input("Enter b2 child of {}: ".format(b9.b1)))
        if b10 != -1:
            b11 = class2(b10)
            b9.b2 = b11
            b8.put(b11)
        b12 = int(input("Enter b3 child of {}: ".format(b9.b1)))
        if b12 != -1:
            b13 = class2(b12)
            b9.b3 = b13
            b8.put(b13)
    return b5
def fonk15(b5):
    if b5 is None:
        return
    b8 = queue.Queue()
    b8.put(b5)
    while not b8.empty():
        b9 = b8.get()
        print(b9.b1, b6 = ":")
        if b9.b2:
            print(b9.b2.b1, b6 = ",")
            b8.put(b9.b2)
        if b9.b3:
            print(b9.b3.b1, b6 = "")
            b8.put(b9.b3)
        print()
b5 = fonk14()
print("Level-wise Tree:")
fonk15(b5)
def fonk16(postorder, inorder):
    if not postorder or not inorder:
        return None
    b4 = postorder.pop()
    b5 = class2(b4)
    b14 = inorder.index(b4)
    b5.b3 = fonk16(postorder, inorder[b14+1:])
    b5.b2 = fonk16(postorder, inorder[:b14])
    return b5
def fonk17(b5):
    if b5 is None:
        return 0
    def fonk18(node):
        if node is None:
            return 0, 0
        left_diameter, b15 = fonk18(node.b2)
        right_diameter, b16 = fonk18(node.b3)
        return max(left_diameter, right_diameter, b15 + b16), max(b15, b16) + 1
    return fonk18(b5)[0]
print("Diameter of the tree:", fonk17(b5))