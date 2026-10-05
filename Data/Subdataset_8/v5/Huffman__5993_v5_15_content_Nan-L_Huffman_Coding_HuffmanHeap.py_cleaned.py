class HuffmanHeap:
    def __init__(self, old=None, new=None):
        self.old = old or []
        self.new = new or []
    def enqueue(self, item):
        self.new.append(item)
    def dequeue(self):
        if not self.old and not self.new:
            print("Both old and new lists are empty!")
            return None
        if not self.old:
            return self.new.pop(0)
        if not self.new:
            return self.old.pop(0)
        if self.old[0].get_freq() >= self.new[0].get_freq():
            return self.new.pop(0)
        else:
            return self.old.pop(0)