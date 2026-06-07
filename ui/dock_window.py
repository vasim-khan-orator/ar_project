from __future__ import annotations

from PyQt6.QtCore import Qt, pyqtSignal
from PyQt6.QtGui import QIcon, QPainter, QPixmap
from PyQt6.QtSvg import QSvgRenderer
from PyQt6.QtWidgets import QHBoxLayout, QToolButton, QWidget


class DockWindow(QWidget):
    browser_clicked = pyqtSignal()
    translator_clicked = pyqtSignal()
    attendance_clicked = pyqtSignal()
    detection_clicked = pyqtSignal()
    voice_assistant_clicked = pyqtSignal()
    settings_clicked = pyqtSignal()

    def __init__(self) -> None:
        super().__init__()
        self.setWindowFlags(
            Qt.WindowType.FramelessWindowHint
            | Qt.WindowType.WindowStaysOnTopHint
            | Qt.WindowType.Tool
        )
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground, True)
        self.setAttribute(Qt.WidgetAttribute.WA_NoSystemBackground, True)
        self.setAutoFillBackground(False)
        self.setStyleSheet("background: transparent;")

        layout = QHBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(18)

        self._browser = self._build_button(self._svg_browser(), "Browser")
        self._translator = self._build_button(self._svg_translator(), "Translator")
        self._attendance = self._build_button(self._svg_attendance(), "Attendance")
        self._detection = self._build_button(self._svg_detection(), "Object Detection")
        self._voice = self._build_button(self._svg_voice(), "Voice Assistant")
        self._settings = self._build_button(self._svg_settings(), "Settings")

        self._browser.clicked.connect(self.browser_clicked.emit)
        self._translator.clicked.connect(self.translator_clicked.emit)
        self._attendance.clicked.connect(self.attendance_clicked.emit)
        self._detection.clicked.connect(self.detection_clicked.emit)
        self._voice.clicked.connect(self.voice_assistant_clicked.emit)
        self._settings.clicked.connect(self.settings_clicked.emit)

        for button in (
            self._browser,
            self._translator,
            self._attendance,
            self._detection,
            self._voice,
            self._settings,
        ):
            layout.addWidget(button)

        self.adjustSize()

    def _build_button(self, svg_markup: str, tooltip: str) -> QToolButton:
        button = QToolButton(self)
        button.setIcon(self._render_svg(svg_markup))
        button.setIconSize(QPixmap(28, 28).size())
        button.setToolTip(tooltip)
        button.setCursor(Qt.CursorShape.PointingHandCursor)
        button.setFixedSize(60, 60)
        button.setStyleSheet(
            "QToolButton {"
            "  background: rgba(120, 210, 255, 14);"
            "  border: 1px solid rgba(120, 210, 255, 200);"
            "  border-radius: 30px;"
            "}"
            "QToolButton:hover {"
            "  background: rgba(120, 210, 255, 28);"
            "  border: 1px solid rgba(160, 230, 255, 240);"
            "}"
        )
        return button

    @staticmethod
    def _render_svg(svg_markup: str) -> QIcon:
        renderer = QSvgRenderer(bytearray(svg_markup, encoding="utf-8"))
        pixmap = QPixmap(28, 28)
        pixmap.fill(Qt.GlobalColor.transparent)
        painter = QPainter(pixmap)
        renderer.render(painter)
        painter.end()
        return QIcon(pixmap)

    @staticmethod
    def _svg_browser() -> str:
        return (
            "<svg width='64' height='64' viewBox='0 0 64 64' xmlns='http://www.w3.org/2000/svg'>"
            "<circle cx='32' cy='32' r='22' fill='none' stroke='#7AD5FF' stroke-width='4'/>"
            "<path d='M14 32h36M32 10c7 6 10 14 10 22s-3 16-10 22"
            "c-7-6-10-14-10-22s3-16 10-22z'"
            " stroke='#7AD5FF' stroke-width='3' fill='none'/>"
            "</svg>"
        )

    @staticmethod
    def _svg_translator() -> str:
        return (
            "<svg width='64' height='64' viewBox='0 0 64 64' xmlns='http://www.w3.org/2000/svg'>"
            "<circle cx='32' cy='32' r='22' fill='none' stroke='#7AD5FF' stroke-width='4'/>"
            "<path d='M20 24h24M24 20v8m16 4c-4 8-8 12-16 12'"
            " stroke='#7AD5FF' stroke-width='3' fill='none'/>"
            "</svg>"
        )

    @staticmethod
    def _svg_attendance() -> str:
        return (
            "<svg width='64' height='64' viewBox='0 0 64 64' xmlns='http://www.w3.org/2000/svg'>"
            "<circle cx='32' cy='32' r='22' fill='none' stroke='#7AD5FF' stroke-width='4'/>"
            "<circle cx='32' cy='28' r='6' fill='none' stroke='#7AD5FF' stroke-width='3'/>"
            "<path d='M20 46c4-6 20-6 24 0' stroke='#7AD5FF' stroke-width='3' fill='none'/>"
            "</svg>"
        )

    @staticmethod
    def _svg_detection() -> str:
        return (
            "<svg width='64' height='64' viewBox='0 0 64 64' xmlns='http://www.w3.org/2000/svg'>"
            "<circle cx='32' cy='32' r='22' fill='none' stroke='#7AD5FF' stroke-width='4'/>"
            "<rect x='22' y='22' width='20' height='20' rx='4'"
            " stroke='#7AD5FF' stroke-width='3' fill='none'/>"
            "<path d='M18 18h8M38 18h8M18 46h8M38 46h8'"
            " stroke='#7AD5FF' stroke-width='3' fill='none'/>"
            "</svg>"
        )

    @staticmethod
    def _svg_voice() -> str:
        return (
            "<svg width='64' height='64' viewBox='0 0 64 64' xmlns='http://www.w3.org/2000/svg'>"
            "<circle cx='32' cy='32' r='22' fill='none' stroke='#7AD5FF' stroke-width='4'/>"
            "<rect x='28' y='20' width='8' height='18' rx='4'"
            " stroke='#7AD5FF' stroke-width='3' fill='none'/>"
            "<path d='M24 32c0 6 16 6 16 0M28 42h8'"
            " stroke='#7AD5FF' stroke-width='3' fill='none'/>"
            "</svg>"
        )

    @staticmethod
    def _svg_settings() -> str:
        return (
            "<svg width='64' height='64' viewBox='0 0 64 64' xmlns='http://www.w3.org/2000/svg'>"
            "<circle cx='32' cy='32' r='22' fill='none' stroke='#7AD5FF' stroke-width='4'/>"
            "<path d='M32 22v6M32 36v6M22 32h6M36 32h6'"
            " stroke='#7AD5FF' stroke-width='3' fill='none'/>"
            "<circle cx='32' cy='32' r='6' stroke='#7AD5FF' stroke-width='3' fill='none'/>"
            "</svg>"
        )
