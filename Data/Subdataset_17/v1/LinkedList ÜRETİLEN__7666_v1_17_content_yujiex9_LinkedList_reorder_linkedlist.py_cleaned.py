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
def locate_the_middle_node(ll):
    cursor, ds_cursor = ll.head, ll.head
    prev_cursor = None
    while ds_cursor and ds_cursor.next_node:
        prev_cursor = cursor
        cursor = cursor.next_node
        ds_cursor = ds_cursor.next_node.next_node
    prev_cursor.next_node = None
    return cursor
def reverse_second_half(middle_node):
    cursor = middle_node
    next_cursor = cursor.next_node
    cursor.next_node = None
    prev_cursor = cursor
    cursor = next_cursor
    while cursor.next_node:
        next_cursor = cursor.next_node
        cursor.next_node = prev_cursor
        prev_cursor = cursor
        cursor = next_cursor
    cursor.next_node = prev_cursor
    return cursor
def reorder_ori_list(ll, head_of_second_half):
    c1 = ll.head
    c2 = head_of_second_half
    while c1.next_node:
        tmp_node = c1.next_node
        c1.next_node = c2
        c1 = tmp_node
        tmp_node = c2.next_node
        c2.next_node = c1
        c2 = tmp_node
    c1.next_node = c2
if __name__ == "__main__":
    ll = LinkedList()
    for i in range(1, 10):
        ll.append(i)
    print("Original List:")
    ll.display()
    middle_node = locate_the_middle_node(ll)
    print("Middle Node:", middle_node.data)
    head_of_second_half = reverse_second_half(middle_node)
    print("Second Half Reversed:")
    temp_list = LinkedList()
    temp_list.head = head_of_second_half
    temp_list.display()
    reorder_ori_list(ll, head_of_second_half)
    print("Reordered List:")
    ll.display()