class class1:
    def fonk1(self, b1):
        self.b1 = b1
        self.b2 = None
class class2:
    def fonk2(self):
        self.b3 = None
    def fonk3(self, b1):
        b4 = class1(b1)
        b4.b2 = self.b3
        self.b3 = b4
    def fonk4(self, b1):
        b5 = self.b3
        b6 = None
        while b5:
            if b5.b1 = = b1:
                if b6:
                    b6.b2 = b5.b2
                else:
                    self.b3 = b5.b2
                return
            b6 = b5
            b5 = b5.b2
        print(f"Value {b1} not found in the list.")
    def fonk5(self):
        b7 = []
        b5 = self.b3
        while b5:
            b7.append(str(b5.b1))
            b5 = b5.b2
        return " -> ".join(b7) + " -> None"
def fonk6(input_list):
    b8 = class2()
    for item in input_list:
        b8.fonk3(item)
    print("Input list:", b8)
    b5 = b8.b3
    b6 = None
    while b5:
        b9 = b5.b2
        b5.b2 = b6
        b6 = b5
        b5 = b9
    b8.b3 = b6
    return b8
if b10 = = "__main__":
    print('\nReverse and Deleting in Singly Linked List\n')
    b11 = [
        (1, 2, 3, 4, 5),
        ('org', 'com', 'her', 'him', 'blah'),
        (1, 'com', 3, 'him', 5),
        (1, 'com', class2(), 'him', 5),
        ('B',),
        ('B', 'B', 'B', 'B'),
        (),
    ]
    for idx, test_case in enumerate(b11):
        b12 = fonk6(test_case)
        print(f"Output list for test case {idx + 1}: {b12}")
        if test_case:
            print(f"Deleting '{test_case[0]}'")
            b12.fonk4(test_case[0])
            print(f"Output list after deleting '{test_case[0]}': {b12}")
        print('')