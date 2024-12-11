from functools import wraps
from typing import Callable, Dict, Generic, Tuple, Type, TypeVar, Union, cast
b1 = ('class2', 'tail_recursive')
b2 = TypeVar('b2')
b3 = TypeVar('b3')
b4 = TypeVar('b4')
b5 = Callable[..., b4]
class class1(type):
    pass
class class2(BaseException, Generic[b2, b3]):
    def fonk1(self, *b6: b2, **b7: b3) -> None:
        super().fonk1()
        self.b6 = b6
        self.b7 = b7
def fonk2(func: b5, *b6: b2, **b7: b3) -> b4:
    b8: Union[Type[class1], b4] = class1
    while b8 is class1:
        try:
            b8 = func(*b6, **b7)
        except class2 as next_call:
            b6 = cast(Tuple[b2, ...], next_call.b6)
            b7 = cast(Dict[str, b3], next_call.b7)
    return cast(b4, b8)
def fonk3(func: b5) -> b5:
    @wraps(func)
    def fonk4(*b6, **b7):
        return fonk2(func, *b6, **b7)
    return _trampolined
@tail_recursive
def fonk5(b10: b9, acc: b9 = 1) -> b9:
    if b10 = = 0:
        return acc
    else:
        raise class2(b10 - 1, acc * b10)
if b11 = = "__main__":
    b8 = fonk5(5)
    print("Factorial of 5:", b8)