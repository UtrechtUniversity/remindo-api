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
from typing import Any, Dict, List, Optional, Tuple, Type, Union

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
    query_dict: Dict[str, Any]
    secret: Any
    url_base: Any
    uuid: Any
    def __init__(self, uuid, secret, url_base) -> None: ...
    def hello_world(self) -> remindo_api.helloworld.RemindoHelloWorld: ...
    def list_clusters(self, filter = ..., category = ..., full = ...) -> List[remindo_api.cluster.RemindoCluster]: ...
    def list_item_results(self, recipe_id = ..., moment_id = ..., subscription_ids = ..., user_ids = ..., add_item_info = ...) -> Optional[List[remindo_api.item.RemindoItem]]: ...
    def list_moments(self, ids = ..., code = ..., recipe_ids = ..., frm = ..., until = ...) -> List[remindo_api.moment.RemindoMoment]: ...
    def list_moments_results(self, id = ..., code = ..., candidate_ids = ..., candidate_codes = ..., candidate_filter = ...) -> Optional[Union[bool, List[remindo_api.result.RemindoResult]]]: ...
    def list_recipes(self, code = ..., category = ..., study_id = ..., recipe_id = ..., filtr = ..., datasource_uuid = ..., since = ..., properties = ..., full = ...) -> List[remindo_api.recipe.RemindoRecipe]: ...
    def list_reliability(self, recipe_id = ..., moment_id = ..., variant_id = ..., scan_id = ..., corrections = ..., locale = ...) -> remindo_api.reliability.RemindoReliability: ...
    def list_results(self, typ = ..., modified_since = ..., modified_until = ..., start_time_since = ..., start_time_until = ..., end_time_since = ..., end_time_until = ..., status = ..., search = ..., candidate_ids = ..., cluster_ids = ..., study_ids = ..., recipe_ids = ..., result_ids = ..., subscription_ids = ..., page = ..., page_size = ..., complete = ...) -> Optional[List[remindo_api.result.RemindoResult]]: ...
    def list_stats(self, recipe_id = ..., moment_id = ..., subscription_ids = ..., user_ids = ...) -> Optional[List[remindo_api.stats.RemindoStats]]: ...
    def list_studies(self, code = ..., study_id = ..., datasource_uuid = ..., complete = ..., since = ...) -> Union[List[remindo_api.study.RemindoStudy], Tuple[List[remindo_api.study.RemindoStudy], List[remindo_api.recipe.RemindoRecipe]]]: ...
    def list_subscription_result(self, recipe_id = ..., moment_id = ..., subscription_ids = ..., user_ids = ..., add_item_info = ...) -> Any: ...
    def request(self, *args, **kwargs) -> Any: ...

class RemindoClientException(Exception):
    __doc__: str
    error_msg: Any
    def __init__(self, error_msg) -> None: ...
    def __str__(self) -> Any: ...
