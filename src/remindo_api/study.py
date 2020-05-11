"""Class implementation for Remindo studies"""
from remindo_api import utils


class RemindoStudy:
    def __init__(self, study_dict):
        self._study_dict = study_dict

    def list_all(self):
        """Return Remindo studies"""
        return {key: value for key, value in self._study_dict.items()}

    @property
    def rid(self):
        """Return the Remindo id for the study"""
        return utils.safeget(self._study_dict, "id")

    @property
    def name(self):
        """Return the Remindo name for the study"""
        return utils.safeget(self._study_dict, "name")

    @property
    def code(self):
        """Return the Remindo code for the study"""
        return utils.safeget(self._study_dict, "code")

    @property
    def descr(self):
        """Return the Remindo description for the study"""
        return utils.safeget(self._study_dict, "descr")

    @property
    def edition_name(self):
        """Return the Remindo edition name for the study"""
        return utils.safeget(self._study_dict, "edition_name")

    @property
    def edition_descr(self):
        """Return the Remindo edition description for the study"""
        return utils.safeget(self._study_dict, "edition_descr")

    @property
    def source_edition_id(self):
        """Return the Remindo source edition id for the study"""
        return utils.safeget(self._study_dict, "source_edition_id")

    @property
    def source_study_id(self):
        """Return the Remindo source study id for the study"""
        return utils.safeget(self._study_dict, "source_study_id")

    # API call params

    @property
    def api_call_params_code(self):
        """Return the parameter code used in the api call"""
        return utils.safeget(self._study_dict, "api_call_params", "code")

    @property
    def api_call_params_study_id(self):
        """Return the parameter study_id used in the api call"""
        return utils.safeget(self._study_dict, "api_call_params", "study_id")

    @property
    def api_call_params_datasource_uuid(self):
        """Return the parameter datasource_uuid used in the api call"""
        return utils.safeget(self._study_dict, "api_call_params", "datasource_uuid")

    @property
    def api_call_params_complete(self):
        """Return the parameter complete used in the api call"""
        return utils.safeget(self._study_dict, "api_call_params", "complete")

    @property
    def api_call_params_since(self):
        """Return the parameter since used in the api call"""
        return utils.safeget(self._study_dict, "api_call_params", "since")
