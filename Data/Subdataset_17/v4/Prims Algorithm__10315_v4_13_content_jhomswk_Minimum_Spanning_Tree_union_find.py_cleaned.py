class Set:
    def __init__(self, value):
        self.value = value
        self.parent = self
        self.next = self
        self.rank = 0
    def findSet(self):
        pathToRoot = []
        element = self
        while element is not element.parent:
            pathToRoot.append(element)
            element = element.parent
        root = element
        for element in pathToRoot:
            element.parent = root
        return root
    def union(self, other):
        selfRep = self.findSet()
        otherRep = other.findSet()
        if selfRep is not otherRep:
            if selfRep.rank < otherRep.rank:
                selfRep.parent = otherRep
            else:
                otherRep.parent = selfRep
                if selfRep.rank == otherRep.rank:
                    selfRep.rank += 1
            selfRep.next, otherRep.next = otherRep.next, selfRep.next
    def add(self, value):
        self.union(Set(value))
    def getElements(self):
        yield self.value
        element = self.next
        while element != self:
            yield element.value
            element = element.next
    def __str__(self):
        return "{{{}}}".format(", ".join(map(str, self.getElements())))
    def __repr__(self):
        return str(self)