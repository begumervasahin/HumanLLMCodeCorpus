from functools import wraps
from typing import cast, Callable, Dict, Generic, Tuple, Type, TypeVar, Union
__all__ = (
    'Recursion',
    'tail_recursive',
)
VT = TypeVar('VT')
KT = TypeVar('KT')
RT = TypeVar('RT')
TailRecFunction = Callable[..., RT]
class NotSet(type):
    pass
class Recursion(BaseException, Generic[VT, KT]):
    def __init__(self, *args: VT, **kwargs: KT) -> None:
        super().__init__()
        self.args = args
        self.kwargs = kwargs
def virtual_recurse(func: TailRecFunction, *args: VT, **kwargs: KT) -> RT:
    result: Union[Type[NotSet], RT] = NotSet
    while result is NotSet:
        try:
            result = func(*args, **kwargs)
        except Recursion as next_call:
            args = cast(Tuple[VT, ...], next_call.args)
            kwargs = cast(Dict[str, KT], next_call.kwargs)
    return cast(RT, result)
def tail_recursive(func: TailRecFunction) -> TailRecFunction:
    @wraps(func)
    def _trampolined(*args, **kwargs):
        return virtual_recurse(func, *args, **kwargs)
    return _trampolined
@tail_recursive
def factorial(n, acc=1):
    if n == 0:
        return acc
    else:
        raise Recursion(n - 1, acc * n)
if __name__ == "__main__":
    result = factorial(5)
    print("Factorial of 5:", result)