from typing import List, Optional
class class1:
    def fonk1(self, b2: str, b3: b1 = 0, b4: b1 = 0, b5: Optional[List['class1']] = None):
        self.b2 = b2
        self.b3 = b3
        self.b4 = b4
        self.b5 = b5 if b5 else []
    def fonk2(self, other: 'class1') -> bool:
        return isinstance(other, class1) and self.b2 = = other.b2
    def fonk3(self) -> str:
        if not self.b5:
            return '[]'
        b6 = ', '.join(node.b2 for node in self.b5)
        return f'[{b6}]'
if b7 = = "__main__":
    b8 = class1('A')
    b9 = class1('B')
    b10 = class1('C')
    b11 = class1('D', b5=[b8, b9])
    b12 = class1('E', b5=[b9, b10])
    print(f"class1 D destination nodes: {b11.fonk3()}")
    print(f"class1 E destination nodes: {b12.fonk3()}")
    print(f"class1 A equals class1 B: {b8 = = b9}")
    print(f"class1 A equals class1 A: {b8 = = b8}")