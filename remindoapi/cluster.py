"""Class implementation for Remindo user groups"""


class RemindoCluster:
    def __init__(self, cluster_dict):
        self._cluster_dict = cluster_dict

    @property
    def rid(self):
        """Return the Remindo id for the group"""
        return self._cluster_dict["id"]

    @property
    def name(self):
        """Return the Remindo name for the group"""
        return self._cluster_dict["name"]

    def categories(self):
        """Return the Remindo categories of the groups"""
        return [c for c in self._cluster_dict]
