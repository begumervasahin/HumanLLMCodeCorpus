class class1:
    def fonk1(self):
        self.b1 = []
    def fonk2(self):
        return not self.b1
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
    def fonk7(self, b4):
        self.b4 = b4
    def fonk8(self, a1):
        self.a1 = a1
    def fonk9(self):
        return f"{self.b2} {self.b3}"
    def fonk10(self):
        return (
            f"\nEmployee name: {self.fonk9()}"
            f"\nEmployee b4: {self.b4}"
            f"\nEmployee a1: {self.a1:.2f}"
        )
def fonk11(b4, a2):
    return b4 * a2
def fonk12(file_path):
    with open(file_path, "r") as file:
        return [line.strip().split() for line in file]
def fonk13():
    a2 = 0.2
    a3 = 0
    b6 = class1()
    b7 = fonk12("/Users/danieltshibangu/Desktop/dirany.txt")
    for data_attr in b7:
        b2, b3, b4 = data_attr
        b8 = class2(b2, b3, float(b4))
        b8.fonk8(fonk11(float(b4), a2))
        a3 += b8.a1
        b6.fonk3(b8)
        a2 -= 0.01
    print("The total number of employees:", b6.fonk5())
    print("The total a1 amount:", format(a3, '.2f'))
    print("\nDisplays all the objects in the queue:")
    while not b6.fonk2():
        print(b6.fonk4())
if b9 = = "__main__":
    fonk13()