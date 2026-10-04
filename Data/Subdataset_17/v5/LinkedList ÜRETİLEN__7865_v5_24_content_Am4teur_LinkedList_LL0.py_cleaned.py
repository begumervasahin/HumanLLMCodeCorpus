class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        else:
            current_node = self.head
            while current_node.next:
                current_node = current_node.next
            current_node.next = new_node
    def __iter__(self):
        current_node = self.head
        while current_node:
            yield current_node
            current_node = current_node.next
    def __str__(self):
        values = [str(node.value) for node in self]
        return ' -> '.join(values)
def main():
    ll = LinkedList()
    ll.append(0)
    ll.append(1)
    ll.append(2)
    print("Linked List:")
    print(ll)
if __name__ == "__main__":
    main()