class DisjointSet:
    _disjoint_set = list()
    def __init__(self, init_arr):
        self._disjoint_set = []
        if init_arr:
            for item in list(set(init_arr)):
                self._disjoint_set.append([item])
    def _find_index(self, elem):
        for item in self._disjoint_set:
            if elem in item:
                return self._disjoint_set.index(item)
        return None
    def find(self, elem):
        for item in self._disjoint_set:
            if elem in item:
                return self._disjoint_set[self._disjoint_set.index(item)]
        return None
    def union(self, elem1, elem2):
        index_elem1 = self._find_index(elem1)
        index_elem2 = self._find_index(elem2)
        if index_elem1 != index_elem2 and index_elem1 is not None and index_elem2 is not None:
            self._disjoint_set[index_elem2] = self._disjoint_set[index_elem2] + self._disjoint_set[index_elem1]
            del self._disjoint_set[index_elem1]
        return self._disjoint_set
    def get(self):
        return self._disjoint_set
init_arr = [1, 2, 3, 4, 5]
disjoint_set = DisjointSet(init_arr)
print("Initial disjoint set:", disjoint_set.get())
disjoint_set.union(1, 2)
disjoint_set.union(3, 4)
disjoint_set.union(4, 5)
print("After unions:", disjoint_set.get())
print("Find 1:", disjoint_set.find(1))
print("Find 2:", disjoint_set.find(2))
print("Find 3:", disjoint_set.find(3))
print("Find 4:", disjoint_set.find(4))
print("Find 5:", disjoint_set.find(5))
print("Find 6:", disjoint_set.find(6))