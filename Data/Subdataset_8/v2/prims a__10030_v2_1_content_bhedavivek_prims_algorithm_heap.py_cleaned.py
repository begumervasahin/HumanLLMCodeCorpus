class Heap:
    def __init__(self):
        self.array = [0]
    def insert(self, key_value):
        self.array.append(key_value)
        self.array[0] = len(self.array) - 1
        self.heapify_up(self.array[0])
    def heapify_up(self, index):
        while index > 1:
            parent_index = index
            if int(self.array[parent_index].distance) > int(self.array[index].distance):
                self.array[index], self.array[parent_index] = self.array[parent_index], self.array[index]
                index = parent_index
            else:
                break
    def extract_min(self):
        last_index = self.array[0]
        ret = self.array[1]
        self.array[1] = self.array[last_index]
        self.array[0] -= 1
        if self.array[0] > 1:
            self.heapify_down(1)
        del self.array[-1]
        return ret
    def heapify_down(self, index):
        while 2 * index <= self.array[0]:
            left_child_index = 2 * index
            right_child_index = 2 * index + 1 if (2 * index < self.array[0]) else left_child_index
            if self.array[left_child_index].distance < self.array[right_child_index].distance:
                smaller_child_index = left_child_index
            else:
                smaller_child_index = right_child_index
            if self.array[smaller_child_index].distance < self.array[index].distance:
                self.array[index], self.array[smaller_child_index] = self.array[smaller_child_index], self.array[index]
                index = smaller_child_index
            else:
                break
if __name__ == "__main__":
    h = Heap()
    h.insert(5)
    h.insert(3)
    h.insert(8)
    h.insert(1)
    h.insert(10)
    print(h.extract_min())
    print(h.extract_min())
w