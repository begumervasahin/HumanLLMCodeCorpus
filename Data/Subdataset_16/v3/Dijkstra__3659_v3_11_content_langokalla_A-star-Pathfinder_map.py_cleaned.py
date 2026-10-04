from typing import List, Tuple
class class1:
    def fonk1(self, b1: str):
        self.b1 = b1
        self.b2 = self.fonk3(self.fonk2(b1))
        self.b3 = len(self.b2)
        self.b4 = len(self.b2[0])
        self.a1 = 30
    @staticmethod
    def fonk2(b1: str) -> str:
        with open(b1, 'r') as file:
            return file.read()
    @staticmethod
    def fonk3(file_content: str) -> List[List[str]]:
        b5 = file_content.splitlines()
        return [list(line) for line in b5]
if b6 = = "__main__":
    b1 = 'map.txt'
    b7 = class1(b1)
    print("class1 Height (cells):", b7.b3)
    print("class1 Width (cells):", b7.b4)
    for row in b7.b2:
        print(''.join(row))