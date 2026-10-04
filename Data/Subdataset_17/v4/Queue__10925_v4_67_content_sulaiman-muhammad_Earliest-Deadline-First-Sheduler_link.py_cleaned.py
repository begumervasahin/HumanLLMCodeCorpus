class Node:
    def __init__(self, val=None, nxt=None):
        self.val = val
        self.nxt = nxt
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    def insert(self, x, pos):
        temp = Node(x)
        temp.nxt = pos.nxt
        pos.nxt = temp
    def append(self, x):
        temp = Node(x)
        if self.head is None:
            self.head = temp
            self.tail = temp
        else:
            self.tail.nxt = temp
            self.tail = temp
    def search(self, x):
        cur = self.head
        while cur is not None and cur.val != x:
            cur = cur.nxt
        return cur if cur is not None else False
    def print_list(self):
        cur = self.head
        while cur:
            print(cur.val)
            cur = cur.nxt
    def findpos(self, x):
        temp = Node(x)
        if self.head is None:
            self.head = temp
            self.tail = temp
        elif self.head.val.cpu > x.cpu:
            temp.nxt = self.head
            self.head = temp
        else:
            cur = self.head
            while cur.nxt is not None and cur.nxt.val.cpu < x.cpu:
                cur = cur.nxt
            temp.nxt = cur.nxt
            cur.nxt = temp
            if temp.nxt is None:
                self.tail = temp
    def reverse(self):
        prev = None
        cur = self.head
        while cur:
            nxt = cur.nxt
            cur.nxt = prev
            prev = cur
            cur = nxt
        self.head = prev
        self.print_list()
    def insert_head(self, x):
        temp = Node(x)
        if self.head is None:
            self.head = temp
            self.tail = temp
        else:
            temp.nxt = self.head
            self.head = temp
    def remove(self):
        if self.head is None:
            print("empty")
            return None
        temp = self.head
        self.head = self.head.nxt
        if self.head is None:
            self.tail = None
        temp.nxt = None
        return temp
def main():
    l = LinkedList()
    l.insert_head(1)
    l.findpos(Node(3))
    l.print_list()
    print("tail", l.tail.val)
    l.remove()
    l.remove()
    l.remove()
    l.remove()
if __name__ == "__main__":
    main()