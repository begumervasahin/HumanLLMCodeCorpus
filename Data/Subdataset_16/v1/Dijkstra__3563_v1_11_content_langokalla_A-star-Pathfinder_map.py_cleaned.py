class class1:
    def fonk1(self, b1: str):
        self.b1 = b1
        self.b2 = self.fonk3(self.fonk2(b1))
        self.b3 = len(self.b2)
        self.b4 = len(self.b2[0])
        self.a1 = 30
    @staticmethod
    def fonk2(b1: str):
        with open(b1, 'r') as file:
            return file.read()
    @staticmethod
    def fonk3(file_content: str):
        b5 = file_content.splitlines()
        return [list(line) for line in b5]
b1 = 'map.txt'
b6 = class1(b1)
print("class1 Height (cells):", b6.b3)
print("class1 Width (cells):", b6.b4)
for row in b6.b2:
    print(''.join(row))