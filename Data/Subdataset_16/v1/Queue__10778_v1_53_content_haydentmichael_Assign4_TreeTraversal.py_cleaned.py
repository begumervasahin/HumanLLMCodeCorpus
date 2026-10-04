class class1(object):
    def fonk1(self, x):
        self.b1 = x
        self.b2 = None
        self.b3 = None
def fonk2(a, b5):
    if b5:
        fonk2(a, b5.b2)
        if b5.b1 is not None:
            a.append(b5.b1)
        fonk2(a, b5.b3)
    return a
def fonk3(a, b5):
    if b5:
        if b5.b1 is not None:
            a.append(b5.b1)
        fonk3(a, b5.b2)
        fonk3(a, b5.b3)
    return a
def fonk4(arr, b5, i, b8):
    if i < b8:
        b4 = class1(arr[i])
        b5 = b4
        b5.b2 = fonk4(arr, b5.b2, 2 * i + 1, b8)
        b5.b3 = fonk4(arr, b5.b3, 2 * i + 2, b8)
    return b5
def fonk5(traversal, order_type):
    print(f"{order_type} Traversal")
    for x in traversal:
        print(x)
    print(" ")
if b6 = = "__main__":
    b7 = [
        [1, None, 2, None, None, 3],
        [1, 2, 3, 4, 5, 6, None],
        [1, 2, 3]
    ]
    for i, arr in enumerate(b7):
        b8 = len(arr)
        b5 = fonk4(arr, None, 0, b8)
        b9 = fonk2([], b5)
        b10 = fonk3([], b5)
        print(f"Array {i + 1}: {arr}")
        fonk5(b9, "In-order")
        fonk5(b10, "Pre-order")