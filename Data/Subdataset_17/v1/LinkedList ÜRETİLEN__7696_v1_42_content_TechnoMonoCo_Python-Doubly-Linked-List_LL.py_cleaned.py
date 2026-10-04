class LL:
    def __init__(self, data=None, post=None, pred=None):
        self.data = data
        self.post = post
        self.pred = pred
    def remove(self, data):
        if self.pred is None:
            if self.data == data:
                if self.post is None:
                    self.data = None
                    return 0
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
                    self.pred.post = None
                    return 0
                else:
                    return -1
            else:
                if self.data == data:
                    self.pred.post = self.post
                    return 0
                else:
                    return self.post.remove(data)
    def insert(self, data):
        if data < self.data:
            hold = LL(data, self, None)
            if self.pred is None:
                self.data, hold.data = hold.data, self.data
                self.post, hold.post = hold.post, self.post
                self.pred = hold
            else:
                self.pred.post = hold
                self.pred = hold
        elif self.post is None:
            self.post = LL(data, None, self)
        else:
            self.post.insert(data)
    def contain(self, s):
        if self.data is None:
            print(s)
        else:
            s = s + ", " + str(self.data)
            if self.post is None:
                print(s)
            else:
                self.post.contain(s)
    def contains(self):
        if self.data is None:
            print("Empty.")
        elif self.post is None:
            print(self.data)
        else:
            self.post.contain(str(self.data))
def test():
    base = LL(0, None, None)
    print("contains...")
    base.contains()
    print("\ninserting 1...")
    base.insert(1)
    print("contains:")
    base.contains()
    print("\ninserting 5...")
    base.insert(5)
    print("contains:")
    base.contains()
    print("\nremoving 1...")
    base.remove(1)
    print("contains:")
    base.contains()
    print("\nremoving 5...")
    base.remove(5)
    print("contains...")
    base.contains()
    print("\nremoving 0...")
    base.remove(0)
    print("contains:")
    base.contains()
if __name__ == "__main__":
    test()