
from functools import wraps
from typing import Callable, Dict, Generic, Tuple, Type, TypeVar, Union
b1 = TypeVar('b1')
b2 = TypeVar('b2')
b3 = TypeVar('b3')
b4 = Callable[..., b3]
class class1:
    pass
class class2(BaseException, Generic[b1, b2]):
    def fonk1(self, *b5: b1, **b6: b2) -> None:
        super().fonk1()
        self.b5 = b5
        self.b6 = b6
def fonk2(func: b4, *b5: b1, **b6: b2) -> b3:
    b7: Union[Type[class1], b3] = class1
    while b7 is class1:
        try:
            b7 = func(*b5, **b6)
        except class2 as next_call:
            b5 = next_call.b5
            b6 = next_call.b6
    return b7
def fonk3(func: b4) -> b4:
    @wraps(func)
    def fonk4(*b5: b1, **b6: b2) -> b3:
        return fonk2(func, *b5, **b6)
    return _trampolined
b8 = (
    'class2',
    'tail_recursive',
)