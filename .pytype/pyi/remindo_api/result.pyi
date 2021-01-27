# (generated with --quick)

from typing import Any, Callable, Type, TypeVar

utils: module

_T = TypeVar('_T')

class RemindoResult:
    __doc__: str
    _result_dict: dict
    api_call_params_candidate_codes: Any
    api_call_params_candidate_filter: Any
    api_call_params_candidate_ids: Any
    api_call_params_cluster_ids: Any
    api_call_params_code: Any
    api_call_params_complete: Any
    api_call_params_end_time_since: Any
    api_call_params_end_time_until: Any
    api_call_params_id: Any
    api_call_params_modified_since: Any
    api_call_params_modified_until: Any
    api_call_params_page: Any
    api_call_params_page_size: Any
    api_call_params_recipe_ids: Any
    api_call_params_result_ids: Any
    api_call_params_search: Any
    api_call_params_start_time_since: Any
    api_call_params_start_time_until: Any
    api_call_params_status: Any
    api_call_params_study_ids: Any
    api_call_params_subscription_ids: Any
    api_call_params_type: Any
    area_feedback: Any
    area_name: Any
    can_change: Any
    cluster_ids: Any
    end_time: Any
    grade: Any
    grade_formatted: Any
    i_answered: Any
    i_correct: Any
    i_count: Any
    i_incorrect: Any
    i_mostlycorrect: Any
    i_mostlyincorrect: Any
    i_review: Any
    i_right: Any
    max_score: Any
    passed: Any
    recipe_category: Any
    recipe_code: Any
    recipe_id: Any
    recipe_name: Any
    recipe_source_id: Any
    recipe_type: Any
    report_data: Any
    result_id: Any
    score: Any
    score_type: Any
    show_correct: Any
    show_given_answer: Any
    show_grade: Any
    show_passed: Any
    show_score: Any
    start_time: Any
    status: Any
    study_id: Any
    study_name: Any
    subscription_id: Any
    try_count: Any
    user_code: Any
    user_id: Any
    def __init__(self, _result_dict: dict) -> None: ...
    def list_results(self) -> dict: ...

@overload
def dataclass(_cls: Type[_T]) -> Type[_T]: ...
@overload
def dataclass(*, init: bool = ..., repr: bool = ..., eq: bool = ..., order: bool = ..., unsafe_hash: bool = ..., frozen: bool = ...) -> Callable[[Type[_T]], Type[_T]]: ...
