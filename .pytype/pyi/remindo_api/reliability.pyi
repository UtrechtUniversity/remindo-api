# (generated with --quick)

from typing import Any, Callable, Type, TypeVar

utils: module

_T = TypeVar('_T')

class RemindoReliability:
    __doc__: str
    _reliability_dict: dict
    alpha: Any
    answer_count: Any
    api_call_params_corrections: Any
    api_call_params_locale: Any
    api_call_params_moment_id: Any
    api_call_params_recipe_id: Any
    api_call_params_scan_id: Any
    api_call_params_variant_id: Any
    average: Any
    max: Any
    missing_count: Any
    notes: Any
    sem: Any
    stdev: Any
    def __init__(self, _reliability_dict: dict) -> None: ...
    def list_all(self) -> dict: ...

@overload
def dataclass(_cls: Type[_T]) -> Type[_T]: ...
@overload
def dataclass(*, init: bool = ..., repr: bool = ..., eq: bool = ..., order: bool = ..., unsafe_hash: bool = ..., frozen: bool = ...) -> Callable[[Type[_T]], Type[_T]]: ...
