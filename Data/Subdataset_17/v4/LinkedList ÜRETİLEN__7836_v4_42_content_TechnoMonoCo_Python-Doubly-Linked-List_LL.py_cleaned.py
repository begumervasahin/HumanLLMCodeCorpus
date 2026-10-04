class Node:
    def __init__(self, data=None, post=None, pred=None):
        self.data = data
        self.post = post
        self.pred = pred
    def remove(self, data):
        if self.pred is None:
            if self.data == data:
                if self.post is None:
                    self.data = None
                else:
                    hold = self.post
                    self.data = self.post.data
                    self.post = self.post.post
                    del hold
                return 0
            elif self.post is None:
                return -1
            else:
                return self.post.remove(data)
        else:
            if self.post is None:
                if self.data == data:
                    hold = self
                    temp = self.pred
                    temp.post = None
                    del hold
                    return 0
                else:
                    return -1
            else:
                if self.data == data:
                    hold = self
                    temp = self.pred
                    temp.post = self.post
                    del hold
                    return 0
                else:
                    return self.post.remove(data)
    def insert(self, data):
        if data < self.data:
            new_node = Node(data, self, self.pred)
            if self.pred:
                self.pred.post = new_node
            self.pred = new_node
        elif self.post is None:
            new_node = Node(data, None, self)
            self.post = new_node
        else:
            self.post.insert(data)
    def contain(self, s):
        if self.data is not None:
            s += ", " + str(self.data)
        if self.post is None:
            print(s)
        else:
            self.post.contain(s)
    def contains(self):
        if self.post is None:
            if self.data is None:
                print("Empty.")
            else:
                print(self.data)
        else:
            self.post.contain(str(self.data))
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