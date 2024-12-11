from Node import Node
class class1:
    def fonk1(self):
        self.b1 = None
    def fonk2(self):
        return self.b1 = =None
    def fonk3(self,b8):
        b2 = Node(b8)
        b2.setNext(self.b1)
        self.b1 = b2
    def fonk4(self):
        b3 = self.b1
        a1 = 0
        while b3 != None:
            a1 = a1+1
            b3 = b3.getNext()
        return a1
    def fonk5(self,b8):
        b3 = self.b1
        while b3 != None:
            if b3.getData()==b8:
                return True
            else :
                b3 = b3.getNext()
        return False
    def fonk6(self,b8):
        b3 = self.b1
        b4 = None
        b5 = False
        while not b5:
            if b3.getData()==b8:
                b5 = True
                b4.setNext(b3.getNext())
            else:
                b4 = b3
                b3 = b3.getNext()
        if b4 = =None:
                self.b1 = b3.getNext()
        else:
            b4.setnext(b3.getnext())
    def fonk7(self):
        b3 = self.b1
        while b3.getNext()!=None:
            b6 = b3
            b7 = b3.getData()
            b8 = b3.getNext()
            while b8 !=None:
                if b7>b8.getData():
                    b7 = b8.getData()
                    b6 = b8
                b8 = b8.getNext()
            b6.setData(b3.getData())
            b3.setData(b7)
            b3 = b3.getNext()
    def fonk8(self):
            print(self.b1.getData())
            b9 = self.b1.getNext()
            print(b9.getData())
            print(b9.getNext().getData())
    def fonk9(self):
        b3 = self.b1
        while b3 !=None:
            print(b3.getData())
            b3 = b3.getNext()