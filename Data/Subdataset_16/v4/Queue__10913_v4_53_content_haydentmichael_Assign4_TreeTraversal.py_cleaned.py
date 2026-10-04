class class1(object):
    def fonk1(self, x):
        self.b1 = x
        self.b2 = None
        self.b3 = None
def fonk2(result, b5):
    if b5:
        fonk2(result, b5.b2)
        if b5.b1 is not None:
            result.append(b5.b1)
        fonk2(result, b5.b3)
    return result
def fonk3(result, b5):
    if b5:
        if b5.b1 is not None:
            result.append(b5.b1)
        fonk3(result, b5.b2)
        fonk3(result, b5.b3)
    return result
def fonk4(arr, b5, i, b7):
    if i < b7:
        b4 = class1(arr[i])
        b5 = b4
        b5.b2 = fonk4(arr, b5.b2, 2 * i + 1, b7)
        b5.b3 = fonk4(arr, b5.b3, 2 * i + 2, b7)
    return b5
def fonk5(title, result):
    print(title)
    for x in result:
        print(x)
    print(" ")
b6 = [
    [1, None, 2, None, None, 3],
    [1, 2, 3, 4, 5, 6, None],
    [1, 2, 3]
]
for arr in b6:
    b7 = len(arr)
    b5 = None
    b5 = fonk4(arr, b5, 0, b7)
    b8 = []
    b8 = fonk2(b8, b5)
    fonk5("In-order Traversal", b8)
    b9 = []
    b9 = fonk3(b9, b5)
    fonk5("Pre-order Traversal", b9)