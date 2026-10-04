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
        if pos == self.tail:
            self.tail = new_node
    def append(self, x):
        new_node = Node(x)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.nxt = new_node
            self.tail = new_node
    def search(self, x):
        cur = self.head
        while cur:
            if cur.val == x:
                return cur
            cur = cur.nxt
        return False
    def print_list(self):
        cur = self.head
        while cur:
            print(cur.val)
            cur = cur.nxt
    def findpos(self, x):
        new_node = Node(x)
        if not self.head or self.head.val > x:
            new_node.nxt = self.head
            self.head = new_node
            if not self.tail:
                self.tail = new_node
            return
        cur = self.head
        while cur.nxt and cur.nxt.val < x:
            cur = cur.nxt
        new_node.nxt = cur.nxt
        cur.nxt = new_node
        if not new_node.nxt:
            self.tail = new_node
    def reverse(self):
        prev = None
        cur = self.head
        self.tail = self.head
        while cur:
            nxt = cur.nxt
            cur.nxt = prev
            prev = cur
            cur = nxt
        self.head = prev
    def insert_head(self, x):
        new_node = Node(x)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.nxt = self.head
            self.head = new_node
    def remove(self):
        if not self.head:
            print("empty")
            return None
        removed_node = self.head
        self.head = self.head.nxt
        if not self.head:
            self.tail = None
        removed_node.nxt = None
        return removed_node
def main():
    linked_list = LinkedList()
    linked_list.insert_head(1)
    linked_list.findpos(3)
    linked_list.print_list()
    print("Tail:", linked_list.tail.val if linked_list.tail else None)
    for _ in range(5):
        linked_list.remove()
if __name__ == "__main__":
    main()