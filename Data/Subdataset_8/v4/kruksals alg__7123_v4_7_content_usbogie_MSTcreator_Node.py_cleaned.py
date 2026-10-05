class Node:
    def __init__(self, xloc, yloc, kval, adjList):
        self.xloc = xloc
        self.yloc = yloc
        self.kval = kval
        self.adjList = adjList
    def __eq__(self, other):
        return (
            self.xloc == other.xloc
            and self.yloc == other.yloc
            and self.kval == other.kval
        )