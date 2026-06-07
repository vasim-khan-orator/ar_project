from __future__ import annotations

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QVBoxLayout, QLabel, QWidget

from ui.animations import apply_fade_in


class HolographicWidgets(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground, True)
        self.setAutoFillBackground(False)
        self.setStyleSheet("background: transparent;")

        layout = QVBoxLayout(self)
        layout.setContentsMargins(24, 24, 24, 24)
        layout.setSpacing(10)

        for text in (
            "Translator: ready",
            "Attendance: idle",
            "Object detection: standby",
            "Voice assistant: awaiting",
        ):
            label = QLabel(text)
            label.setStyleSheet(
                "color: rgba(120, 210, 255, 200);"
                "font-size: 14px;"
                "font-weight: 500;"
                "background: transparent;"
            )
            layout.addWidget(label)

        apply_fade_in(self, 1200)
