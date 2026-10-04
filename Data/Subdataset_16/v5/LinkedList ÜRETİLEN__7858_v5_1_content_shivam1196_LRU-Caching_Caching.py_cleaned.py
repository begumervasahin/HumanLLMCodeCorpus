from caching.doublylinkedlist.DoublyLinkedList import DoublyLinkedList
from caching.node.HashNode import HashNode
class class1:
    def fonk1(self, b2):
        self.b1 = {}
        self.b2 = b2
        self.a1 = 0
        self.b3 = DoublyLinkedList()
    def fonk2(self, key):
        if key in self.b1:
            self.b3.access_node(self.b1[key])
            return self.b1[key].value
        else:
            print(-1)
            return -1
    def fonk3(self, key, value):
        if self.a1 < self.b2:
            self.b1[key] = self.b3.add_node(key, value)
            self.a1 += 1
        else:
            b4 = self.b3.get_head_node()
            del self.b1[b4.key]
            self.b1[key] = self.b3.replace_node(b4, key, value)
    def fonk4(self, key):
        return key % self.b2
    def fonk5(self):
        return self.a1
    def fonk6(self):
        self.b3.print_list()
if b5 = = "__main__":
    b1 = class1(5)
    b1.fonk3(1, 1)
    b1.fonk3(2, 2)
    b1.fonk3(3, 3)
    b1.fonk3(4, 4)
    b1.fonk3(5, 5)
    b1.fonk2(1)
    b1.fonk3(6, 6)
    b1.fonk3(7, 7)
    b1.fonk2(11)
    b1.fonk6()