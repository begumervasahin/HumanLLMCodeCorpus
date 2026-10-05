class Heap:
    def __init__(self):
        self.heap_list = [0]
    def insert(self, key_value):
        self.heap_list.append(key_value)
        self.update_heap_size()
        self.heapify_up(self.size())
    def update_heap_size(self):
        self.heap_list[0] = self.size()
    def size(self):
        return len(self.heap_list) - 1
    def heapify_up(self, index):
        while index > 1:
            parent_index = index
            if self.is_parent_greater(parent_index, index):
                self.swap_nodes(parent_index, index)
                index = parent_index
            else:
                break
    def is_parent_greater(self, parent_index, index):
        return int(self.heap_list[parent_index].distance) > int(self.heap_list[index].distance)
    def swap_nodes(self, index1, index2):
        self.heap_list[index1], self.heap_list[index2] = self.heap_list[index2], self.heap_list[index1]
    def extract_min(self):
        last_index = self.size()
        min_element = self.heap_list[1]
        self.heap_list[1] = self.heap_list[last_index]
        self.update_heap_size()
        if self.size() > 1:
            self.heapify_down(1)
        self.heap_list.pop()
        return min_element
    def heapify_down(self, index):
        while 2 * index <= self.size():
            left_child_index = 2 * index
            right_child_index = left_child_index + 1
            smaller_child_index = self.find_smaller_child(left_child_index, right_child_index)
            if self.is_child_smaller(smaller_child_index, index):
                self.swap_nodes(index, smaller_child_index)
                index = smaller_child_index
            else:
                break
    def find_smaller_child(self, left_child_index, right_child_index):
        if right_child_index > self.size() or \
                int(self.heap_list[left_child_index].distance) < int(self.heap_list[right_child_index].distance):
            return left_child_index
        else:
            return right_child_index
    def is_child_smaller(self, child_index, parent_index):
        return int(self.heap_list[child_index].distance) < int(self.heap_list[parent_index].distance)
if __name__ == "__main__":
    h = Heap()
    h.insert(5)
    h.insert(3)
    h.insert(8)
    h.insert(1)
    h.insert(10)
    print(h.extract_min())
    print(h.extract_min())
