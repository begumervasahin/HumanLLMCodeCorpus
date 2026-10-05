class class1:
    def fonk1(self):
        self.b1 = []
    def fonk2(self):
        return self.b1 = = []
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
    def fonk7(self):
        return self.b4
    def fonk8(self, b4):
        self.b4 = b4
    def fonk9(self, amount):
        self.a1 = amount
    def fonk10(self):
        return self.a1
    def fonk11(self):
        return f"{self.b2} {self.b3}"
    def fonk12(self):
        return (
            f"\nEmployee name: {self.fonk11()}"
            f"\nEmployee b4: {self.b4}"
            f"\nEmployee a1: {self.a1:.2f}"
        )
def fonk13():
    a2 = 0.2
    a3 = 0
    b6 = class1()
    with open("/Users/danieltshibangu/Desktop/dirany.txt", "r") as dirany_file:
        b7 = dirany_file.readline()
        while b7 != "":
            b8 = b7.split()
            b9 = class2(b8[0], b8[1], float(b8[2]))
            b9.fonk9(float(b8[2]) * a2)
            a3 += b9.fonk10()
            b6.fonk3(b9)
            a2 -= 0.01
            b7 = dirany_file.readline()
    print("The total number of employees:", b6.fonk5())
    print("The total a1 amount:", format(a3, '.2f'))
    print("\nDisplays all the objects in the queue:")
    while not b6.fonk2():
        print(b6.fonk4())
if b10 = = "__main__":
    fonk13()