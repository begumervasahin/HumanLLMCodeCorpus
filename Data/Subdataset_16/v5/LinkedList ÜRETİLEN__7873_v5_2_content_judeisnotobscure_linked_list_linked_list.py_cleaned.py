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
        if b6 is not None and b6.b1 = = key:
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
        b6 = self.b3
        while b6 is not None:
            print(b6.b1)
            b6 = b6.b2
def fonk6(lst):
    try:
        for i in range(1, len(lst)):
            print(f"d{i+1} = class1('{lst[i]}')")
    except (TypeError, ValueError):
        print("Pass in a list to generate nodes from the list items. Usage: fonk6(list)")
def fonk7(lst):
    b8 = [f"d{i+1}" for i in range(1, len(lst))]
    try:
        for d in range(len(b8) - 1):
            print(f"{b8[d]}.b2 = {b8[d+1]}")
    except (TypeError, ValueError):
        print("Usage: fonk7(list)")
if b9 = = "__main__":
    b10 = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    b11 = class2()
    b11.b3 = class1("Monday")
    b12 = class1("Tuesday")
    b13 = class1("Wednesday")
    b14 = class1("Thursday")
    b15 = class1("Friday")
    b16 = class1("Saturday")
    b17 = class1("Sunday")
    b11.b3.b2 = b12
    b12.b2 = b13
    b13.b2 = b14
    b14.b2 = b15
    b15.b2 = b16
    b16.b2 = b17
    print("Original List:")
    b11.fonk5()
    print("*" * 40)
    b11.fonk3("Frargsday")
    print("After Adding 'Frargsday':")
    b11.fonk5()
    print("*" * 40)
    b11.fonk4("Frargsday")
    print("After Removing 'Frargsday':")
    b11.fonk5()