class HuffmanHeap:
    def __init__(self, old, new=None):
        self.old = old
        self.new = new if new is not None else []
    def enqueue(self, item):
        self.new.append(item)
    def dequeue(self):
        if not self.old and self.new:
            return self.new.pop(0)
        elif not self.new and self.old:
            return self.old.pop(0)
        elif self.old and self.new:
            if self.old[0].get_freq() >= self.new[0].get_freq():
                return self.new.pop(0)
            else:
                return self.old.pop(0)
        else:
            print("Both old and new heaps are empty!")
            return None