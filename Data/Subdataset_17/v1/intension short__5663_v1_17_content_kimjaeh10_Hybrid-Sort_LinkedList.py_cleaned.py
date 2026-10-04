class Node:
    __slots__ = 'value', 'next_node'
    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node
    def __eq__(self, other):
        if other is None:
            return False
        return self.value == other.value
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
            for i in data:
                self.push_back(i)
    def __len__(self):
        return self.length()
    def __eq__(self, other):
        """
        Defines "==" (equality) for two linked lists.
        :param other: Linked list to compare to.
        :return: True if equal, False otherwise.
        String representation of a linked list.
        :return: String of list of values.
        Gets the number of nodes of the linked list.
        :return: Size of list.
        Determines if the linked list is empty.
        :return: True if list is empty, False if not empty.
        Gets the first value of the list.
        :return: Value of the list head.
        Adds a node to the front of the list with value 'val'.
        :param val: Value to add to list.
        :return: No return.
        Adds a node to the back of the list with value 'val'.
        :param val: Value to add to list.
        :return: No return.
        Removes a node from the front of the list.
        :return: The value of the removed node.
        Sorts the singly linked list using a placeholder list.
        :return: No return.
        """
        if self.head is None:
            return
        sorted_list = LinkedList()
        sorted_list.push_back(self.pop_front())
        while self.head is not None:
            h = self.pop_front()
            if h >= sorted_list.tail.value:
                sorted_list.push_back(h)
            elif h <= sorted_list.head.value:
                sorted_list.push_front(h)
            else:
                current = sorted_list.head
                while current.next_node is not None:
                    if h <= current.next_node.value and h > current.value:
                        new_node = Node(h, current.next_node)
                        current.next_node = new_node
                        sorted_list.size += 1
                        break
                    current = current.next_node
        self.head = sorted_list.head
        self.tail = sorted_list.tail
        self.size = sorted_list.size
if __name__ == "__main__":
    list5 = LinkedList()
    list5.push_back(6)
    list5.push_back(2)
    list5.push_back(3)
    list5.push_back(1)
    list5.push_back(4)
    list5.push_back(5)
    print("Before sorting:", list5)
    list5.insertion_sort()
    print("After sorting:", list5)