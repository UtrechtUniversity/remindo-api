# src/remindo_api/reliability.py
"""Class implementation for Remindo reliability."""
from dataclasses import dataclass


from remindo_api import utils


@dataclass
class RemindoReliability:
    """Remindo Reliability object.

    Attributes
    ----------
    reliability_dict : dict
        Dictionary containing the reliability information.
    """

    _reliability_dict: dict

    def list_all(self):
        """Return Remindo reliability key values."""
        return {key: value for key, value in self._reliability_dict.items()}

    @property
    def alpha(self):
        """Return the alpha for the selected assessment."""
        return utils.safeget(self._reliability_dict, "alpha")

    @property
    def sem(self):
        """Return the sem for the selected assessment."""
        return utils.safeget(self._reliability_dict, "sem")

    @property
    def notes(self):
        """Return the notes for the selected assessment."""
        # TODO: to check when available
        return utils.safeget(self._reliability_dict, "notes")

    @property
    def missing_count(self):
        """Return the missing count for the selected assessment."""
        return utils.safeget(self._reliability_dict, "missing_count")

    @property
    def answer_count(self):
        """Return the answer count for the selected assessment."""
        return utils.safeget(self._reliability_dict, "answer_count")

    @property
    def stdev(self):
        """Return the standard deviation for the selected assessment."""
        return utils.safeget(self._reliability_dict, "stdev")

    @property
    def average(self):
        """Return the average for the selected assessment."""
        return utils.safeget(self._reliability_dict, "average")

    @property
    def max(self):
        """Return the max for the selected assessment."""
        return utils.safeget(self._reliability_dict, "max")

    # Api calls

    @property
    def api_call_params_recipe_id(self):
        """Return the parameter recipe id used in the api call."""
        return utils.safeget(self._reliability_dict, "api_call_params", "recipe_id")

    @property
    def api_call_params_moment_id(self):
        """Return the parameter moment_id used in the api call."""
        return utils.safeget(self._reliability_dict, "api_call_params", "moment_id")

    @property
    def api_call_params_variant_id(self):
        """Return the parameter variant_id used in the api call."""
        return utils.safeget(self._reliability_dict, "api_call_params", "variant_id")

    @property
    def api_call_params_scan_id(self):
        """Return the parameter scan_id used in the api call."""
        return utils.safeget(self._reliability_dict, "api_call_params", "scan_id")

    @property
    def api_call_params_corrections(self):
        """Return the parameter corrections used in the api call."""
        return utils.safeget(self._reliability_dict, "api_call_params", "corrections")

    @property
    def api_call_params_locale(self):
        """Return the parameter locale used in the api call."""
        return utils.safeget(self._reliability_dict, "api_call_params", "locale")
