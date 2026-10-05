class Heap:
    def __init__(self):
        self.array = [0]
    def insert(self, key_value):
        self.array.append(key_value)
        self.array[0] = len(self.array) - 1
        self.heapify_up(self.array[0])
    def heapify_up(self, index):
        while index > 1:
            j = index
            if int(self.array[j].distance) > int(self.array[index].distance):
                self.array[index], self.array[j] = self.array[j], self.array[index]
                index = j
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
            if 2 * index == self.array[0] or self.array[2 * index].distance < self.array[2 * index + 1].distance:
                j = 2 * index
            else:
                j = 2 * index + 1
            if self.array[j].distance < self.array[index].distance:
                self.array[index], self.array[j] = self.array[j], self.array[index]
                index = j
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
