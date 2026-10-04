class PriorityQueue:
    def __init__(self):
        self.queue = [(0, 0)]
        self.size = 0
    def get_size(self):
        return self.size
    def find_min(self):
        if self.size > 0:
            return self.queue[1]
        return None
    def remove_min(self):
        min_element = self.find_min()
        if min_element:
            self.queue[1] = self.queue[self.size]
            self.size -= 1
            self.queue.pop()
            self._fix_down(1)
        return min_element
    def insert(self, element):
        self.queue.append(element)
        self.size += 1
        self._fix_up(self.size)
    def increase_key(self, node, value):
        for i in range(1, self.size + 1):
            if self.queue[i][1] == node:
                self.queue[i] = (value, node)
                self._fix_up(i)
                break
    def __contains__(self, element):
        return element in self.queue
    def _fix_down(self, index):
        while 2 * index <= self.size:
            child = 2 * index
            if child < self.size and self.queue[child][0] > self.queue[child + 1][0]:
                child += 1
            if self.queue[index][0] <= self.queue[child][0]:
                break
            self.queue[index], self.queue[child] = self.queue[child], self.queue[index]
            index = child
    def build_min_heap(self, elements):
        self.queue = [(0, 0)] + elements
        self.size = len(elements)
        for i in range(self.size
            self._fix_down(i)
    def _fix_up(self, index):
        while index > 1 and self.queue[index][0] < self.queue[index
            self.queue[index], self.queue[index
            index