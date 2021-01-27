# (generated with --quick)

import collections
from typing import Any, Callable, Type, TypeVar

OrderedDict: Type[collections.OrderedDict]
utils: module

_T = TypeVar('_T')

class RemindoItem:
    __doc__: str
    _item_dict: collections.OrderedDict
    api_call_params_add_item_info: Any
    api_call_params_moment_id: Any
    api_call_params_recipe_id: Any
    api_call_params_subscription_ids: Any
    api_call_params_user_ids: Any
    check_manually: Any
    duration: Any
    flagged: Any
    item_identifier: Any
    max_score: Any
    num_attempts: Any
    passed: Any
    position_item: Any
    response_baseType: Any
    response_candidateResponse: Any
    response_cardinality: Any
    response_choiceSequence: Any
    response_correctResponse: Any
    score: Any
    status: Any
    subscription_id: Any
    weight: Any
    def __init__(self, _item_dict: collections.OrderedDict) -> None: ...

@overload
def dataclass(_cls: Type[_T]) -> Type[_T]: ...
@overload
def dataclass(*, init: bool = ..., repr: bool = ..., eq: bool = ..., order: bool = ..., unsafe_hash: bool = ..., frozen: bool = ...) -> Callable[[Type[_T]], Type[_T]]: ...
