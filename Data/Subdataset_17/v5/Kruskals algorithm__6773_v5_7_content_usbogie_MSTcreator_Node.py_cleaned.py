class Node:
    def __init__(self, xloc, yloc, kval, adj_list=None):
        self.xloc = xloc
        self.yloc = yloc
        self.kval = kval
        self.adj_list = adj_list if adj_list is not None else []
    def __eq__(self, other):
        if not isinstance(other, Node):
            return False
        return (
            self.xloc == other.xloc and
            self.yloc == other.yloc and
            self.kval == other.kval
        )