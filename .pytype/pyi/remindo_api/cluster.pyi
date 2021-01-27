# (generated with --quick)

from typing import Callable, Type, TypeVar

utils: module

_T = TypeVar('_T')

class RemindoCluster:
    __doc__: str
    _cluster_dict: dict
    name: str
    rid: int
    def __init__(self, _cluster_dict: dict) -> None: ...
    def categories(self) -> list: ...

@overload
def dataclass(_cls: Type[_T]) -> Type[_T]: ...
@overload
def dataclass(*, init: bool = ..., repr: bool = ..., eq: bool = ..., order: bool = ..., unsafe_hash: bool = ..., frozen: bool = ...) -> Callable[[Type[_T]], Type[_T]]: ...
