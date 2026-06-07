from __future__ import annotations

from PyQt6.QtCore import Qt, pyqtSignal
from PyQt6.QtWidgets import QGridLayout, QWidget

from core.app_launcher import AppLauncher
from services.attendance import AttendanceService
from services.object_detection import ObjectDetectionService
from services.translator import TranslatorService
from services.voice_assistant import VoiceAssistantService
from ui.ai_orb import AiOrb
from ui.floating_icons import FloatingIcons


class WidgetManager(QWidget):
    system_menu_requested = pyqtSignal()

    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__(parent)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground, True)
        self.setAutoFillBackground(False)
        self.setStyleSheet("background: transparent;")

        self._launcher = AppLauncher()
        self._translator = TranslatorService(self._launcher)
        self._attendance = AttendanceService(self._launcher)
        self._object_detection = ObjectDetectionService(self._launcher)
        self._voice_assistant = VoiceAssistantService(self._launcher)

        self._icons = FloatingIcons()
        self._icons.browser_clicked.connect(self._launcher.launch_chrome)
        self._icons.translator_clicked.connect(self._translator.launch)
        self._icons.attendance_clicked.connect(self._attendance.launch)
        self._icons.object_detection_clicked.connect(self._object_detection.launch)
        self._icons.voice_assistant_clicked.connect(self._voice_assistant.launch)
        self._icons.system_menu_clicked.connect(self.system_menu_requested.emit)

        self._orb = AiOrb(self)

        layout = QGridLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)
        layout.addWidget(self._orb, 0, 0, Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter)
        layout.addWidget(self._icons, 1, 0, Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignBottom)

    @property
    def interactive_widget(self) -> QWidget:
        return self._icons
