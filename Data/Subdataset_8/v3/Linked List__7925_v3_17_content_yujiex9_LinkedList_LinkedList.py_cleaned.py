class Node:
    def __init__(self, value):
        self.value = value
        self.next_node = None
    def __eq__(self, other):
        return self.value == other.value
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
        else:
            current = self.head
            while current.next_node:
                current = current.next_node
            current.next_node = node
    def insert_after(self, target_node, new_node):
        if self.head == target_node:
            new_node.next_node = self.head
            self.head = new_node
        else:
            current = self.head
            while current:
                if current == target_node:
                    new_node.next_node = current.next_node
                    current.next_node = new_node
                    break
                current = current.next_node
    def delete(self, target_node):
        if self.head == target_node:
            self.head = self.head.next_node
        else:
            prev_node = self.head
            while prev_node.next_node:
                if prev_node.next_node == target_node:
                    prev_node.next_node = prev_node.next_node.next_node
                    break
                prev_node = prev_node.next_node
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
        prev_node = None
        current = self.head
        while current:
            next_node = current.next_node
            current.next_node = prev_node
            prev_node = current
            current = next_node
        self.head = prev_node
    def print_list(self):
        current = self.head
        while current:
            print(current.value)
            current = current.next_node
if __name__ == "__main__":
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node5 = Node(5)
    linked_list = LinkedList()
    linked_list.append(node1)
    linked_list.append(node2)
    linked_list.append(node3)
    linked_list.append(node4)
    linked_list.append(node5)
    print("Initial List:")
    linked_list.print_list()
    print()
    new_node = Node(0)
    linked_list.insert_after(node1, new_node)
    print("List after inserting a new node:")
    linked_list.print_list()
    print()
    linked_list.delete(new_node)
    print("List after deleting the new node:")
    linked_list.print_list()
    print()
    linked_list.remove_duplicates()
    print("List after removing duplicates:")
    linked_list.print_list()
    print()
    linked_list.reverse()
    print("Reversed List:")
    linked_list.print_list()
    print()