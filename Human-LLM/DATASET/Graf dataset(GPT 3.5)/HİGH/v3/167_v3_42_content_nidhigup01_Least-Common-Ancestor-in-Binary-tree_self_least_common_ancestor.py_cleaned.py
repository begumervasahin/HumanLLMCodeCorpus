class class1:
    def fonk1(self, b1):
        self.b1 = b1
        self.b2 = None
        self.b3 = None
def fonk2(adjacency_matrix, b1, parent):
    b4 = class1(b1)
    if not adjacency_matrix or not adjacency_matrix[b1]:
        return None
    for child in range(len(adjacency_matrix[b1])):
        if adjacency_matrix[b1][child] == 1 and child != parent:
            if child < b1:
                b4.b2 = fonk2(adjacency_matrix, child, b1)
            else:
                b4.b3 = fonk2(adjacency_matrix, child, b1)
    return b4
def fonk3(b7, node1, node2):
    if b7 is None:
        return None
    if b7.b1 = = node1 or b7.b1 == node2:
        return b7
    b5 = fonk3(b7.b2, node1, node2)
    b6 = fonk3(b7.b3, node1, node2)
    if b5 and b6:
        return b7
    return b5 if b5 is not None else b6
def fonk4(adjacency_matrix, b1, node1, node2):
    b7 = fonk2(adjacency_matrix, b1, -1)
    b8 = fonk3(b7, node1, node2)
    return b8.b1 if b8 else None
print("LCA(1, 4) =", fonk4([[0, 1, 0, 0, 0],
                                [0, 0, 0, 0, 0],
                                [0, 0, 0, 0, 0],
                                [1, 0, 0, 0, 1],
                                [0, 0, 0, 0, 0]], b1 = 3, node1=1, node2=4))