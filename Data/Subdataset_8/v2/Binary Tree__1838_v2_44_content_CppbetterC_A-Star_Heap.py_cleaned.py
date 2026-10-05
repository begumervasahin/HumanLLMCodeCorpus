class Edge:
    def __init__(self, id, distance, time, index):
        self.id = id
        self.distance = distance
        self.time = time
        self.index = index
        self.left = None
        self.right = None
        self.parent = None
class MinHeap:
    def __init__(self, dimension_type):
        self.heap_tree = {}
        self.dimension_type = dimension_type
    def insert(self, data):
        index = self.tree_size + 1
        if index > 1:
            parent_index = int(index / 2)
            new_node = Edge(data.id, data.distance, data.time, index)
            self.heap_tree[index] = new_node
            if new_node.index == 2 * self.heap_tree[parent_index].index:
                self.heap_tree[parent_index].left = new_node
            else:
                self.heap_tree[parent_index].right = new_node
            new_node.parent = self.heap_tree[parent_index]
            while True:
                if self.calculate_weight(self.heap_tree[index]) < self.calculate_weight(self.heap_tree[parent_index]):
                    self.__swap(self.heap_tree, index, parent_index)
                    index = parent_index
                    parent_index = int(parent_index / 2)
                    if parent_index == 0:
                        break
                else:
                    break
        else:
            self.heap_tree[index] = data
    def extract_min(self):
        index = self.tree_size
        if index <= 0:
            return None
        self.__swap(self.heap_tree, 1, index)
        edge = self.heap_tree[1]
        self.heap_tree.pop(index)
        self.__heapify(self.heap_tree, 1, len(self.heap_tree))
        return edge
    def calculate_weight(self, data):
        if 'distance' in self.dimension_type and 'time' in self.dimension_type:
            return data.distance + data.time
        elif 'distance' in self.dimension_type:
            return data.distance
        elif 'time' in self.dimension_type:
            return data.time
        else:
            raise Exception('<---Dimension Error--->')
    def __heapify(self, data, root, length):
        left_child = 2 * root
        right_child = 2 * root + 1
        if left_child < length and self.calculate_weight(data[left_child]) < self.calculate_weight(data[root]):
            min_node = left_child
        else:
            min_node = root
        if right_child < length and self.calculate_weight(data[right_child]) < self.calculate_weight(data[min_node]):
            min_node = right_child
        if min_node != root:
            self.__swap(data, root, min_node)
            self.__heapify(data, min_node, length)
    @staticmethod
    def __swap(data, x, y):
        if x != y:
            data[x], data[y] = data[y], data[x]
    @property
    def tree_size(self):
        return len(self.heap_tree)
heap = MinHeap(['distance', 'time'])
edge1 = Edge(1, 10, 5, 1)
edge2 = Edge(2, 8, 4, 2)
edge3 = Edge(3, 12, 6, 3)
heap.insert(edge1)
heap.insert(edge2)
heap.insert(edge3)
print("Tree size:", heap.tree_size)
print("Extracted min:", heap.extract_min().id)
print("Tree size after extraction:", heap.tree_size)