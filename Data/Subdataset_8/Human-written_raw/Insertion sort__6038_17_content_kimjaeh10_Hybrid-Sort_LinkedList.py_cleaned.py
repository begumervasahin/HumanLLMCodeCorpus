class Node:
    __slots__ = 'value', 'next_node'
    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node
    def __eq__(self, other):
        if other is None:
            return False
        if self.value == other.value:
            return True
        return False
    def __repr__(self):
        return str(self.value)
def _insertion_wrapper(insertion_sort):
    def insertion_counter(self, *args, **kwargs):
        if self.size > 1:
            LinkedList._c += 1
        insertion_sort(self)
    return insertion_counter
class LinkedList:
    _c = 0
    def __init__(self, data=None):
        self.head = None
        self.tail = None
        self.size = 0
        if data:
            [self.push_back(i) for i in data]
    def __len__(self):
        return self.length()
    def __eq__(self, other):
        """
        DO NOT EDIT
        Defines "==" (equality) for two linked lists
        :param other: Linked list to compare to
        :return: True if equal, False otherwise
        DO NOT EDIT
        String representation of a linked list
        :return: string of list of values
        Gets the number of nodes of the linked list
        :return: size of list
        Determines if the linked list is empty
        :return: True if list is empty and False if not empty
        Gets the first value of the list
        :return: value of the list head
        Adds a node to the front of the list with value 'val'
        :param val: value to add to list
        :return: no return
        Adds a node to the back of the list with value 'val'
        :param val: value to add to list
        :return: no return
        Removes a node from the front of the list
        :return: the value of the removed node
        Sorts the singly linked list using a placeholder list.
        :return:
        """
        if self.head is None:
            return
        pointer = self.head.next_node
        sortedlist = LinkedList()
        sortedlist.push_back(self.pop_front())
        h = self.pop_front()
        while pointer is not None:
            if h >= sortedlist.tail.value:
                sortedlist.push_back(h)
            elif h <= sortedlist.head.value:
                sortedlist.push_front(h)
            else:
                new_head = sortedlist.head
                while new_head.next_node is not None:
                    if h <= new_head.next_node.value and h > new_head.value:
                        temp = Node(h, new_head.next_node)
                        new_head.next_node = temp
                        sortedlist.size += 1
                        new_head = new_head.next_node
                    else:
                        new_head = new_head.next_node
            h = self.pop_front()
            pointer = pointer.next_node
        self.head = sortedlist.head
        self.tail = sortedlist.tail
        self.size = sortedlist.size
list5 = LinkedList()
list5.push_back(6)
list5.push_back(2)
list5.push_back(3)
list5.push_back(1)
list5.push_back(4)
list5.push_back(5)
print(list5)
list5.insertion_sort()
print(list5)