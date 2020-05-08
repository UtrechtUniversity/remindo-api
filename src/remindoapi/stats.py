"""Class implementation for Remindo stats

These are overall statistics for items.
"""
from remindoapi import utils


class RemindoStats:
    def __init__(self, stats_dict):
        self._stats_dict = stats_dict

    @property
    def item_identifier(self):
        """Return the item_identifier"""
        return utils.safeget(self._stats_dict, "item_identifier")

    @property
    def code(self):
        """Return the code"""
        return utils.safeget(self._stats_dict, "code")

    @property
    def type(self):
        """Return the type"""
        return utils.safeget(self._stats_dict, "type")

    @property
    def language(self):
        """Return the language"""
        return utils.safeget(self._stats_dict, "language")

    @property
    def max_score(self):
        """Return the max score"""
        return utils.safeget(self._stats_dict, "max_score")

    @property
    def interaction_count(self):
        """Return the interaction count"""
        return utils.safeget(self._stats_dict, "interaction_count")

    @property
    def difficulty(self):
        """Return the difficulty"""
        return utils.safeget(self._stats_dict, "difficulty")

    @property
    def section(self):
        """Return the section"""
        return utils.safeget(self._stats_dict, "section")

    @property
    def question_numbers(self):
        """Return the question numbers in which it appears"""
        # Confirm this description
        return utils.safeget(self._stats_dict, "question_numbers")

    @property
    def p(self):
        """Return the p-value"""
        return utils.safeget(self._stats_dict, "p")

    @property
    def std(self):
        """Return the deviation"""
        return utils.safeget(self._stats_dict, "std")

    @property
    def rir(self):
        """Return the rir"""
        return utils.safeget(self._stats_dict, "rir")

    @property
    def total(self):
        """Return the total number of possible answers"""
        return utils.safeget(self._stats_dict, "total")

    @property
    def answered(self):
        """Return the number of answers"""
        return utils.safeget(self._stats_dict, "answered")
