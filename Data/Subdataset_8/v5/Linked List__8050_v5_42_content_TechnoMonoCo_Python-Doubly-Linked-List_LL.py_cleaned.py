class LinkedListNode:
    def __init__(self, data, post=None, pred=None):
        self.data = data
        self.post = post
        self.pred = pred
    def remove(self, data):
        if self.data == data:
            if self.pred is None:
                if self.post:
                    self.data = self.post.data
                    self.post = self.post.post
                else:
                    self.data = None
                return 0
            elif self.post is None:
                self.pred.post = None
                return 0
            else:
                self.pred.post = self.post
                return 0
        elif self.post:
            return self.post.remove(data)
        else:
            return -1
    def insert(self, data):
        if data < self.data:
            hold = LinkedListNode(data, self, None)
            self = hold
        elif self.post is None:
            hold = LinkedListNode(data, None, self)
            self.post = hold
        else:
            self.post.insert(data)
    def contains(self):
        current = self
        if current.data is None:
            print("Empty.")
        else:
            while current:
                print(current.data, end=", ")
                current = current.post
            print()
def test():
    base = LinkedListNode(0)
    print("contains...")
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
    print("contains...")
    base.contains()
    print()
    print("removing 0...")
    base.remove(0)
    print("contains:")
    base.contains()
    print()
test()