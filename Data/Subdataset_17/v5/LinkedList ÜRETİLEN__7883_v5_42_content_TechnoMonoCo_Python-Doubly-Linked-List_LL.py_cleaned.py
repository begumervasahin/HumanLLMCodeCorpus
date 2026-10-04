class Node:
    def __init__(self, data=None, next_node=None, prev_node=None):
        self.data = data
        self.next_node = next_node
        self.prev_node = prev_node
    def remove(self, data):
        if self.prev_node is None:
            if self.data == data:
                if self.next_node is None:
                    self.data = None
                else:
                    next_node = self.next_node
                    self.data = next_node.data
                    self.next_node = next_node.next_node
                    if self.next_node:
                        self.next_node.prev_node = self
                    del next_node
                return 0
            elif self.next_node is None:
                return -1
            else:
                return self.next_node.remove(data)
        else:
            if self.next_node is None:
                if self.data == data:
                    prev_node = self.prev_node
                    prev_node.next_node = None
                    del self
                    return 0
                else:
                    return -1
            else:
                if self.data == data:
                    prev_node = self.prev_node
                    next_node = self.next_node
                    prev_node.next_node = next_node
                    next_node.prev_node = prev_node
                    del self
                    return 0
                else:
                    return self.next_node.remove(data)
    def insert(self, data):
        if data < self.data:
            new_node = Node(data, self, self.prev_node)
            if self.prev_node:
                self.prev_node.next_node = new_node
            self.prev_node = new_node
        elif self.next_node is None:
            new_node = Node(data, None, self)
            self.next_node = new_node
        else:
            self.next_node.insert(data)
    def _collect(self, elements):
        if self.data is not None:
            elements.append(str(self.data))
        if self.next_node:
            self.next_node._collect(elements)
    def contains(self):
        if self.data is None and self.next_node is None:
            print("Empty.")
        else:
            elements = []
            self._collect(elements)
            print(", ".join(elements))
def test():
    base = Node(0)
    print("contains:")
    base.contains()
    print()
    print("inserting 1...")
    base.insert(1)
    print("contains:")
    base.contains()
    print()
    print("inserting 5...")
    base.insert(5)
    print("contains:")
    base.contains()
    print()
    print("removing 1...")
    base.remove(1)
    print("contains:")
    base.contains()
    print()
    print("removing 5...")
    base.remove(5)
    print("contains:")
    base.contains()
    print()
    print("removing 0...")
    base.remove(0)
    print("contains:")
    base.contains()
    print()
if __name__ == "__main__":
    test()