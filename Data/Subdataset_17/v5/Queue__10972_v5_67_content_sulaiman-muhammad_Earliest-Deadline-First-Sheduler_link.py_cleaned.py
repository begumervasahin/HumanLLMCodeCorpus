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
        current = self.head
        while current is not None and current.val != x:
            current = current.nxt
        return current
    def print_list(self):
        current = self.head
        while current:
            print(current.val)
            current = current.nxt
    def findpos(self, node):
        if self.head is None:
            self.head = node
            self.tail = node
        elif self.head.val.cpu > node.val.cpu:
            node.nxt = self.head
            self.head = node
        else:
            current = self.head
            while current.nxt is not None and current.nxt.val.cpu < node.val.cpu:
                current = current.nxt
            node.nxt = current.nxt
            current.nxt = node
            if node.nxt is None:
                self.tail = node
    def reverse(self):
        prev = None
        current = self.head
        while current:
            nxt = current.nxt
            current.nxt = prev
            prev = current
            current = nxt
        self.head = prev
        self.print_list()
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
    l.findpos(Node({'cpu': 3}))
    l.print_list()
    print("tail", l.tail.val)
    l.remove()
    l.remove()
    l.remove()
    l.remove()
if __name__ == "__main__":
    main()