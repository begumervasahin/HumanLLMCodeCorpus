class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    def is_empty(self):
        return self.head is None
    def append(self, item):
        new_node = Node(item)
        new_node.next = self.head
        if self.head is None:
            self.tail = new_node
        self.head = new_node
        self.size += 1
    def append_sorted(self, new_node):
        new_node.next = None
        current = self.tail
        previous = None
        data = new_node.data
        while current is not None:
            if current.data > data:
                break
            previous = current
            current = current.next
        if previous is None:
            new_node.next = self.tail
            self.tail = new_node
        else:
            new_node.next = current
            previous.next = new_node
    def length(self):
        current = self.head
        count = 0
        while current is not None:
            count += 1
            current = current.next
        return count
    def search(self, item):
        current = self.head
        while current is not None:
            if current.get_data() == item:
                return True
            current = current.next
        return False
    def remove(self, item):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.get_data() == item:
                found = True
            else:
                previous = current
                current = current.get_next()
        if previous is None:
            self.head = current.get_next()
        else:
            previous.set_next(current.get_next())
        self.size -= 1