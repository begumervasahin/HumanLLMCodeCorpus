from typing import Any, Optional
class class1:
    def fonk1(
        self,
        b1: Any,
        b2: Optional['class1'],
        b3: Any,
        b4: int,
        b5: float,
        b6: Any
    ) -> None:
        self.b1 = b1
        self.b2 = b2
        self.b3 = b3
        self.b4 = b4
        self.b5 = b5
        self.b6 = b6
        if self.b1 is not None:
            self.b7 = ''.join(map(str, self.b1))
    def fonk2(self, other: 'class1') -> bool:
        return self.b7 = = other.b7
    def fonk3(self, other: 'class1') -> bool:
        return self.b7 < other.b7