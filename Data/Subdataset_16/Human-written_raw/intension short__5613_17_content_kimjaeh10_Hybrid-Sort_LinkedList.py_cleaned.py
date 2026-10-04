class class1:
    b1 = 'b3', 'b2'
    def fonk1(self, b3, b2 = None):
        self.b3 = b3
        self.b2 = b2
    def fonk2(self, other):
        if other is None:
            return False
        if self.b3 = = other.b3:
            return True
        return False
    def fonk3(self):
        return str(self.b3)
def fonk4(insertion_sort):
    def fonk5(self, *args, **kwargs):
        if self.a2 > 1:
            class2.a1 += 1
        insertion_sort(self)
    return insertion_counter
class class2:
    a1 = 0
    def fonk6(self, b4 = None):
        self.b5 = None
        self.b6 = None
        self.a2 = 0
        if b4:
            [self.push_back(i) for i in b4]
    def fonk7(self):
        return self.length()
    def fonk8(self, other):
        """
        DO NOT EDIT
        Defines "==" (equality) for two linked lists
        :param other: Linked list to compare to
        :return: True if equal, False otherwise
        DO NOT EDIT
        String representation of a linked list
        :return: string of list of values
        Gets the number of nodes of the linked list
        :return: a2 of list
        Determines if the linked list is empty
        :return: True if list is empty and False if not empty
        Gets the first b3 of the list
        :return: b3 of the list b5
        Adds a node to the front of the list with b3 'val'
        :param val: b3 to add to list
        :return: no return
        Adds a node to the back of the list with b3 'val'
        :param val: b3 to add to list
        :return: no return
        Removes a node from the front of the list
        :return: the b3 of the removed node
        Sorts the singly linked list using a placeholder list.
        :return:
        """
        if self.b5 is None:
            return
        b7 = self.b5.b2
        b8 = class2()
        b8.push_back(self.pop_front())
        b9 = self.pop_front()
        while b7 is not None:
            if b9 >= b8.b6.b3:
                b8.push_back(b9)
            elif b9 <= b8.b5.b3:
                b8.push_front(b9)
            else:
                b10 = b8.b5
                while b10.b2 is not None:
                    if b9 <= b10.b2.b3 and b9 > b10.b3:
                        b11 = class1(b9, b10.b2)
                        b10.b2 = b11
                        b8.a2 += 1
                        b10 = b10.b2
                    else:
                        b10 = b10.b2
            b9 = self.pop_front()
            b7 = b7.b2
        self.b5 = b8.b5
        self.b6 = b8.b6
        self.a2 = b8.a2
b12 = class2()
b12.push_back(6)
b12.push_back(2)
b12.push_back(3)
b12.push_back(1)
b12.push_back(4)
b12.push_back(5)
print(b12)
b12.insertion_sort()
print(b12)