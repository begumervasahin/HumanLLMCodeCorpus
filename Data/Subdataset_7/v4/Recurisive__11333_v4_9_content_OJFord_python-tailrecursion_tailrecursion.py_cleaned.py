from functools import wraps
from typing import cast, Callable, Dict, Generic, Tuple, Type, TypeVar, Union
b1 = TypeVar('b1')
b2 = TypeVar('b2')
b3 = TypeVar('b3')
b4 = Callable[..., b3]
class class1(BaseException, Generic[b1, b2]):
    def fonk1(self, *b5: b1, **b6: b2) -> None:
        super().fonk1()
        self.b5 = b5
        self.b6 = b6
class class2(type):
    pass
def fonk2(func: b4, *b5: b1, **b6: b2) -> b3:
    b7: Union[Type[class2], b3] = class2
    while b7 is class2:
        try:
            b7 = func(*b5, **b6)
        except class1 as next_call:
            b5 = cast(Tuple[b1, ...], next_call.b5)
            b6 = cast(Dict[str, b2], next_call.b6)
    return cast(b3, b7)
def fonk3(func: b4) -> b4:
    @wraps(func)
    def fonk4(*b5, **b6):
        return fonk2(func, *b5, **b6)
    return _trampolined