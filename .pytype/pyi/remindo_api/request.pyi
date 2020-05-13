# (generated with --quick)

from typing import Any, Dict, Tuple, TypeVar

HMAC: Any
SHA1: Any
json: module
requests: module
time: module

_T0 = TypeVar('_T0')

class RemindoRequest:
    __doc__: str
    api_url_base: Any
    body: Dict[str, Any]
    content: Any
    contentDumped: str
    envelope: Dict[str, Any]
    ip: Any
    message: Any
    payload: Any
    req_format: Any
    secEncoded: Any
    secret: Any
    signature: Any
    timestamp: int
    url: Any
    uuid: Any
    def __init__(self, client, url, content, req_format = ...) -> None: ...
    def makeFilter(self, params) -> Any: ...
    def makeTable(self, response: _T0) -> _T0: ...
    def request(self) -> Any: ...

class RemindoRequestException(Exception):
    __doc__: str
    error_msg: Any
    url: Any
    def __init__(self, error_msg, url) -> None: ...
    def __str__(self) -> Tuple[Any, str, Any]: ...
