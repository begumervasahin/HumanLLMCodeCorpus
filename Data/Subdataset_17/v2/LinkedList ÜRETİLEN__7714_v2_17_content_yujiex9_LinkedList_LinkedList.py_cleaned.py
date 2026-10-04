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
        cursor = self.head
        while cursor:
            if cursor == node:
                return True
            cursor = cursor.next_node
        return False
    def __len__(self):
        count = 0
        cursor = self.head
        while cursor:
            count += 1
            cursor = cursor.next_node
        return count
    def append(self, node):
        if not self.head:
            self.head = node
            return
        cursor = self.head
        while cursor.next_node:
            cursor = cursor.next_node
        cursor.next_node = node
    def insert(self, flag_node, node):
        if self.head == flag_node:
            node.next_node = self.head
            self.head = node
        else:
            cursor = self.head
            while cursor and cursor.next_node != flag_node:
                cursor = cursor.next_node
            if cursor:
                node.next_node = cursor.next_node
                cursor.next_node = node
    def delete(self, node):
        if self.head:
            if self.head == node:
                self.head = self.head.next_node
                return
            cursor = self.head
            while cursor.next_node and cursor.next_node != node:
                cursor = cursor.next_node
            if cursor.next_node:
                cursor.next_node = cursor.next_node.next_node
    def remove_duplicates(self):
        outer_cursor = self.head
        while outer_cursor:
            inner_cursor = outer_cursor
            while inner_cursor.next_node:
                if inner_cursor.next_node == outer_cursor:
                    inner_cursor.next_node = inner_cursor.next_node.next_node
                else:
                    inner_cursor = inner_cursor.next_node
            outer_cursor = outer_cursor.next_node
    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next_node
            current.next_node = prev
            prev = current
            current = next_node
        self.head = prev
    def print_list(self):
        cursor = self.head
        while cursor:
            print(cursor.value, end=' -> ')
            cursor = cursor.next_node
        print('None')
if __name__ == "__main__":
    linked_list = LinkedList()
    linked_list.append(Node(1))
    linked_list.append(Node(2))
    linked_list.append(Node(3))
    linked_list.insert(linked_list.head, Node(0))
    linked_list.insert(linked_list.head.next_node, Node(1.5))
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