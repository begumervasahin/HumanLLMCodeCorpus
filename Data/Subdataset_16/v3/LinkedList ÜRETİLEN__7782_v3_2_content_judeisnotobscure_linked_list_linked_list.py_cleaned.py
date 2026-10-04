class class1:
    def fonk1(self, b1 = None):
        self.b1 = b1
        self.b2 = None
class class2:
    def fonk2(self):
        self.b3 = None
    def fonk3(self, end_data):
        b4 = class1(end_data)
        if self.b3 is None:
            self.b3 = b4
            return
        b5 = self.b3
        while b5.b2:
            b5 = b5.b2
        b5.b2 = b4
    def fonk4(self, key):
        b6 = self.b3
        b7 = None
        while b6 and b6.b1 != key:
            b7 = b6
            b6 = b6.b2
        if b6 is None:
            return
        if b7 is None:
            self.b3 = b6.b2
        else:
            b7.b2 = b6.b2
        b6 = None
    def fonk5(self):
        b6 = self.b3
        while b6:
            print(b6.b1, b8 = ' -> ')
            b6 = b6.b2
        print('None')
def fonk6(b10):
    if not isinstance(b10, list):
        print("Please pass a list to generate nodes from the list items.")
        return
    for i in range(1, len(b10)):
        print(f"d{i + 1} = class1('{b10[i]}')")
def fonk7(b10):
    if not isinstance(b10, list):
        print("Please pass a list to generate code for linking nodes.")
        return
    for i in range(1, len(b10)):
        print(f"d{i}.b2 = d{i + 1}")
if b9 = = "__main__":
    b10 = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    b11 = class2()
    b11.b3 = class1(b10[0])
    b12 = class1('Tuesday')
    b13 = class1('Wednesday')
    b14 = class1('Thursday')
    b15 = class1('Friday')
    b16 = class1('Saturday')
    b17 = class1('Sunday')
    b11.b3.b2 = b12
    b12.b2 = b13
    b13.b2 = b14
    b14.b2 = b15
    b15.b2 = b16
    b16.b2 = b17
    print("Initial list:")
    b11.fonk5()
    print("*" * 40)
    b11.fonk3("Frargsday")
    print("List after adding 'Frargsday':")
    b11.fonk5()
    print("*" * 40)
    b11.fonk4("Frargsday")
    print("List after removing 'Frargsday':")
    b11.fonk5()
    print("*" * 40)
    print("Generated node creation code:")
    fonk6(b10)
    print("*" * 40)
    print("Generated node linking code:")
    fonk7(b10)