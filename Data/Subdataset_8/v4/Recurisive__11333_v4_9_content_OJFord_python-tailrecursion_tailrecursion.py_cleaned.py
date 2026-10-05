from functools import wraps
from typing import cast, Callable, Dict, Generic, Tuple, Type, TypeVar, Union
VT = TypeVar('VT')
KT = TypeVar('KT')
RT = TypeVar('RT')
TailRecFunction = Callable[..., RT]
class Recursion(BaseException, Generic[VT, KT]):
    def __init__(self, *args: VT, **kwargs: KT) -> None:
        super().__init__()
        self.args = args
        self.kwargs = kwargs
class NotSet(type):
    pass
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