# content of src/remindo_api/helloworld.py
from remindo_api import utils


class RemindoHelloWorld:
    def __init__(self, hw):
        self._hw = hw

    @property
    def message(self):
        """Return the Remindo id for the moment"""
        return utils.safeget(self._hw, "message")
