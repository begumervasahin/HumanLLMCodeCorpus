class class1(object):
    def fonk1(self, x):
        self.b1 = x
        self.b2 = None
        self.b3 = None
def fonk2(b5):
    b4 = []
    if b5:
        b4 += fonk2(b5.b2)
        b4.append(b5.b1)
        b4 += fonk2(b5.b3)
    return b4
def fonk3(b5):
    b4 = []
    if b5:
        b4.append(b5.b1)
        b4 += fonk3(b5.b2)
        b4 += fonk3(b5.b3)
    return b4
def fonk4(arr, i):
    if i < len(arr):
        if arr[i] is None:
            return None
        b5 = class1(arr[i])
        b5.b2 = fonk4(arr, 2 * i + 1)
        b5.b3 = fonk4(arr, 2 * i + 2)
        return b5
    return None
b6 = [1, None, 2, None, None, 3]
b7 = fonk4(b6, 0)
print("In order Traversal")
print(fonk2(b7))
print("")
print("Pre-order Traversal")
print(fonk3(b7))
print("")
b8 = [1, 2, 3, 4, 5, 6, None]
b9 = fonk4(b8, 0)
print("In Order Traversal")
print(fonk2(b9))
print("")
print("Pre-order Traversal")
print(fonk3(b9))
print("")
b10 = [1, 2, 3]
b11 = fonk4(b10, 0)
print("In Order Traversal")
print(fonk2(b11))
print("")
print("Pre-order Traversal")
print(fonk3(b11))