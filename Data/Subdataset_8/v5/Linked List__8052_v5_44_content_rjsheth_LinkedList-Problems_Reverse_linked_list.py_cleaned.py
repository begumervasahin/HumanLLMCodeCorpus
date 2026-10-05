from Singly_Linked_List import Singly_Linked_List
def reverse_list(input_list):
    linked_list = Singly_Linked_List()
    for item in input_list:
        linked_list.add(item)
    print("Input list:", linked_list)
    previous_node = None
    current_node = linked_list.head
    while current_node:
        next_node = current_node.next
        current_node.next = previous_node
        previous_node = current_node
        current_node = next_node
    linked_list.head = previous_node
    return linked_list
def test_reverse_list():
    print('\nReverse and deleting in Singly Linked List \n')
    test_list0 = (1, 2, 3, 4, 5)
    returned_test0 = reverse_list(test_list0)
    print("Output list:", returned_test0)
    print("Deleting 3")
    returned_test0.delete(3)
    print("Output list after delete:", returned_test0)
    print('')
    test_list1 = ('org', 'com', 'her', 'him', 'blah')
    returned_test1 = reverse_list(test_list1)
    print("Output list:", returned_test1)
    print("Deleting 'org'")
    returned_test1.delete('org')
    print("Output list after delete:", returned_test1)
    print('')
    test_list2 = (1, 'com', 3, 'him', 5)
    returned_test2 = reverse_list(test_list2)
    print("Output list:", returned_test2)
    print('')
    lp = Singly_Linked_List()
    lp.add('Fa')
    lp.add('la')
    lp.add('al')
    lp.add('ta')
    test_list3 = (1, 'com', lp, 'him', 5)
    returned_test3 = reverse_list(test_list3)
    print("Output list:", returned_test3)
    print('')
    test_list4 = ('B',)
    returned_test4 = reverse_list(test_list4)
    print("Output list:", returned_test4)
    print("Deleting 'B'")
    returned_test4.delete('B')
    print("Output list after delete:", returned_test4)
    print('')
    test_list5 = ('B', 'B', 'B', 'B')
    returned_test5 = reverse_list(test_list5)
    print("Output list:", returned_test5)
    print("Deleting 'B'")
    returned_test5.delete('B')
    print("Output list after delete:", returned_test5)
    print('')
    test_list6 = ()
    returned_test6 = reverse_list(test_list6)
    print("Output list:", returned_test6)
    print('')
if __name__ == "__main__":
    test_reverse_list()