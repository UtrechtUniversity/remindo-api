# src/remindo_api/collectdata.py
"""Class implementation for testing API connection."""
from dataclasses import dataclass


from remindo_api import utils


@dataclass
class RemindoHelloWorld:
    """Class used to test connection to server.

    Args:
        _hw (dict): Dictionary containing the hello world object.

    """

    _hw: dict

    @property
    def message(self) -> int:
        """Return the Remindo id for the moment."""
        return utils.safeget(self._hw, "message")
