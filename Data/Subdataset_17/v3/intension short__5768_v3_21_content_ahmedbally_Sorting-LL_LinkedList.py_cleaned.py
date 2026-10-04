class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    def get_data(self):
        return self.data
    def get_next(self):
        return self.next
    def set_next(self, new_next):
        self.next = new_next
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    def is_empty(self):
        return self.head is None
    def append(self, item):
        new_node = Node(item)
        new_node.set_next(self.head)
        self.head = new_node
        if self.tail is None:
            self.tail = new_node
        self.size += 1
    def append_sorted(self, item):
        new_node = Node(item)
        if self.is_empty() or self.tail.get_data() >= new_node.get_data():
            self._insert_at_end(new_node)
            return
        previous = None
        current = self.tail
        while current and current.get_data() <= new_node.get_data():
            previous = current
            current = current.get_next()
        new_node.set_next(current)
        if previous:
            previous.set_next(new_node)
        else:
            self.tail = new_node
        self.size += 1
    def _insert_at_end(self, new_node):
        new_node.set_next(self.tail)
        self.tail = new_node
        if self.head is None:
            self.head = new_node
        self.size += 1
    def length(self):
        return self.size
    def search(self, item):
        current = self.head
        while current:
            if current.get_data() == item:
                return True
            current = current.get_next()
        return False
    def remove(self, item):
        current = self.head
        previous = None
        while current:
            if current.get_data() == item:
                break
            previous = current
            current = current.get_next()
        if not current:
            return
        if previous is None:
            self.head = current.get_next()
        else:
            previous.set_next(current.get_next())
        if current == self.tail:
            self.tail = previous
        self.size -= 1
if __name__ == "__main__":
    linked_list = LinkedList()
    linked_list.append(10)
    linked_list.append(20)
    linked_list.append(30)
    print("Search for 20:", linked_list.search(20))
    print("Search for 40:", linked_list.search(40))
    linked_list.remove(20)
    print("Search for 20 after removal:", linked_list.search(20))
    print("Length of the list:", linked_list.length())
