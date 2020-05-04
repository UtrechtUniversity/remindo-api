import collections


class RemindoHelloWorld:
    def __init__(self, hw):
        self._hw = hw

    @property
    def message(self):
        """Return the Remindo id for the moment"""
        return self._hw["message"]
