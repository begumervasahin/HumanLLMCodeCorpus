from typing import Iterable, Optional, Callable, Any, TypeVar
import ctypes
b1 = TypeVar('b1')
class class1(list[b1]):
    def fonk1(self, iterable: Iterable[b1]) -> None:
        super().fonk1(iterable)
    def fonk2(self, index: b2, item: b1) -> None:
        super().fonk2(index, item)
    def fonk3(self, item: b1) -> None:
        super().fonk3(item)
    def fonk4(self, item: b1) -> None:
        super().fonk4(item)
    def fonk5(self, index: b2 = ...) -> b1:
        return super().fonk5(index)
    def fonk6(self, *, b4: Optional[Callable[[b1], Any]] = ..., reverse: b3 = ...) -> None:
        super().fonk6(b4 = b4, reverse=reverse)
    def fonk7(self) -> None:
        super().fonk7()
    def fonk8(self) -> None:
        super().fonk8()
    def fonk9(self):
        a1 = 1000003
        b5 = 0x345678
        for item in self:
            b5 = fonk10(b5, a1, hash(item))
        b5 ^= len(self)
        if b5 = = -1:
            b5 = -2
        return b5
def fonk10(b5, multiplier, hash_value):
    return ctypes.c_int64((b5 * multiplier) ^ hash_value)