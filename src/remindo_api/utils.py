# src/remindo_api/utils.py
import re


class TextCleaner:
    """Class to clean notes' text."""

    @classmethod
    def clean_all(cls, text):
        text = TextCleaner.clean_html_tags(text)
        return TextCleaner.clean_extra_spaces(text)

    @classmethod
    def clean_html_tags(cls, text):
        cleanr = re.compile("<.*?>|&([a-z0-9]+|#[0-9]{1,6}|#x[0-9a-f]{1,6});")
        return re.sub(cleanr, "", str(text))

    @classmethod
    def clean_extra_spaces(cls, text):
        return " ".join(text.split())


def retry_if_type_error(exception):
    """Return True if we should retry, False otherwise."""
    return isinstance(exception, TypeError)


# From https://stackoverflow.com/questions/25833613/python-safe-method-to-get-value-of-nested-dictionary
def safeget(dct, *keys):
    for key in keys:
        try:
            dct = dct[key]
        except KeyError:
            return None
    return dct


# @retry(retry_on_exception=retry_if_type_error, wrap_exception=True, stop_max_attempt_number=10)
