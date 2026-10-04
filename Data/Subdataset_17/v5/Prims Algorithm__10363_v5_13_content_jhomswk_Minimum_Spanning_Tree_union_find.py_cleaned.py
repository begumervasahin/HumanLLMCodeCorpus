class Set:
    def __init__(self, value):
        self.value = value
        self.parent = self
        self.next = self
        self.rank = 0
    def findSet(self):
        if self.parent != self:
            self.parent = self.parent.findSet()
        return self.parent
    def union(self, other):
        root1 = self.findSet()
        root2 = other.findSet()
        if root1 != root2:
            if root1.rank < root2.rank:
                root1.parent = root2
            elif root1.rank > root2.rank:
                root2.parent = root1
            else:
                root2.parent = root1
                root1.rank += 1
            root1.next, root2.next = root2.next, root1.next
    def add(self, value):
        new_set = Set(value)
        self.union(new_set)
    def getElements(self):
        current = self
        while True:
            yield current.value
            current = current.next
            if current == self:
                break
    def __str__(self):
        return "{{{}}}".format(", ".join(map(str, self.getElements())))
    def __repr__(self):
        return self.__str__()