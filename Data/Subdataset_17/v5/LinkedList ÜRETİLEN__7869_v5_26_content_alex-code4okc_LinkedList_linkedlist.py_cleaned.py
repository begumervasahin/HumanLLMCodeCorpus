class LinkedList:
    class Node:
        def __init__(self, item, prev_node=None, next_node=None):
            self.item = item
            self.prev_node = prev_node
            self.next_node = next_node
    def __init__(self):
        self.head = self.Node(None)
        self.tail = self.Node(None)
        self.head.next_node = self.tail
        self.tail.prev_node = self.head
        self.count = 0
    def insert_last(self, item):
        node = self.Node(item)
        last = self.tail.prev_node
        last.next_node = node
        node.prev_node = last
        node.next_node = self.tail
        self.tail.prev_node = node
        self.count += 1
    def insert_first(self, item):
        node = self.Node(item)
        first = self.head.next_node
        self.head.next_node = node
        node.prev_node = self.head
        node.next_node = first
        first.prev_node = node
        self.count += 1
    def get_first(self):
        if self.is_empty():
            return "Linked List is empty!"
        return self.head.next_node.item
    def get_last(self):
        if self.is_empty():
            return "Linked List is empty!"
        return self.tail.prev_node.item
    def size(self):
        return self.count
    def __str__(self):
        if self.is_empty():
            return "Linked List is empty!"
        else:
            accumulator = []
            current_node = self.head.next_node
            while current_node != self.tail:
                accumulator.append(str(current_node.item))
                current_node = current_node.next_node
            return ", ".join(accumulator)
    def insert_into(self, item, index):
        if self.is_empty():
            self.insert_last(item)
        elif index == 0:
            self.insert_first(item)
        elif index == -1 or index == self.count:
            self.insert_last(item)
        elif index < self.count:
            node = self.Node(item)
            current_node = self.head.next_node
            for _ in range(index):
                current_node = current_node.next_node
            prev_node = current_node.prev_node
            prev_node.next_node = node
            node.prev_node = prev_node
            node.next_node = current_node
            current_node.prev_node = node
            self.count += 1
        else:
            print("Attempted to insert element beyond the length of the list")
    def remove_first(self):
        if self.is_empty():
            print("List is empty! No elements to remove.")
        else:
            first = self.head.next_node
            second = first.next_node
            self.head.next_node = second
            second.prev_node = self.head
            first.next_node = None
            first.prev_node = None
            self.count -= 1
    def remove_last(self):
        if self.is_empty():
            print("List is empty! No elements to remove.")
        else:
            last = self.tail.prev_node
            second_last = last.prev_node
            self.tail.prev_node = second_last
            second_last.next_node = self.tail
            last.next_node = None
            last.prev_node = None
            self.count -= 1
    def is_empty(self):
        return self.count == 0
if __name__ == "__main__":
    ll = LinkedList()
    ll.insert_last(1)
    ll.insert_last(2)
    ll.insert_first(0)
    print(ll)
    ll.insert_into(1.5, 2)
    print(ll)
    ll.remove_first()
    print(ll)
    ll.remove_last()
    print(ll)
