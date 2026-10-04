class Set:
    def __init__(self, value):
        self.value = value
        self.parent = self
        self.next = self
        self.rank = 0
    def findSet(self):
        elements_to_compress = []
        current = self
        while current is not current.parent:
            elements_to_compress.append(current)
            current = current.parent
        root = current
        for element in elements_to_compress:
            element.parent = root
        return root
    def union(self, other):
        root1 = self.findSet()
        root2 = other.findSet()
        if root1 is not root2:
            if root1.rank < root2.rank:
                root1.parent = root2
            else:
                root2.parent = root1
                if root1.rank == root2.rank:
                    root1.rank += 1
            root1.next, root2.next = root2.next, root1.next
    def add(self, value):
        new_set = Set(value)
        self.union(new_set)
    def getElements(self):
        yield self.value
        current = self.next
        while current != self:
            yield current.value
            current = current.next
    def __str__(self):
        return "{{{}}}".format(", ".join(map(str, self.getElements())))
    def __repr__(self):
        return str(self)
if __name__ == "__main__":
    set1 = Set(1)
    set2 = Set(2)
    set3 = Set(3)
    set1.union(set2)
    set2.union(set3)
    set1.add(4)
    print(set1)
    print(set2)
    print(set3)
