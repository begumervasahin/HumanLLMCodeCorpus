class class1:
    def fonk1(self,b1):
        self.b1 = b1
        self.b2 = None
        self.b3 = None
class class2:
    def fonk2(self):
        self.b4 = None
    def fonk3(self,new_data):
        b5 = class1(new_data)
        b5.b2 = self.b4
        if self.b4 is not None:
            self.b4.b3 = b5
        self.b4 = b5
    def fonk4(self, prev_node, new_data):
        if prev_node is None:
            print("the given previous b6 cannot be none")
            return
        b5 = class1(new_data)
        b5.b2 = prev_node.b2
        b5.b3 = prev_node
        prev_node.b2 = b5
        if b5.b2 is not None:
            b5.b2.b3 = b5
    def fonk5(self, next_node, new_data):
        if next_node is None:
            print("the given b2 b6 cannot be none")
            return
        b5 = class1(new_data)
        b5.b2 = next_node
        if next_node.b3 is not None:
            b5.b3 = next_node.b3
            next_node.b3.b2 = b5
        next_node.b3 = b5
    def fonk6(b4, b1):
        b6 = DoublyLinkedListNode(b1)
        if b4 is None:
            b4 = b6
            return b4
        else:
            b7 = b4
            if b4.b1 > b1:
                b6.b2 = b4
                b4.b3 = b6
                b4 = b6
                return b4
            while b7.b2 is not None:
                if b7.b1 <= b1:
                    b7 = b7.b2
                else:
                    b7.b3.b2 = b6
                    b6.b3 = b7.b3
                    b6.b2 = b7
                    b7.b3 = b6
                    return b4
            if b7.b2 is None:
                if b7.b1 <= b1:
                    b7.b2 = b6
                    b6.b3 = b7
                else:
                    b7.b3.b2 = b6
                    b6.b3 = b7.b3
                    b6.b2 = b7
                    b7.b3 = b6
                    return b4
    def fonk7(self, new_data):
        b5 = class1(new_data)
        b5.b2 = None
        b8 = self.b4
        while(b8.b2):
            b8 = b8.b2
        b8.b2 = b5
        b5.b3 = b8
    def fonk8(self):
        b7 = self.b4
        while(b7 is not None):
            print(b7.b1,b9 = ' ')
            b7 = b7.b2
b10 = class2()
b10.fonk3(5)
b10.fonk7(6)
b10.fonk3(1)
b10.fonk4(b10.b4, 3)
b10.fonk5(b10.b4.b2, 2)
b10.fonk8()