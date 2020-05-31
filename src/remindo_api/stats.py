"""Class implementation for Remindo stats

These are overall statistics for items.
"""
from dataclasses import dataclass


from remindo_api import utils


@dataclass
class RemindoStats:
    _stats_dict: dict

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
    def question_position(self):
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

    # Api call
    @property
    def api_call_params_recipe_id(self):
        """Return the Remindo recipe_id for the study"""
        return utils.safeget(self._stats_dict, "api_call_params", "recipe_id")

    @property
    def api_call_params_moment_id(self):
        """Return the Remindo moment_id for the study"""
        return utils.safeget(self._stats_dict, "api_call_params", "moment_id")

    @property
    def api_call_params_subscription_ids(self):
        """Return the Remindo subscription_ids for the study"""
        return utils.safeget(self._stats_dict, "api_call_params", "subscription_ids")

    @property
    def api_call_params_user_ids(self):
        """Return the Remindo user_ids for the study"""
        return utils.safeget(self._stats_dict, "api_call_params", "user_ids")
