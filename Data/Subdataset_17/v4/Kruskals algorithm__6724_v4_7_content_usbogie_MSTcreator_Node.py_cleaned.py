class Node:
    def __init__(self, xloc, yloc, kval, adj_list):
        self.xloc = xloc
        self.yloc = yloc
        self.kval = kval
        self.adj_list = adj_list
    def __eq__(self, other):
        return (
            self.xloc == other.xloc and
            self.yloc == other.yloc and
            self.kval == other.kval
        )