from Edges import Edges
class Heap:
    def __init__(self, dimension_type):
        self.heap_tree = {}
        self.dimension_type = dimension_type
    def insert(self, data):
        index = self.tree_size + 1
        if index > 1:
            parent_index = index
            new_node = Edges(data.id, data.distance, data.time, index)
            self.heap_tree[index] = new_node
            if new_node.index == 2 * self.heap_tree[parent_index].index:
                self.heap_tree[parent_index].left = new_node
            else:
                self.heap_tree[parent_index].right = new_node
            new_node.parent = self.heap_tree[parent_index]
            while index > 1 and self._calculate_weight(self.heap_tree[index]) < self._calculate_weight(self.heap_tree[parent_index]):
                self._swap(index, parent_index)
                index = parent_index
                parent_index = parent_index
        else:
            self.heap_tree[index] = data
    def extract_max(self):
        index = self.tree_size
        if index <= 0:
            return None
        self._swap(1, index)
        max_edge = self.heap_tree.pop(index)
        self._heapify(1)
        return max_edge
    def _calculate_weight(self, data):
        if 'distance' in self.dimension_type and 'time' in self.dimension_type:
            return data.distance + data.time
        elif 'distance' in self.dimension_type:
            return data.distance
        elif 'time' in self.dimension_type:
            return data.time
        else:
            raise ValueError("Invalid dimension type")
    def _heapify(self, root):
        left_child = 2 * root
        right_child = 2 * root + 1
        smallest = root
        if left_child <= self.tree_size and self._calculate_weight(self.heap_tree[left_child]) < self._calculate_weight(self.heap_tree[root]):
            smallest = left_child
        if right_child <= self.tree_size and self._calculate_weight(self.heap_tree[right_child]) < self._calculate_weight(self.heap_tree[smallest]):
            smallest = right_child
        if smallest != root:
            self._swap(root, smallest)
            self._heapify(smallest)
    def _swap(self, x, y):
        if x != y:
            self.heap_tree[x], self.heap_tree[y] = self.heap_tree[y], self.heap_tree[x]
            self.heap_tree[x].index, self.heap_tree[y].index = x, y
    @property
    def tree_size(self):
        return len(self.heap_tree)
if __name__ == "__main__":
    edges = [
        Edges(1, 10, 5),
        Edges(2, 15, 7),
        Edges(3, 5, 2),
        Edges(4, 20, 8),
    ]
    heap = Heap(dimension_type=['distance', 'time'])
    for edge in edges:
        heap.insert(edge)
    print("Heap after insertions:")
    for key, node in heap.heap_tree.items():
        print(f"Index {key}: ID={node.id}, Distance={node.distance}, Time={node.time}")
    print("\nExtracting max:")
    while heap.tree_size > 0:
        max_edge = heap.extract_max()
        print(f"Extracted: ID={max_edge.id}, Distance={max_edge.distance}, Time={max_edge.time}")