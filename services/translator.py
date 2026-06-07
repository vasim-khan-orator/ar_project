from __future__ import annotations

from core.app_launcher import AppLauncher


class TranslatorService:
    def __init__(self, launcher: AppLauncher) -> None:
        self._launcher = launcher

    def launch(self) -> None:
        self._launcher.log_action("translator")
