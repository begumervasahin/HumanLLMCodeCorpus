class Node:
    def __init__(self, data):
        self.data = data
        self.next_node = None
class LinkedList:
    def __init__(self):
        self.head = None
    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next_node:
            last = last.next_node
        last.next_node = new_node
    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> " if current.next_node else "\n")
            current = current.next_node
def locate_middle_node(linked_list):
    slow_ptr = linked_list.head
    fast_ptr = linked_list.head
    prev_ptr = None
    while fast_ptr and fast_ptr.next_node:
        prev_ptr = slow_ptr
        slow_ptr = slow_ptr.next_node
        fast_ptr = fast_ptr.next_node.next_node
    if prev_ptr:
        prev_ptr.next_node = None
    return slow_ptr
def reverse_list(head):
    prev = None
    current = head
    while current:
        next_node = current.next_node
        current.next_node = prev
        prev = current
        current = next_node
    return prev
def reorder_list(first_half, second_half):
    first_half_ptr = first_half.head
    second_half_ptr = second_half
    while first_half_ptr and second_half_ptr:
        first_half_next = first_half_ptr.next_node
        second_half_next = second_half_ptr.next_node
        first_half_ptr.next_node = second_half_ptr
        if first_half_next:
            second_half_ptr.next_node = first_half_next
        first_half_ptr = first_half_next
        second_half_ptr = second_half_next
if __name__ == "__main__":
    linked_list = LinkedList()
    for i in range(1, 10):
        linked_list.append(i)
    print("Original List:")
    linked_list.display()
    middle_node = locate_middle_node(linked_list)
    print("Middle Node:", middle_node.data)
    second_half_head = reverse_list(middle_node)
    print("Second Half Reversed:")
    temp_list = LinkedList()
    temp_list.head = second_half_head
    temp_list.display()
    reorder_list(linked_list, second_half_head)
    print("Reordered List:")
    linked_list.display()