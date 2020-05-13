# (generated with --quick)

from typing import Any

re: module

class TextCleaner:
    __doc__: str
    @classmethod
    def clean_all(cls, text) -> str: ...
    @classmethod
    def clean_extra_spaces(cls, text) -> str: ...
    @classmethod
    def clean_html_tags(cls, text) -> str: ...

def retry_if_type_error(exception) -> bool: ...
def safeget(dct, *keys) -> Any: ...
