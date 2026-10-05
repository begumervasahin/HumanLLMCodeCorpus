class Node(object):
    def __init__(self, xloc, yloc, kval, adjList):
        self.xloc = xloc
        self.yloc = yloc
        self.kval = kval
        self.adjList = adjList
    def __eq__(self, rhs):
        return self.xloc == rhs.xloc and self.yloc == rhs.yloc and self.kval == rhs.kval
node1 = Node(1, 2, 3, [4, 5, 6])
node2 = Node(1, 2, 3, [4, 5, 6])
node3 = Node(4, 5, 6, [7, 8, 9])
print("node1 == node2:", node1 == node2)
print("node1 == node3:", node1 == node3)
