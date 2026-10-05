from functools import wraps
from typing import cast, Callable, Dict, Generic, Tuple, Type, TypeVar, Union
ValueType = TypeVar('ValueType')
KeywordType = TypeVar('KeywordType')
ReturnType = TypeVar('ReturnType')
TailRecFunction = Callable[..., ReturnType]
class Recursion(BaseException, Generic[ValueType, KeywordType]):
    def __init__(self, *args: ValueType, **kwargs: KeywordType) -> None:
        super().__init__()
        self.args = args
        self.kwargs = kwargs
class NotSet(type):
    pass
def virtual_recurse(func: TailRecFunction, *args: ValueType, **kwargs: KeywordType) -> ReturnType:
    result: Union[Type[NotSet], ReturnType] = NotSet
    while result is NotSet:
        try:
            result = func(*args, **kwargs)
        except Recursion as next_call:
            args = cast(Tuple[ValueType, ...], next_call.args)
            kwargs = cast(Dict[str, KeywordType], next_call.kwargs)
    return cast(ReturnType, result)
def tail_recursive(func: TailRecFunction) -> TailRecFunction:
    @wraps(func)
    def _trampolined(*args, **kwargs):
        return virtual_recurse(func, *args, **kwargs)
    return _trampolined