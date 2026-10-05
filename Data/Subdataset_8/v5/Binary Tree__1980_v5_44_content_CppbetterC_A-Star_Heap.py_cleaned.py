from Edges import Edges
class Heap:
    def __init__(self, dimension_type):
        self.heap_tree = []
        self.dimension_type = dimension_type
    def insert(self, data):
        self.heap_tree.append(data)
        index = len(self.heap_tree) - 1
        self.__heapify_up(index)
    def extract_max(self):
        if not self.heap_tree:
            return None
        root = self.heap_tree[0]
        self.heap_tree[0] = self.heap_tree[-1]
        self.heap_tree.pop()
        self.__heapify_down(0)
        return root
    def cal_weight(self, data):
        if 'distance' in self.dimension_type and 'time' in self.dimension_type:
            return data.distance + data.time
        elif 'distance' in self.dimension_type:
            return data.distance
        elif 'time' in self.dimension_type:
            return data.time
        else:
            raise Exception('<---Dimension Error--->')
    def __heapify_up(self, index):
        while index > 0:
            parent_index = (index - 1)
            if self.cal_weight(self.heap_tree[index]) < self.cal_weight(self.heap_tree[parent_index]):
                self.heap_tree[index], self.heap_tree[parent_index] = self.heap_tree[parent_index], self.heap_tree[index]
                index = parent_index
            else:
                break
    def __heapify_down(self, index):
        length = len(self.heap_tree)
        while True:
            left_child = 2 * index + 1
            right_child = 2 * index + 2
            min_node = index
            if left_child < length and self.cal_weight(self.heap_tree[left_child]) < self.cal_weight(self.heap_tree[min_node]):
                min_node = left_child
            if right_child < length and self.cal_weight(self.heap_tree[right_child]) < self.cal_weight(self.heap_tree[min_node]):
                min_node = right_child
            if min_node != index:
                self.heap_tree[index], self.heap_tree[min_node] = self.heap_tree[min_node], self.heap_tree[index]
                index = min_node
            else:
                break
    @property
    def tree_size(self):
        return len(self.heap_tree)