from __future__ import annotations

from core.app_launcher import AppLauncher


class VoiceAssistantService:
    def __init__(self, launcher: AppLauncher) -> None:
        self._launcher = launcher

    def launch(self) -> None:
        self._launcher.log_action("voice_assistant")
