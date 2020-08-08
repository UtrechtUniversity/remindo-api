# src/remindo_api/cluster.py
"""Class implementation for Remindo user groups."""
from dataclasses import dataclass

from remindo_api import utils


@dataclass
class RemindoCluster:
    """Remindo Cluster object.

    Attributes
    ----------
    _cluster_dict : dict
        Dictionary containing the cluster information.
    """

    _cluster_dict: dict

    @property
    def rid(self) -> int:
        """Return the Remindo id for the group."""
        return utils.safeget(self._cluster_dict, "id")

    @property
    def name(self) -> str:
        """Return the Remindo name for the group."""
        return utils.safeget(self._cluster_dict, "name")

    def categories(self) -> list:
        """Return the Remindo categories of the groups."""
        return [c for c in self._cluster_dict]
