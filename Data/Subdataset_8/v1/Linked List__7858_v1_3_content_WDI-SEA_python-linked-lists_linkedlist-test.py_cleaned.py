class ListNode:
    def __init__(self, data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
    def insert_in_front(self, data):
        new_node = ListNode(data)
        new_node.next = self.head
        self.head = new_node
    def insert_at_end(self, data):
        new_node = ListNode(data)
        if not self.head:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node
    def remove_last(self):
        if not self.head:
            return False
        if not self.head.next:
            self.head = None
            return True
        second_last = self.head
        while second_last.next.next:
            second_last = second_last.next
        second_last.next = None
        return True
    def insert_at_index(self, data, index=0):
        if index == 0:
            self.insert_in_front(data)
            return
        new_node = ListNode(data)
        current = self.head
        for _ in range(index - 1):
            if current is None:
                raise IndexError("Index out of range")
            current = current.next
        new_node.next = current.next
        current.next = new_node
    def remove_at_index(self, index=None):
        if not self.head:
            return False
        if index is None:
            return False
        if index == 0:
            self.head = self.head.next
            return True
        current = self.head
        for _ in range(index - 1):
            if current.next is None:
                raise IndexError("Index out of range")
            current = current.next
        if current is None or current.next is None:
            raise IndexError("Index out of range")
        current.next = current.next.next
        return True
    def is_empty(self):
        return self.head is None
    def __len__(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count
    def __str__(self):
        result = "["
        current = self.head
        while current:
            result += str(current.data)
            current = current.next
            if current:
                result += " -> "
        result += "]"
        return result
if __name__ == "__main__":
    linked_list = LinkedList()
    print(linked_list.is_empty())
    linked_list.insert_in_front(1)
    linked_list.insert_at_end(2)
    linked_list.insert_at_end(3)
    print(linked_list)
    print(len(linked_list))
    linked_list.remove_last()
    print(linked_list)
    print(len(linked_list))
    linked_list.insert_at_index(4, 1)
    print(linked_list)
    print(len(linked_list))
    linked_list.remove_at_index(1)
    print(linked_list)
    print(len(linked_list))
    print(linked_list.is_empty())
