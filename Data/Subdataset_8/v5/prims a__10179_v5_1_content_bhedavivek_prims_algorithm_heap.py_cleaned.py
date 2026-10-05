class Heap:
    def __init__(self):
        self._size = 0
        self._data = [0]
    def insert(self, key_value):
        self._data.append(key_value)
        self._size += 1
        self._heapify_up(self._size)
    def _heapify_up(self, index):
        while index > 1:
            parent_index = index
            if self._data[parent_index].distance > self._data[index].distance:
                self._data[parent_index], self._data[index] = self._data[index], self._data[parent_index]
                index = parent_index
            else:
                break
    def extract_min(self):
        if self._size < 1:
            return None
        min_element = self._data[1]
        self._data[1] = self._data[self._size]
        self._size -= 1
        if self._size > 1:
            self._heapify_down(1)
        self._data.pop()
        return min_element
    def _heapify_down(self, index):
        while 2 * index <= self._size:
            left_child_index = 2 * index
            right_child_index = left_child_index + 1
            smaller_child_index = left_child_index
            if (right_child_index <= self._size and
                    self._data[right_child_index].distance < self._data[left_child_index].distance):
                smaller_child_index = right_child_index
            if self._data[index].distance > self._data[smaller_child_index].distance:
                self._data[index], self._data[smaller_child_index] = self._data[smaller_child_index], self._data[index]
                index = smaller_child_index
            else:
                break
if __name__ == "__main__":
    pass