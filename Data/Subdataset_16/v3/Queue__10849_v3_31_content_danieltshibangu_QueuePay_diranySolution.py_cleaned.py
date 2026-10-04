class class1:
    def fonk1(self):
        self.b1 = []
    def fonk2(self):
        return not self.b1
    def fonk3(self, item):
        self.b1.insert(0, item)
    def fonk4(self):
        return self.b1.pop() if not self.fonk2() else None
    def fonk5(self):
        return len(self.b1)
class class2:
    def fonk6(self, b2, b3, b4):
        self.b2 = b2
        self.b3 = b3
        self.b4 = float(b4)
        self.b5 = f"{b2}.{b3}@company.com"
        self.a1 = 0.0
    def fonk7(self):
        return self.b4
    def fonk8(self, b4):
        self.b4 = float(b4)
    def fonk9(self, amount):
        self.a1 = amount
    def fonk10(self):
        return self.a1
    def fonk11(self):
        return f"{self.b2} {self.b3}"
    def fonk12(self):
        return (f"\nEmployee name: {self.fonk11()}"
                f"\nEmployee b4: {self.b4:.2f}"
                f"\nEmployee a1: {self.a1:.2f}")
def fonk13(b10, b6 = 0.2):
    a2 = 0.0
    b7 = class1()
    try:
        with open(b10, 'r') as file:
            for line in file:
                b8 = line.split()
                if len(b8) < 3:
                    continue
                first_name, last_name, b4 = b8
                b9 = class2(first_name, last_name, b4)
                a1 = b9.fonk7() * b6
                b9.fonk9(a1)
                a2 += b9.fonk10()
                b7.fonk3(b9)
                b6 -= 0.01
    except FileNotFoundError:
        print(f"Error: The file {b10} was not found.")
        return None, None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None, None
    return b7, a2
def fonk14(b7, a2):
    if b7 is None:
        return
    print(f"The total number of employees: {b7.fonk5()}")
    print(f"The total a1 amount: {a2:.2f}")
    print("\nDisplays all the objects in the queue:")
    while not b7.fonk2():
        print(b7.fonk4())
def fonk15():
    b10 = '/Users/danieltshibangu/Desktop/dirany.txt'
    b7, a2 = fonk13(b10)
    if b7 is not None:
        fonk14(b7, a2)
if b11 = = "__main__":
    fonk15()