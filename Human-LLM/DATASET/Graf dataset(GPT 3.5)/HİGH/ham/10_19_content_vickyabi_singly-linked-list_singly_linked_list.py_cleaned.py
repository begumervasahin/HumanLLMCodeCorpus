class class1:
    def fonk1(self,b1):
        self.b1 = b1
        self.b2 = None
class class2:
    def fonk2(self):
        self.b3 = None
    def fonk3(self,b1):
        b4 = class1(b1)
        if self.b3 is None:
            self.b3 = b4
        else:
            b4.b2 = self.b3
            self.b3 = b4
    def fonk4(self,b1,b9):
        b4 = class1(b1)
        b5 = self.b3
        if self.b3 = =None:
            print("list is empty")
        else:
            while b5.b2 != None:
                if b5.b1 = =b9:
                   break
                b5 = b5.b2
            b4.b2 = b5.b2
            b5.b2 = b4
    def fonk5(self,b1):
        b4 = class1(b1)
        if self.b3 is None:
            self.b3 = b4
        else:
            b5 = self.b3
            while True:
                if b5.b2 is None:
                    break
                b5 = b5.b2
            b5.b2 = b4
    def fonk6(self):
        b6 = self.b3
        while True:
            if b6 is None:
                break
            print(b6.b1)
            b6 = b6.b2
b7 = class2()
while True:
    print("1.insert at beginnig \n2.insert at position \n3.insert at end \n4.display list")
    b8 = int(input("enter your choice:"))
    if b8 = =1:
        b1 = input("enter the element to insert:")
        b7.fonk3(b1)
    elif b8 = =2:
        b1 = input("enter the element to insert:")
        b9 = input("enter the element after insertion:")
        b7.fonk4(b1,b9)
    elif b8 = =3:
        b1 = input("enter the element to insert:")
        b7.fonk5(b1)
    elif b8 = =4:
        b7.fonk6()
    else:
        print("invalid input")