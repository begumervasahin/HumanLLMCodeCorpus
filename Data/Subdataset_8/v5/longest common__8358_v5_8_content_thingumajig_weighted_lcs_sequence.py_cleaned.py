from typing import Iterable, Optional, Callable, Any, TypeVar
import ctypes
_T = TypeVar('_T')
class TokenSequence(list[_T]):
    def extend(self, iterable: Iterable[_T]) -> None:
        super().extend(iterable)
    def insert(self, index: int, item: _T) -> None:
        super().insert(index, item)
    def append(self, item: _T) -> None:
        super().append(item)
    def remove(self, item: _T) -> None:
        super().remove(item)
    def pop(self, index: int = ...) -> _T:
        return super().pop(index)
    def sort(self, *, key: Optional[Callable[[_T], Any]] = ..., reverse: bool = ...) -> None:
        super().sort(key=key, reverse=reverse)
    def clear(self) -> None:
        super().clear()
    def reverse(self) -> None:
        super().reverse()
    def __hash__(self):
        value = 0x345678
        prime = 1000003
        for item in self:
            value = combine_hashes(multiply_hash(prime, value), hash(item))
        value = value ^ len(self)
        if value == -1:
            value = -2
        return value
def multiply_hash(a, b):
    return ctypes.c_int64((a * b) & 0xffffffff).value
def combine_hashes(a, b):
    return a ^ b