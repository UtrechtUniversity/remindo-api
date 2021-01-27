# (generated with --quick)

from typing import Any, Callable, Dict, Type, TypeVar

utils: module

_T = TypeVar('_T')

class RemindoRecipe:
    __doc__: str
    _recipe_dict: dict
    api_call_params_category: Any
    api_call_params_code: Any
    api_call_params_datasource_uuid: Any
    api_call_params_filtr: Any
    api_call_params_full: Any
    api_call_params_recipe_id: Any
    api_call_params_since: Any
    api_call_params_study_id: Any
    category: Any
    code: Any
    name: Any
    rid: Any
    settings_exam: Dict[str, Any]
    settings_exam_caesura: Any
    settings_exam_duration: Any
    settings_exam_round_grade_decimals: Any
    settings_max_retries: Any
    settings_passed: Any
    settings_practice: Dict[str, Any]
    settings_practice_continue_practice: Any
    settings_practice_repeat_until: Any
    settings_practice_start_retry_by_candidate: Any
    settings_practice_start_retry_delay: Any
    settings_settings: Dict[str, Any]
    settings_settings_bonuspoints: Any
    settings_settings_edit_caesura: Any
    settings_settings_edit_continue_practice: Any
    settings_settings_edit_retry_delay: Any
    settings_settings_edit_show_result: Any
    settings_settings_extra_time: Any
    settings_show_correct: Any
    settings_show_grade: Any
    settings_show_result: Dict[str, Any]
    settings_show_result_correct_answer: Any
    settings_show_result_given_answer: Any
    settings_show_result_score: Any
    settings_tools: Any
    settings_v: Any
    source_recipe_id: Any
    status: Any
    study_id: Any
    type: Any
    def __init__(self, _recipe_dict: dict) -> None: ...

@overload
def dataclass(_cls: Type[_T]) -> Type[_T]: ...
@overload
def dataclass(*, init: bool = ..., repr: bool = ..., eq: bool = ..., order: bool = ..., unsafe_hash: bool = ..., frozen: bool = ...) -> Callable[[Type[_T]], Type[_T]]: ...
