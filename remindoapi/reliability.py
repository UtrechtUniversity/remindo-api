"""Class implementation for Remindo reliability"""


class RemindoReliability:
    def __init__(self, reliability_dict):
        self._reliability_dict = reliability_dict

    def list_all(self):
        """Return Remindo reliability key values"""
        return {key: value for key, value in self._reliability_dict.items()}

    @property
    def alpha(self):
        """Return the alpha for the selected assessment"""
        return self._reliability_dict["alpha"]

    @property
    def sem(self):
        """Return the sem for the selected assessment"""
        return self._reliability_dict["sem"]

    @property
    def notes(self):
        """Return the notes for the selected assessment"""
        return self._reliability_dict["notes"][0]

    @property
    def missing_count(self):
        """Return the missing count for the selected assessment"""
        return self._reliability_dict["missing_count"]

    @property
    def answer_count(self):
        """Return the answer count for the selected assessment"""
        return self._reliability_dict["answer_count"]

    @property
    def stdev(self):
        """Return the standard deviation for the selected assessment"""
        return self._reliability_dict["stdev"]

    @property
    def average(self):
        """Return the average for the selected assessment"""
        return self._reliability_dict["average"]

    @property
    def max(self):
        """Return the max for the selected assessment"""
        return self._reliability_dict["max"]
