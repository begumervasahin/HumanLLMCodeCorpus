class class1:
    def fonk1(self, b1):
        self.b1 = b1
        self.b2 = None
        self.b3 = None
def fonk2(node, b4 = None):
    if b4 is None:
        b4 = []
    if node:
        fonk2(node.b2, b4)
        if node.b1 is not None:
            b4.append(node.b1)
        fonk2(node.b3, b4)
    return b4
def fonk3(node, b4 = None):
    if b4 is None:
        b4 = []
    if node:
        if node.b1 is not None:
            b4.append(node.b1)
        fonk3(node.b2, b4)
        fonk3(node.b3, b4)
    return b4
def fonk4(values, b5 = 0):
    if b5 >= len(values) or values[b5] is None:
        return None
    b6 = class1(values[b5])
    b6.b2 = fonk4(values, 2 * b5 + 1)
    b6.b3 = fonk4(values, 2 * b5 + 2)
    return b6
def fonk5(traversal, traversal_type):
    """
    Print the traversal of the binary tree.
    Args:
        traversal (list): List of values representing the traversal.
        traversal_type (str): The type of traversal ("In-order" or "Pre-order").
    """
    print(f"{traversal_type} Traversal:")
    for b1 in traversal:
        print(b1, b7 = ' ')
    print('\n')
if b8 = = "__main__":
    b9 = [
        [1, None, 2, None, None, 3],
        [1, 2, 3, 4, 5, 6, None],
        [1, 2, 3]
    ]
    for b5, tree_values in enumerate(b9):
        b6 = fonk4(tree_values)
        b10 = fonk2(b6)
        b11 = fonk3(b6)
        print(f"Tree {b5 + 1}: {tree_values}")
        fonk5(b10, "In-order")
        fonk5(b11, "Pre-order")