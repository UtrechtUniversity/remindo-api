# (generated with --quick)

from typing import Any, Callable, Dict, Type, TypeVar

utils: module

_T = TypeVar('_T')

class RemindoMoment:
    __doc__: str
    _moment_dict: dict
    api_call_params_codes: Any
    api_call_params_from: Any
    api_call_params_ids: Any
    api_call_params_recipe_ids: Any
    api_call_params_until: Any
    caesura: Any
    code: Any
    datasource_id: Any
    date_end: Any
    date_start: Any
    duration: Any
    extra_time: Any
    limit_ips: Any
    name: Any
    recipe_id: Any
    recipe_type: Any
    requires_approval: Any
    rid: Any
    show_result: Any
    show_result_date: Any
    show_result_delay: Any
    show_result_delay_type: Any
    show_result_time: Any
    status: Any
    study_id: Any
    study_name: Any
    subscription_settings: Dict[str, Any]
    subscription_settings_exam_duration: Any
    time_end: Any
    time_start: Any
    type: Any
    def __init__(self, _moment_dict: dict) -> None: ...

@overload
def dataclass(_cls: Type[_T]) -> Type[_T]: ...
@overload
def dataclass(*, init: bool = ..., repr: bool = ..., eq: bool = ..., order: bool = ..., unsafe_hash: bool = ..., frozen: bool = ...) -> Callable[[Type[_T]], Type[_T]]: ...
