class class1:
    def fonk1(self, b1):
        self.b1 = b1
        self.b2 = self.fonk2(b1)
        self.height, self.b3 = len(self.b2), len(self.b2[0])
        self.a1 = 30
    @staticmethod
    def fonk2(b1):
        with open(b1) as file:
            return [line.strip() for line in file.readlines()]
b1 = "map.txt"
b4 = class1(b1)
print("class1 Dimensions:", b4.height, "x", b4.b3)
print("Cell Size:", b4.a1)
print("class1 Content:")
for row in b4.b2:
    print(row)