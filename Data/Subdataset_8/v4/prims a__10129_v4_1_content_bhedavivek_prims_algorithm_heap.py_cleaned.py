class Heap:
    def __init__(self):
        self.array = [0]
    def insert(self, key_value):
        self.array.append(key_value)
        self.array[0] = len(self.array) - 1
        self._heapify_up(self.array[0])
    def _heapify_up(self, index):
        while index > 1:
            parent_index = index
            if self.array[parent_index].distance > self.array[index].distance:
                self.array[parent_index], self.array[index] = self.array[index], self.array[parent_index]
                index = parent_index
            else:
                break
    def extract_min(self):
        if self.array[0] < 1:
            return None
        min_element = self.array[1]
        last_element = self.array[self.array[0]]
        self.array[1] = last_element
        self.array[0] -= 1
        if self.array[0] > 1:
            self._heapify_down(1)
        self.array.pop()
        return min_element
    def _heapify_down(self, index):
        while 2 * index <= self.array[0]:
            left_child_index = 2 * index
            right_child_index = left_child_index + 1
            if right_child_index > self.array[0] or self.array[left_child_index].distance < self.array[right_child_index].distance:
                smaller_child_index = left_child_index
            else:
                smaller_child_index = right_child_index
            if self.array[index].distance > self.array[smaller_child_index].distance:
                self.array[index], self.array[smaller_child_index] = self.array[smaller_child_index], self.array[index]
                index = smaller_child_index
            else:
                break
if __name__ == "__main__":
    pass