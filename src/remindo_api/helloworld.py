# content of src/remindo_api/helloworld.py
from dataclasses import dataclass


from remindo_api import utils


@dataclass
class RemindoHelloWorld:
    _hw: dict

    @property
    def message(self) -> int:
        """Return the Remindo id for the moment"""
        return utils.safeget(self._hw, "message")
