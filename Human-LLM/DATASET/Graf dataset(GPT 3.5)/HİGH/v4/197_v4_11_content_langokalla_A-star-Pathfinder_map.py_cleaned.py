class class1:
    def fonk1(self, b1):
        self.b1 = b1
        self.b2 = self.fonk2(b1)
        self.b3 = len(self.b2)
        self.b4 = len(self.b2[0])
        self.a1 = 30
    @staticmethod
    def fonk2(b1):
        with open(b1) as file:
            b5 = file.read().splitlines()
        return b5
b1 = "map.txt"
b6 = class1(b1)
print("class1 Dimensions:", b6.b3, "x", b6.b4)
print("Cell Size:", b6.a1)
print("class1 Content:")
for row in b6.b2:
    print(row)