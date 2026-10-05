class MaxHeap(object):
    def __init__(self):
        self.names = [-1]
        self.values = [-1]
        self.size = 0
    def maximum(self):
        return self.values[1]
    def insert(self, name, value):
        self.size += 1
        self.names.append(name)
        self.values.append(value)
        self.heapify_up(self.size)
    def update(self, name, value):
        for i in range(1, self.size + 1):
            if self.names[i] == name:
                self.values[i] = value
                self.heapify_down(i)
                break
    def delete(self, index):
        if self.size == 1 or index == self.size:
            self.values.pop()
            self.names.pop()
            self.size -= 1
        else:
            self.values[index] = self.values.pop()
            self.names[index] = self.names.pop()
            self.size -= 1
            self.heapify_down(index)
    def heapify_up(self, index):
        while index > 1 and self.values[index] > self.values[index
            self.swap(index, index
            index
    def heapify_down(self, index):
        while index <= self.size
            child = 2 * index
            if child + 1 <= self.size and self.values[child] < self.values[child + 1]:
                child += 1
            if self.values[index] >= self.values[child]:
                break
            self.swap(index, child)
            index = child
    def swap(self, index1, index2):
        self.values[index1], self.values[index2] = self.values[index2], self.values[index1]
        self.names[index1], self.names[index2] = self.names[index2], self.names[index1]
    def heap_sort(self):
        sorted_values = []
        sorted_names = []
        while self.size >= 1:
            sorted_values.append(self.values[1])
            sorted_names.append(self.names[1])
            self.delete(1)
        return sorted_values, sorted_names
mh = MaxHeap()
mh.insert(1, 10)
print('\n', mh.names, mh.values)
mh.insert(2, 30)
print('\n', mh.names, mh.values)
mh.insert(3, 40)
print('\n', mh.names, mh.values)
mh.insert(4, 15)
print('\n', mh.names, mh.values)
mh.insert(5, 60)
print('\n', mh.names, mh.values)
print(mh.maximum())
mh.delete(1)
print('\n', mh.names, mh.values)
print(mh.maximum())
