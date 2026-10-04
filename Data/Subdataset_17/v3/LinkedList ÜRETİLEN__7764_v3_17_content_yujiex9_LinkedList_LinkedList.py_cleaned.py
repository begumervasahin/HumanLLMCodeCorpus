class Node:
    def __init__(self, value):
        self.value = value
        self.next_node = None
    def __eq__(self, other):
        return self.value == other.value if other else False
class LinkedList:
    def __init__(self):
        self.head = None
    def __contains__(self, node):
        current = self.head
        while current:
            if current == node:
                return True
            current = current.next_node
        return False
    def __len__(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next_node
        return count
    def append(self, node):
        if not self.head:
            self.head = node
            return
        current = self.head
        while current.next_node:
            current = current.next_node
        current.next_node = node
    def insert_after(self, target_node, new_node):
        if not self.head:
            print("List is empty")
            return
        current = self.head
        while current and current != target_node:
            current = current.next_node
        if current:
            new_node.next_node = current.next_node
            current.next_node = new_node
    def delete(self, target_node):
        if not self.head:
            return
        if self.head == target_node:
            self.head = self.head.next_node
            return
        current = self.head
        while current.next_node and current.next_node != target_node:
            current = current.next_node
        if current.next_node:
            current.next_node = current.next_node.next_node
    def remove_duplicates(self):
        current = self.head
        while current:
            runner = current
            while runner.next_node:
                if runner.next_node == current:
                    runner.next_node = runner.next_node.next_node
                else:
                    runner = runner.next_node
            current = current.next_node
    def reverse(self):
        previous = None
        current = self.head
        while current:
            next_node = current.next_node
            current.next_node = previous
            previous = current
            current = next_node
        self.head = previous
    def print_list(self):
        current = self.head
        while current:
            print(current.value, end=' -> ')
            current = current.next_node
        print('None')
if __name__ == "__main__":
    linked_list = LinkedList()
    linked_list.append(Node(1))
    linked_list.append(Node(2))
    linked_list.append(Node(3))
    linked_list.insert_after(linked_list.head, Node(0))
    linked_list.insert_after(linked_list.head.next_node, Node(1.5))
    print("List after insertions:")
    linked_list.print_list()
    linked_list.append(Node(2))
    linked_list.remove_duplicates()
    print("List after removing duplicates:")
    linked_list.print_list()
    linked_list.reverse()
    print("List after reversing:")
    linked_list.print_list()
    linked_list.delete(Node(1.5))
    print("List after deleting node with value 1.5:")
    linked_list.print_list()
    print(f"Length of list: {len(linked_list)}")
    print(f"Node with value 2 in list: {Node(2) in linked_list}")
    print(f"Node with value 4 in list: {Node(4) in linked_list}")