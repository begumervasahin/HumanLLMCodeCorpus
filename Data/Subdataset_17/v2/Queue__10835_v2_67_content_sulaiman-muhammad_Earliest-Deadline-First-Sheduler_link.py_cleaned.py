class Node:
    def __init__(self, val=None, nxt=None):
        self.val = val
        self.nxt = nxt
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    def insert(self, x, pos):
        new_node = Node(x)
        new_node.nxt = pos.nxt
        pos.nxt = new_node
    def append(self, x):
        new_node = Node(x)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.nxt = new_node
            self.tail = new_node
    def search(self, x):
        cur = self.head
        while cur and cur.val != x:
            cur = cur.nxt
        return cur if cur else False
    def print_list(self):
        cur = self.head
        while cur:
            print(cur.val)
            cur = cur.nxt
    def findpos(self, x):
        new_node = Node(x)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return
        if self.head.val > x:
            new_node.nxt = self.head
            self.head = new_node
            return
        cur = self.head
        while cur.nxt and cur.nxt.val < x:
            cur = cur.nxt
        new_node.nxt = cur.nxt
        cur.nxt = new_node
        if new_node.nxt is None:
            self.tail = new_node
    def reverse(self):
        prev = None
        cur = self.head
        while cur:
            nxt = cur.nxt
            cur.nxt = prev
            prev = cur
            cur = nxt
        self.head = prev
    def insert_head(self, x):
        new_node = Node(x)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.nxt = self.head
            self.head = new_node
    def remove(self):
        if self.head is None:
            print("empty")
            return None
        removed_node = self.head
        self.head = self.head.nxt
        if self.head is None:
            self.tail = None
        removed_node.nxt = None
        return removed_node
def main():
    l = LinkedList()
    l.insert_head(1)
    l.findpos(3)
    l.print_list()
    print("Tail:", l.tail.val if l.tail else None)
    l.remove()
    l.remove()
    l.remove()
    l.remove()
    l.remove()
if __name__ == "__main__":
    main()