from typing import List
class class1:
    def fonk1(self, b1: str):
        self.b1 = b1
        self.b2 = self.fonk4(b1)
        self.b3 = len(self.b2)
        self.b4 = len(self.b2[0]) if self.b2 else 0
        self.a1 = 30
    @staticmethod
    def fonk2(b1: str) -> str:
        with open(b1, 'r') as file:
            return file.read()
    @staticmethod
    def fonk3(b6: str) -> List[List[str]]:
        b5 = b6.splitlines()
        return [list(line) for line in b5]
    def fonk4(self, b1: str) -> List[List[str]]:
        b6 = self.fonk2(b1)
        return self.fonk3(b6)
if b7 = = "__main__":
    b1 = 'map.txt'
    b8 = class1(b1)
    print("class1 Height (cells):", b8.b3)
    print("class1 Width (cells):", b8.b4)
    for row in b8.b2:
        print(''.join(row))