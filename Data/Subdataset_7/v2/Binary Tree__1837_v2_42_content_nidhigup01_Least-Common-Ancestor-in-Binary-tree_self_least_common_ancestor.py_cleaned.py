class class1:
    def fonk1(self, b1):
        self.b1 = b1
        self.b2 = None
        self.b3 = None
def fonk2(adjacency_matrix, b1, node1, node2):
    def fonk3(adjacency_matrix, b1, parent):
        b4 = class1(b1)
        if not adjacency_matrix or not adjacency_matrix[b1]:
            return None
        for child in range(len(adjacency_matrix[b1])):
            if adjacency_matrix[b1][child] == 1 and child != parent:
                if child < b1:
                    b4.b2 = fonk3(adjacency_matrix, child, b1)
                else:
                    b4.b3 = fonk3(adjacency_matrix, child, b1)
        return b4
    def fonk4(b4, node1, node2):
        if b4 is None:
            return None
        if b4.b1 = = node1 or b4.b1 == node2:
            return b4
        b5 = fonk4(b4.b2, node1, node2)
        b6 = fonk4(b4.b3, node1, node2)
        if b5 and b6:
            return b4
        return b5 if b5 is not None else b6
    b7 = fonk3(adjacency_matrix, b1, -1)
    b8 = fonk4(b7, node1, node2)
    return b8.b1 if b8 else None
print("LCA(1, 4) =", fonk2([[0, 1, 0, 0, 0],
                                [0, 0, 0, 0, 0],
                                [0, 0, 0, 0, 0],
                                [1, 0, 0, 0, 1],
                                [0, 0, 0, 0, 0]], b1 = 3, node1=1, node2=4))