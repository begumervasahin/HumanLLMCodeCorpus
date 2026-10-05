class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    def insert_after(self, new_value, position):
        new_node = Node(new_value)
        new_node.next_node = position.next_node
        position.next_node = new_node
    def append(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
        else:
            self.tail.next_node = new_node
        self.tail = new_node
    def search(self, value):
        current_node = self.head
        while current_node and current_node.value != value:
            current_node = current_node.next_node
        return current_node
    def print_list(self):
        current_node = self.head
        while current_node:
            print(current_node.value, end=" ")
            current_node = current_node.next_node
        print()
    def find_position_to_insert(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            self.tail = new_node
            return
        current_node = self.head
        if current_node.value > value:
            new_node.next_node = current_node
            self.head = new_node
            return
        while current_node.next_node and current_node.next_node.value < value:
            current_node = current_node.next_node
        new_node.next_node = current_node.next_node
        current_node.next_node = new_node
        if not new_node.next_node:
            self.tail = new_node
    def reverse(self):
        previous_node = None
        current_node = self.head
        while current_node:
            next_node = current_node.next_node
            current_node.next_node = previous_node
            previous_node = current_node
            current_node = next_node
        self.head = previous_node
    def insert_at_head(self, value):
        new_node = Node(value)
        new_node.next_node = self.head
        self.head = new_node
    def remove_head(self):
        if not self.head:
            print("List is empty")
            return None
        removed_node = self.head
        self.head = self.head.next_node
        if not self.head:
            self.tail = None
        return removed_node
def main():
    linked_list = LinkedList()
    linked_list.insert_at_head(1)
    linked_list.find_position_to_insert(3)
    linked_list.print_list()
    if linked_list.tail:
        print("Tail:", linked_list.tail.value)
    else:
        print("Tail: None")
    linked_list.remove_head()
    linked_list.remove_head()
if __name__ == "__main__":
    main()