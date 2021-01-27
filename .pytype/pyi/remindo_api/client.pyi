# (generated with --quick)

import remindo_api.cluster
import remindo_api.helloworld
import remindo_api.item
import remindo_api.moment
import remindo_api.recipe
import remindo_api.reliability
import remindo_api.request
import remindo_api.result
import remindo_api.stats
import remindo_api.study
from typing import Any, List, Type

RemindoCluster: Type[remindo_api.cluster.RemindoCluster]
RemindoHelloWorld: Type[remindo_api.helloworld.RemindoHelloWorld]
RemindoItem: Type[remindo_api.item.RemindoItem]
RemindoMoment: Type[remindo_api.moment.RemindoMoment]
RemindoRecipe: Type[remindo_api.recipe.RemindoRecipe]
RemindoReliability: Type[remindo_api.reliability.RemindoReliability]
RemindoRequest: Type[remindo_api.request.RemindoRequest]
RemindoResult: Type[remindo_api.result.RemindoResult]
RemindoStats: Type[remindo_api.stats.RemindoStats]
RemindoStudy: Type[remindo_api.study.RemindoStudy]
requests: module

class RemindoClient:
    __doc__: str
    ip: Any
    query_dict: dict
    secret: Any
    url_base: Any
    uuid: Any
    def __init__(self, uuid, secret, url_base) -> None: ...
    def hello_world(self) -> remindo_api.request.RemindoRequest: ...
    def list_clusters(self, filter: str = ..., category: str = ..., full: bool = ...) -> List[remindo_api.cluster.RemindoCluster]: ...
    def list_item_results(self, recipe_id: int = ..., moment_id: int = ..., subscription_ids: int = ..., user_ids: int = ..., add_item_info: bool = ...) -> List[remindo_api.item.RemindoItem]: ...
    def list_moments(self, ids: int = ..., code: str = ..., recipe_ids: int = ..., frm: str = ..., until: str = ...) -> List[remindo_api.moment.RemindoMoment]: ...
    def list_moments_results(self, id: int = ..., code: int = ..., candidate_ids: int = ..., candidate_codes: int = ..., candidate_filter: str = ...) -> List[remindo_api.result.RemindoResult]: ...
    def list_recipes(self, code: str = ..., category: str = ..., study_id: int = ..., recipe_id: int = ..., filtr: str = ..., datasource_uuid: str = ..., since: str = ..., properties: bool = ..., full: bool = ...) -> List[remindo_api.recipe.RemindoRecipe]: ...
    def list_reliability(self, recipe_id: int = ..., moment_id: int = ..., variant_id: int = ..., scan_id: int = ..., corrections: list = ..., locale: str = ...) -> Any: ...
    def list_results(self, typ: str = ..., modified_since: str = ..., modified_until: str = ..., start_time_since: str = ..., start_time_until: str = ..., end_time_since: str = ..., end_time_until: str = ..., status: str = ..., search: str = ..., candidate_ids: int = ..., cluster_ids: int = ..., study_ids: int = ..., recipe_ids: int = ..., result_ids: int = ..., subscription_ids: int = ..., page: int = ..., page_size: int = ..., complete: bool = ...) -> List[remindo_api.result.RemindoResult]: ...
    def list_stats(self, recipe_id: int = ..., moment_id: int = ..., subscription_ids: int = ..., user_ids: int = ...) -> List[remindo_api.stats.RemindoStats]: ...
    def list_studies(self, code: str = ..., study_id: int = ..., datasource_uuid: str = ..., complete: bool = ..., since: str = ...) -> list: ...
    def list_subscription_result(self, recipe_id: int = ..., moment_id: int = ..., subscription_ids: int = ..., user_ids: int = ..., add_item_info: bool = ...) -> Any: ...
    def request(self, *args, **kwargs) -> Any: ...

class RemindoClientException(Exception):
    __doc__: str
    error_msg: Any
    def __init__(self, error_msg) -> None: ...
    def __str__(self) -> Any: ...
