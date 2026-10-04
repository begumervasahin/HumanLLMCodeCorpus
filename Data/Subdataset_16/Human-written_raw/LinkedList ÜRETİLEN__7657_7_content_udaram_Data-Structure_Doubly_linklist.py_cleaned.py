class class1:
    def fonk1(self,b1):
        self.b1 = b1
        self.b2 = None
        self.b3 = None
class class2:
    def fonk2(self):
        self.b4 = None
        self.b5 = None
    def fonk3(self,b1):
        b6 = class1(b1)
        if self.b4 is None:
            self.b4 = self.b5=b6
        else:
            self.b5.b2 = b6
            b6.b3 = self.b5
            self.b5 = b6
    def fonk4(self,b1):
        b6 = class1(b1)
        if self.b4 is None:
            self.b4 = self.b5=b6
        else :
            b6.b2 = self.b4
            self.b4.b3 = b6
            self.b4 = b6
    def fonk5(self,b8,b1):
        b6 = class1(b1)
        b7 = self.b4
        a1 = 0
        if b8 = =0:
            self.fonk4(b1)
        else:
            while b7!=None and b8-1!=a1:
                a1+=1
                b7 = b7.b2
            if b7 is None and b8>a1 :
                print("INVALID POSITION")
            else:
                b6.b3 = b7
                b6.b2 = b7.b2
                b7.b2.b3 = b6
                b7.b2 = b6
    def fonk6(self):
        b7 = self.b4
        print("\nDoubly Link list is:::",b9 = "")
        if b7 is None:
            print("Empty!!!!")
        while b7 is not None:
            print("<=> ",b7.b1,b9 = " ")
            b7 = b7.b2
    def fonk7(self):
        b7 = self.b5
        if b7 is None:
            print("List is Empty")
        else:
            while b7 is not None:
                print("<=>",b7.b1,b9 = "")
                b7 = b7.b3
    def fonk8(self):
        if self.b4 is None:
            print("List is Empty")
        else:
            self.b4 = self.b4.b2
            self.b4.b3 = None
    def fonk9(self):
        if self.b4 is None:
            print("List is Empty")
        else:
            self.b5 = self.b5.b3
            self.b5.b2 = None
    def fonk10(self,b8):
        if self.b4 = =None:
            print("List is Empty")
        elif b8 = =0:
            self.fonk8()
        else:
            b7 = self.b4
            a1 = 0
            while b7!=None and b8-1 is not a1:
                a1+=1
                b7 = b7.b2
            if b7 is None and b8>=a1:
                print("Invalid Position")
            elif b7.b2.b2 is None and a1 is b8-1:
                b7.b2 = None
                self.b5 = b7;
            else:
                b7.b2.b2.b3 = b7
                b7.b2 = b7.b2.b2
def fonk11():
    b10 = class2()
    b11 = 'y'
    while b11 is 'y':
        print('''1.Insertion
2.Insert at begining
3.Insert at End
4.Insert at Position
5.Display list
6.Display in reverse order
7.Delete from begining
8.Delete from b9
9.Delete from position
10.EXIT''')
        b12 = int(input("Enter b12:::"))
        if b12 is 1:
            b6 = int(input("Enter b1::"))
            b10.fonk3(b6)
        elif b12 is 2:
            b6 = int(input("Enter b1::"))
            b10.fonk4(b6)
        elif b12 is 3:
            b6 = int(input("Enter b1::"))
            b10.fonk3(b6)
        elif b12 is 4:
            b8 = int(input("Enter Position(0 ......n)::"))
            b6 = int(input("Enter b1::"))
            b10.fonk5(b8,b6)
        elif b12 is 5:
            b10.fonk6()
        elif b12 is 6:
            print("List in Reverse Order is :::",b9 = "")
            b10.fonk7()
        elif b12 is 7:
            b10.fonk8()
        elif b12 is 8:
            b10.fonk9()
        elif b12 is 9:
            b8 = int(input("Enter Position(0 ......n)::"))
            b10.fonk10(b8)
        else:
            quit()
        b11 = input("\nEnter y to continue program:::")
fonk11()