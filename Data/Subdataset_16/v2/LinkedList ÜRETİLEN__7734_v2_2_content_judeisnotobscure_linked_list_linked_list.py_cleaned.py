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
        if b6 is not None:
            if b6.b1 = = key:
                self.b3 = b6.b2
                b6 = None
                return
        while b6 is not None:
            if b6.b1 = = key:
                break
            b7 = b6
            b6 = b6.b2
        if b6 is None:
            return
        b7.b2 = b6.b2
        b6 = None
    def fonk5(self):
        b8 = self.b3
        while b8 is not None:
            print(b8.b1)
            b8 = b8.b2
def fonk6(b11):
    if not isinstance(b11, list):
        print("Please pass a list to generate nodes from the list items.")
        return
    for i in range(2, len(b11) + 1):
        print(f"d{i} = class1('{b11[i - 1]}')")
def fonk7(b11):
    if not isinstance(b11, list):
        print("Please pass a list to generate code for linking nodes.")
        return
    b9 = [f"d{i}" for i in range(2, len(b11) + 1)]
    for d in range(len(b9) - 1):
        print(f"{b9[d]}.b2 = {b9[d + 1]}")
if b10 = = "__main__":
    b11 = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    b12 = class2()
    b12.b3 = class1("Monday")
    b13 = class1('Tuesday')
    b14 = class1('Wednesday')
    b15 = class1('Thursday')
    b16 = class1('Friday')
    b17 = class1('Saturday')
    b18 = class1('Sunday')
    b12.b3.b2 = b13
    b13.b2 = b14
    b14.b2 = b15
    b15.b2 = b16
    b16.b2 = b17
    b17.b2 = b18
    print("Initial list:")
    b12.fonk5()
    print("*" * 40)
    b12.fonk3("frargsday")
    print("List after adding 'frargsday':")
    b12.fonk5()
    print("*" * 40)
    b12.fonk4("frargsday")
    print("List after removing 'frargsday':")
    b12.fonk5()
    print("*" * 40)
    print("Generated node creation code:")
    fonk6(b11)
    print("*" * 40)
    print("Generated node linking code:")
    fonk7(b11)