class class1:
    def fonk1(self, x):
        self.b1 = x
        self.b2 = None
        self.b3 = None
def fonk2(b4):
    if not b4:
        return []
    return fonk2(b4.b2) + [b4.b1] + fonk2(b4.b3)
def fonk3(b4):
    if not b4:
        return []
    return [b4.b1] + fonk3(b4.b2) + fonk3(b4.b3)
def fonk4(arr, i):
    if i < len(arr):
        if arr[i] is None:
            return None
        b4 = class1(arr[i])
        b4.b2 = fonk4(arr, 2 * i + 1)
        b4.b3 = fonk4(arr, 2 * i + 2)
        return b4
    return None
def fonk5(arr):
    b4 = fonk4(arr, 0)
    print("Inorder Traversal:")
    print(fonk2(b4))
    print("")
    print("Preorder Traversal:")
    print(fonk3(b4))
    print("")
b5 = [1, None, 2, None, None, 3]
fonk5(b5)
b6 = [1, 2, 3, 4, 5, 6, None]
fonk5(b6)
b7 = [1, 2, 3]
fonk5(b7)