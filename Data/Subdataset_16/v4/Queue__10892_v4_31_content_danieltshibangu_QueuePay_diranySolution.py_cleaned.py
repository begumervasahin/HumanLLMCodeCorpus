class class1:
    def fonk1(self):
        self.b1 = []
    def fonk2(self):
        return len(self.b1) == 0
    def fonk3(self, item):
        self.b1.insert(0, item)
    def fonk4(self):
        return self.b1.pop()
    def fonk5(self):
        return len(self.b1)
class class2:
    def fonk6(self, b2, b3, b4):
        self.b2 = b2
        self.b3 = b3
        self.b4 = float(b4)
        self.b5 = f'{b2}.{b3}@company.com'
        self.a1 = 0.0
    def fonk7(self):
        return self.b4
    def fonk8(self, b4):
        self.b4 = float(b4)
    def fonk9(self, amount):
        self.a1 = float(amount)
    def fonk10(self):
        return self.a1
    def fonk11(self):
        return f'{self.b2} {self.b3}'
    def fonk12(self):
        return (
            f'\nEmployee name: {self.fonk11()}'
            f'\nEmployee b4: {self.b4}'
            f'\nEmployee a1: {self.a1:.2f}'
        )
def fonk13():
    a2 = 0.2
    a3 = 0.0
    b6 = class1()
    with open('/Users/danieltshibangu/Desktop/dirany.txt', 'r') as dirany_file:
        for line in dirany_file:
            b7 = line.split()
            if len(b7) < 3:
                continue
            b8 = class2(b7[0], b7[1], b7[2])
            b8.fonk9(b8.fonk7() * a2)
            a3 += b8.fonk10()
            b6.fonk3(b8)
            a2 -= 0.01
    print(f"The total number of employees: {b6.fonk5()}")
    print(f"The total a1 amount: {a3:.2f}")
    print("\nDisplays all the objects in the queue:")
    while not b6.fonk2():
        print(b6.fonk4())
if b9 = = "__main__":
    fonk13()