from __future__ import annotations

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QWidget


class AttendanceWidget(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.setFixedSize(240, 160)
        self.setWindowFlags(
            Qt.WindowType.FramelessWindowHint
            | Qt.WindowType.WindowStaysOnTopHint
            | Qt.WindowType.Tool
        )
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground, True)
        self.setAttribute(Qt.WidgetAttribute.WA_NoSystemBackground, True)
        self.setAutoFillBackground(False)
        self.setStyleSheet("background: transparent;")
        self.hide()
