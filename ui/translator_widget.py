from __future__ import annotations

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QWidget


class TranslatorWidget(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.setFixedSize(280, 180)
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

    def show_centered(self) -> None:
        screen = QApplication.primaryScreen()
        if screen is not None:
            screen_rect = screen.availableGeometry()
            self.move(
                screen_rect.center().x() - self.width() // 2,
                screen_rect.center().y() - self.height() // 2 + 140,
            )
        self.show()
