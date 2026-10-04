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
        node = self.Node(item, prev_node=self.tail.prev_node, next_node=self.tail)
        self.tail.prev_node.next_node = node
        self.tail.prev_node = node
        self.count += 1
    def insert_first(self, item):
        node = self.Node(item, next_node=self.head.next_node, prev_node=self.head)
        self.head.next_node.prev_node = node
        self.head.next_node = node
        self.count += 1
    def get_first(self):
        return self.head.next_node.item if not self.is_empty() else "Linked List is empty!"
    def get_last(self):
        return self.tail.prev_node.item if not self.is_empty() else "Linked List is empty!"
    def size(self):
        return self.count
    def __str__(self):
        if self.is_empty():
            return "Linked List is empty!"
        else:
            items = []
            current_node = self.head.next_node
            while current_node != self.tail:
                items.append(str(current_node.item))
                current_node = current_node.next_node
            return ", ".join(items)
    def insert_into(self, item, index):
        if index < 0 or index > self.count:
            print("Attempted to insert element beyond the length of the list")
            return
        if index == 0:
            self.insert_first(item)
        elif index == self.count:
            self.insert_last(item)
        else:
            current_node = self.head.next_node
            for _ in range(index):
                current_node = current_node.next_node
            node = self.Node(item, prev_node=current_node.prev_node, next_node=current_node)
            current_node.prev_node.next_node = node
            current_node.prev_node = node
            self.count += 1
    def remove_first(self):
        if self.is_empty():
            print("List is empty! No elements to remove.")
        else:
            first_node = self.head.next_node
            self.head.next_node = first_node.next_node
            first_node.next_node.prev_node = self.head
            self.count -= 1
    def remove_last(self):
        if self.is_empty():
            print("List is empty! No elements to remove.")
        else:
            last_node = self.tail.prev_node
            self.tail.prev_node = last_node.prev_node
            last_node.prev_node.next_node = self.tail
            self.count -= 1
    def is_empty(self):
        return self.count == 0
if __name__ == "__main__":
    linked_list = LinkedList()
    linked_list.insert_first(1)
    linked_list.insert_last(2)
    linked_list.insert_last(3)
    linked_list.insert_into(4, 2)
    print(linked_list)
    linked_list.remove_first()
    print(linked_list)
    linked_list.remove_last()
    print(linked_list)
    print("First item:", linked_list.get_first())
    print("Last item:", linked_list.get_last())
    print("List count:", linked_list.size())