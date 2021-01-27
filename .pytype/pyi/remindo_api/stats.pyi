# (generated with --quick)

from typing import Any, Callable, Type, TypeVar

utils: module

_T = TypeVar('_T')

class RemindoStats:
    __doc__: str
    _stats_dict: dict
    answered: Any
    api_call_params_moment_id: Any
    api_call_params_recipe_id: Any
    api_call_params_subscription_ids: Any
    api_call_params_user_ids: Any
    code: Any
    difficulty: Any
    interaction_count: Any
    item_identifier: Any
    language: Any
    max_score: Any
    p: Any
    question_position: Any
    rir: Any
    section: Any
    std: Any
    total: Any
    type: Any
    def __init__(self, _stats_dict: dict) -> None: ...

@overload
def dataclass(_cls: Type[_T]) -> Type[_T]: ...
@overload
def dataclass(*, init: bool = ..., repr: bool = ..., eq: bool = ..., order: bool = ..., unsafe_hash: bool = ..., frozen: bool = ...) -> Callable[[Type[_T]], Type[_T]]: ...
