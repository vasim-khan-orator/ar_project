from __future__ import annotations


class VoiceRouter:
    def __init__(self) -> None:
        self._enabled = False

    def enable(self) -> None:
        self._enabled = True

    def disable(self) -> None:
        self._enabled = False
