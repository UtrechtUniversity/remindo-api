# (generated with --quick)

from typing import Any, Callable, Type, TypeVar

utils: module

_T = TypeVar('_T')

class RemindoStudy:
    __doc__: str
    _study_dict: dict
    api_call_params_code: Any
    api_call_params_complete: Any
    api_call_params_datasource_uuid: Any
    api_call_params_since: Any
    api_call_params_study_id: Any
    code: Any
    descr: Any
    edition_descr: Any
    edition_name: Any
    name: Any
    rid: Any
    source_edition_id: Any
    source_study_id: Any
    def __init__(self, _study_dict: dict) -> None: ...
    def list_all(self) -> dict: ...

@overload
def dataclass(_cls: Type[_T]) -> Type[_T]: ...
@overload
def dataclass(*, init: bool = ..., repr: bool = ..., eq: bool = ..., order: bool = ..., unsafe_hash: bool = ..., frozen: bool = ...) -> Callable[[Type[_T]], Type[_T]]: ...
