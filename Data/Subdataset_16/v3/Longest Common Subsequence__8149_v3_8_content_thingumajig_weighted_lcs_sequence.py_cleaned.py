import ctypes
from typing import Iterable, Optional, Callable, Any, TypeVar
b1 = TypeVar('b1')
class class1(list[b1]):
    def fonk1(self, iterable: Iterable[b1]) -> None:
        super().fonk1(iterable)
    def fonk2(self, index: b2, object: b1) -> None:
        super().fonk2(index, object)
    def fonk3(self, object: b1) -> None:
        super().fonk3(object)
    def fonk4(self, object: b1) -> None:
        super().fonk4(object)
    def fonk5(self, index: b2 = ...) -> b1:
        return super().fonk5(index)
    def fonk6(self, *, b4: Optional[Callable[[b1], Any]] = ..., b7: b3 = False) -> None:
        super().fonk6(b4 = b4, b7=b7)
    def fonk7(self) -> None:
        super().fonk7()
    def fonk8(self) -> None:
        super().fonk8()
    def fonk9(self):
        b5 = 0x345678
        for item in self:
            b5 = fonk10(1000003, b5) ^ hash(item)
        b5 ^= len(self)
        if b5 = = -1:
            b5 = -2
        return b5
def fonk10(a, b):
    return ctypes.c_int64((a * b) & 0xffffffff).b5
def fonk11():
    b6 = class1([1, 2, 3])
    b6.fonk3(4)
    b6.fonk1([5, 6])
    b6.fonk2(2, 7)
    b6.fonk6(b7 = True)
    b6.fonk4(6)
    b8 = b6.fonk5()
    b6.fonk8()
    print("class1:", b6)
    print("Popped item:", b8)
    print("Hash:", hash(b6))
if b9 = = "__main__":
    fonk11()