"""Class implementation for Remindo studies"""


class RemindoStudy:
    def __init__(self, study_dict):
        self._study_dict = study_dict

    def list_all(self):
        """Return Remindo studies"""
        return {key: value for key, value in self._study_dict.items()}

    @property
    def rid(self):
        """Return the Remindo id for the study"""
        return self._study_dict["id"]

    @property
    def name(self):
        """Return the Remindo name for the study"""
        return self._study_dict["name"]

    @property
    def code(self):
        """Return the Remindo code for the study"""
        return self._study_dict["code"]

    @property
    def descr(self):
        """Return the Remindo description for the study"""
        return self._study_dict["descr"]

    @property
    def edition_name(self):
        """Return the Remindo edition name for the study"""
        return self._study_dict["edition_name"]

    @property
    def edition_descr(self):
        """Return the Remindo edition description for the study"""
        return self._study_dict["edition_descr"]

    @property
    def source_edition_id(self):
        """Return the Remindo source edition id for the study"""
        return self._study_dict["source_edition_id"]

    @property
    def source_study_id(self):
        """Return the Remindo source study id for the study"""
        return self._study_dict["source_study_id"]
