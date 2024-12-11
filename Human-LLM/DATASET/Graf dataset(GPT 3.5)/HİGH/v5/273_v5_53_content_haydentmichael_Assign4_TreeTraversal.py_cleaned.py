class class1:
    def fonk1(self, x):
        self.b1 = x
        self.b2 = None
        self.b3 = None
def fonk2(b4):
    if b4 is None:
        return []
    return fonk2(b4.b2) + [b4.b1] + fonk2(b4.b3)
def fonk3(b4):
    if b4 is None:
        return []
    return [b4.b1] + fonk3(b4.b2) + fonk3(b4.b3)
def fonk4(arr, i, b6):
    b4 = None
    if i < b6:
        if arr[i] is not None:
            b4 = class1(arr[i])
            b4.b2 = fonk4(arr, 2 * i + 1, b6)
            b4.b3 = fonk4(arr, 2 * i + 2, b6)
    return b4
def fonk5(traversal_type, b4):
    """
    Print the traversal results of a binary tree.
    Args:
    traversal_type (str): Type of traversal (e.g., "In-order", "Pre-order").
    b4 (class1): The b4 node of the binary tree.
    """
    print(f"{traversal_type} Traversal")
    for x in traversal_type.lower() + "Traversal"(b4):
        print(x)
    print()
b5 = [1, None, 2, None, None, 3]
b6 = len(b5)
b7 = fonk4(b5, 0, b6)
fonk5("In-order", b7)
fonk5("Pre-order", b7)
b8 = [1, 2, 3, 4, 5, 6, None]
b9 = len(b8)
b10 = fonk4(b8, 0, b9)
fonk5("In-order", b10)
fonk5("Pre-order", b10)
b11 = [1, 2, 3]
b12 = len(b11)
b13 = fonk4(b11, 0, b12)
fonk5("In-order", b13)
fonk5("Pre-order", b13)