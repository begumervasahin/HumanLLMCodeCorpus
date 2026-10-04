class PriorityQueue:
    def __init__(self):
        self.queue = [(0, 0)]
        self.size = 0
    def get_size(self):
        return self.size
    def find_min(self):
        if self.size != 0:
            return self.queue[1]
        return None
    def remove_min(self):
        minimum = self.find_min()
        if minimum is not None:
            self.queue[1] = self.queue[self.size]
            self.size -= 1
            self.queue.pop()
            self.fix_down(1)
        return minimum
    def insert(self, element):
        self.queue.append(element)
        self.size += 1
        self.fix_up(self.size)
    def increase_key(self, node, new_value):
        for i in range(1, self.size + 1):
            if self.queue[i][1] == node:
                self.queue[i] = (new_value, node)
                self.fix_up(i)
                break
    def __contains__(self, element):
        return element in self.queue
    def fix_down(self, index):
        while 2 * index <= self.size:
            child = 2 * index
            if child < self.size and self.queue[child][0] > self.queue[child + 1][0]:
                child += 1
            if self.queue[index][0] <= self.queue[child][0]:
                break
            self.queue[index], self.queue[child] = self.queue[child], self.queue[index]
            index = child
    def build_min_heap(self, elements):
        self.queue = [(0, 0)]
        self.size = len(elements)
        self.queue.extend(elements)
        for i in range(len(elements)
            self.fix_down(i)
    def fix_up(self, index):
        while index > 1 and self.queue[index
            self.queue[index
            index