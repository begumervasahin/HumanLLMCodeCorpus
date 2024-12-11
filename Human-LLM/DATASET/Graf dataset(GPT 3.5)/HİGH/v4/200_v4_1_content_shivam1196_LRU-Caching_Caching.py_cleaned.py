from b7.doublylinkedlist.DoublyLinkedList import DoublyLinkedList
from b7.b4.HashNode import HashNode
class class1:
    def fonk1(self, capacity):
        self.b1 = {}
        self.b2 = capacity
        self.a1 = 0
        self.b3 = DoublyLinkedList()
    def fonk2(self, key):
        if key in self.b1:
            self.b3.access_a_node(self.b1[key])
        else:
            print(-1)
    def fonk3(self, key, value):
        if self.a1 < self.b2:
            self.b1[key] = self.b3.enter_value(key, value)
            self.a1 += 1
        else:
            b4 = self.b3.get_head_node()
            del self.b1[b4.key]
            self.b1[key] = self.b3.replace_a_node(key, value)
    def fonk4(self, key):
        b5 = key % self.b2
        return b5
    def fonk5(self):
        return self.a1
    def fonk6(self):
        self.b3.print_doubly_linked_list()
if b6 = = "__main__":
    b7 = class1(5)
    b7.fonk3(1, 1)
    b7.fonk3(2, 2)
    b7.fonk3(3, 3)
    b7.fonk3(4, 4)
    b7.fonk3(5, 5)
    b7.fonk2(1)
    b7.fonk3(6, 6)
    b7.fonk3(7, 7)
    b7.fonk2(11)
    b7.fonk6()