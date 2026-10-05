class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class SinglyLinkedList:
    def __init__(self):
        self.head = None
    def add(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
    def delete(self, data):
        current = self.head
        if current and current.data == data:
            self.head = current.next
            return
        while current:
            if current.data == data:
                break
            prev = current
            current = current.next
        if current:
            prev.next = current.next
            del current
    def __str__(self):
        if not self.head:
            return "Empty"
        result = ""
        current = self.head
        while current:
            result += str(current.data) + " -> "
            current = current.next
        return result[:-4]
def reverse_list(lst):
    l = SinglyLinkedList()
    for i in lst:
        l.add(i)
    print("Input list: ", l)
    curr_node = l.head
    prev_node = None
    next_node = None
    if curr_node:
        next_node = curr_node.next
    while curr_node:
        curr_node.next = prev_node
        prev_node = curr_node
        curr_node = next_node
        if curr_node:
            next_node = curr_node.next
    l.head = prev_node
    return l
def main():
    print('\nReverse and deleting in Singly Linked List \n')
    test_list0 = (1, 2, 3, 4, 5)
    returned_test0 = reverse_list(test_list0)
    print("Output list: ", returned_test0)
    print("Deleting 3")
    returned_test0.delete(3)
    print("Output list after delete: ", returned_test0)
    print('')
    test_list1 = ('org', 'com', 'her', 'him', 'blah')
    returned_test1 = reverse_list(test_list1)
    print("Output list: ", returned_test1)
    print("Deleting 'org'")
    returned_test1.delete('org')
    print("Output list after delete: ", returned_test1)
    print('')
    test_list2 = (1, 'com', 3, 'him', 5)
    returned_test2 = reverse_list(test_list2)
    print("Output list: ", returned_test2)
    print('')
    lp = SinglyLinkedList()
    lp.add('Fa')
    lp.add('la')
    lp.add('al')
    lp.add('ta')
    test_list3 = (1, 'com', lp, 'him', 5)
    returned_test3 = reverse_list(test_list3)
    print("Output list: ", returned_test3)
    print('')
    test_list4 = ('B',)
    returned_test4 = reverse_list(test_list4)
    print("Output list: ", returned_test4)
    print("Deleting 'B'")
    returned_test4.delete('B')
    print("Output list after delete: ", returned_test4)
    print('')
    test_list5 = ('B', 'B', 'B', 'B')
    returned_test5 = reverse_list(test_list5)
    print("Output list: ", returned_test5)
    print("Deleting 'B'")
    returned_test5.delete('B')
    print("Output list after delete: ", returned_test5)
    print('')
    test_list6 = ()
    returned_test6 = reverse_list(test_list6)
    print("Output list: ", returned_test6)
    print('')
if __name__ == "__main__":
    main()