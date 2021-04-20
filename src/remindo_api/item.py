# src/remindo_api/item.py
"""Class implementation for Remindo item."""
from collections import OrderedDict
from dataclasses import dataclass


from remindo_api import utils


@dataclass
class RemindoItem:
    """Remindo Item object.

    Attributes
    ----------
    _item_dict : dict
        Dictionary containing the item information.
    """

    _item_dict: OrderedDict

    @property
    def item_identifier(self):
        """Return the section_id."""
        return utils.safeget(self._item_dict, "item_identifier")

    @property
    def num_attempts(self):
        """Return the number of attempts to the item."""
        return utils.safeget(self._item_dict, "num_attempts")

    @property
    def duration(self):
        """Return the duration of the answer to the item."""
        return utils.safeget(self._item_dict, "duration")

    @property
    def status(self):
        """Return the status of the answer to the item."""
        return utils.safeget(self._item_dict, "status")

    @property
    def score(self):
        """Return the score."""
        return utils.safeget(self._item_dict, "score")

    @property
    def passed(self):
        """Return boolean if item was correct."""
        return utils.safeget(self._item_dict, "passed")

    @property
    def max_score(self):
        """Return the max score on the item."""
        return utils.safeget(self._item_dict, "max_score")

    @property
    def flagged(self):
        """Return the whether the item was flagged."""
        return utils.safeget(self._item_dict, "flagged")

    @property
    def check_manually(self):
        """Return the check manually boolean."""
        return utils.safeget(self._item_dict, "check_manually")

    @property
    def weight(self):
        """Return the weight of the item."""
        return utils.safeget(self._item_dict, "weight")

    @property
    def subscription_id(self):
        """Return the subscription_id."""
        return utils.safeget(self._item_dict, "subscription_id")

    @property
    def position_item(self):
        """Return the position_id."""
        return utils.safeget(self._item_dict, "position_item")

    @property
    def response_cardinality(self):
        """Return the cardinality of the item response."""
        return utils.safeget(self._item_dict, "response", "RESPONSE", "cardinality")

    @property
    def response_baseType(self):
        """Return the base type of the item response."""
        return utils.safeget(self._item_dict, "response", "RESPONSE", "baseType")

    @property
    def response_choiceSequence(self):
        """Return the choice sequence."""
        return utils.safeget(self._item_dict, "response", "RESPONSE", "choiceSequence")

    @property
    def response_candidateResponse(self):
        """Return the candidate response."""
        return utils.safeget(
            self._item_dict, "response", "RESPONSE", "candidateResponse"
        )

    @property
    def response_correctResponse(self):
        """Return a boolean whether the answer was correct or not."""
        return utils.safeget(self._item_dict, "response", "RESPONSE", "correctResponse")

    # Api calls properties

    @property
    def api_call_params_recipe_id(self):
        """Return the parameter recipe_id used in the api call."""
        return utils.safeget(self._item_dict, "api_call_params", "recipe_id")

    @property
    def api_call_params_moment_id(self):
        """Return the parameter moment_id used in the api call."""
        return utils.safeget(self._item_dict, "api_call_params", "moment_id")

    @property
    def api_call_params_subscription_ids(self):
        """Return the parameter subscription_ids used in the api call."""
        return utils.safeget(self._item_dict, "api_call_params", "subscription_ids")

    @property
    def api_call_params_user_ids(self):
        """Return the parameter user_ids used in the api call."""
        return utils.safeget(self._item_dict, "api_call_params", "user_ids")

    @property
    def api_call_params_add_item_info(self):
        """Return the parameter add_item_info used in the api call."""
        return utils.safeget(self._item_dict, "api_call_params", "add_item_info")
