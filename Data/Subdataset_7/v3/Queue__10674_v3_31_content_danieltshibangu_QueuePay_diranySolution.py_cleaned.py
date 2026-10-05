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
        self.b4 = b4
        self.b5 = f"{b2}.{b3}@company.com"
        self.a1 = 0
    def fonk7(self, amount):
        self.a1 = amount
    def fonk8(self):
        return self.a1
    def fonk9(self):
        return f"{self.b2} {self.b3}"
    def fonk10(self):
        return (f"\nEmployee name: {self.fonk9()}\n"
                f"class2 b4: {self.b4}\n"
                f"class2 a1: {self.a1:.2f}")
def fonk11():
    a2 = 0.2
    a3 = 0
    b6 = class1()
    with open('/Users/danieltshibangu/Desktop/dirany.txt', 'r') as dirany_file:
        for line_data in dirany_file:
            b7 = line_data.split()
            b2, b3, b4 = b7[0], b7[1], float(b7[2])
            b8 = class2(b2, b3, b4)
            b8.fonk7(b4 * a2)
            a3 += b8.fonk8()
            b6.fonk3(b8)
            a2 -= 0.01
    print("The total number of employees:", b6.fonk5())
    print("The total a1 amount:", f"{a3:.2f}")
    print("\nDisplays all the objects in the queue:")
    while not b6.fonk2():
        print(b6.fonk4())
if b9 = = "__main__":
    fonk11()