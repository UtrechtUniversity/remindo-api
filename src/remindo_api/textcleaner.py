# src/remindo_api/textcleaner.py
"""Class implementation to clean text retrieved from Remindo."""
import re


class RemindoTextCleaner:
    """Class to clean Remindo text."""

    @classmethod
    def clean_all(cls, text):
        """Clean all text."""
        text = RemindoTextCleaner.clean_html_tags(text)
        return RemindoTextCleaner.clean_extra_spaces(text)

    @classmethod
    def clean_html_tags(cls, text):
        """Clean html tags."""
        cleanr = re.compile("<.*?>|&([a-z0-9]+|#[0-9]{1,6}|#x[0-9a-f]{1,6});")
        return re.sub(cleanr, "", str(text))

    @classmethod
    def clean_extra_spaces(cls, text):
        """Trim extra spaces."""
        return " ".join(text.split())
