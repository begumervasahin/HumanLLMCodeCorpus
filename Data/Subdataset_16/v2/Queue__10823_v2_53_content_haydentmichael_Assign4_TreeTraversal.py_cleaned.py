class class1:
    def fonk1(self, b1):
        self.b1 = b1
        self.b2 = None
        self.b3 = None
def fonk2(result_list, b4):
    if b4:
        fonk2(result_list, b4.b2)
        if b4.b1 is not None:
            result_list.append(b4.b1)
        fonk2(result_list, b4.b3)
    return result_list
def fonk3(result_list, b4):
    if b4:
        if b4.b1 is not None:
            result_list.append(b4.b1)
        fonk3(result_list, b4.b2)
        fonk3(result_list, b4.b3)
    return result_list
def fonk4(values, b5, index, length):
    if index < length:
        b4 = class1(values[index])
        b5 = b4
        b5.b2 = fonk4(values, b5.b2, 2 * index + 1, length)
        b5.b3 = fonk4(values, b5.b3, 2 * index + 2, length)
    return b5
def fonk5(traversal, traversal_type):
    print(f"{traversal_type} Traversal:")
    for b1 in traversal:
        print(b1)
    print()
if b6 = = "__main__":
    b7 = [
        [1, None, 2, None, None, 3],
        [1, 2, 3, 4, 5, 6, None],
        [1, 2, 3]
    ]
    for index, tree_values in enumerate(b7):
        b8 = len(tree_values)
        b5 = fonk4(tree_values, None, 0, b8)
        b9 = fonk2([], b5)
        b10 = fonk3([], b5)
        print(f"Tree {index + 1}: {tree_values}")
        fonk5(b9, "In-order")
        fonk5(b10, "Pre-order")