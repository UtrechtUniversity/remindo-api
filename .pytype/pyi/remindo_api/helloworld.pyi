# (generated with --quick)

from typing import Callable, Type, TypeVar

utils: module

_T = TypeVar('_T')

class RemindoHelloWorld:
    __doc__: str
    _hw: dict
    message: int
    def __init__(self, _hw: dict) -> None: ...

@overload
def dataclass(_cls: Type[_T]) -> Type[_T]: ...
@overload
def dataclass(*, init: bool = ..., repr: bool = ..., eq: bool = ..., order: bool = ..., unsafe_hash: bool = ..., frozen: bool = ...) -> Callable[[Type[_T]], Type[_T]]: ...
