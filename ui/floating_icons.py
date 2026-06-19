from __future__ import annotations

from PyQt6.QtCore import Qt, pyqtSignal
from PyQt6.QtGui import QIcon, QPainter, QPixmap
from PyQt6.QtSvg import QSvgRenderer
from PyQt6.QtWidgets import QHBoxLayout, QToolButton, QWidget
from pathlib import Path
from typing import Callable

from ui.animations import apply_fade_in


class FloatingIcons(QWidget):
    browser_clicked = pyqtSignal()
    translator_clicked = pyqtSignal()
    attendance_clicked = pyqtSignal()
    object_detection_clicked = pyqtSignal()
    voice_assistant_clicked = pyqtSignal()
    system_menu_clicked = pyqtSignal()
    close_clicked = pyqtSignal()

    def __init__(self) -> None:
        super().__init__()
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground, True)
        self.setAttribute(Qt.WidgetAttribute.WA_Hover, True)
        self.setAutoFillBackground(False)
        self.setStyleSheet("background: transparent;")

        layout = QHBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 24)
        layout.setSpacing(18)

        self._browser = self._build_button("browser", self._svg_browser, "Browser")
        self._translator = self._build_button("translator", self._svg_translator, "Translator")
        self._attendance = self._build_button("attendance", self._svg_attendance, "Attendance")
        self._object_detection = self._build_button(
            "object_detection", self._svg_object_detection, "Object Detection"
        )
        self._voice_assistant = self._build_button("voice_assistant", self._svg_voice_assistant, "Voice Assistant")
        self._system = self._build_button("settings", self._svg_settings, "Settings")
        self._close = self._build_button("close", self._svg_close, "Close")
        # make close button visually distinct (red)
        self._close.setStyleSheet(
            "QToolButton {"
            "  background: rgba(255, 59, 59, 24);"
            "  border: 1px solid rgba(255, 59, 59, 220);"
            "  border-radius: 40px;"
            "}" 
            "QToolButton:hover {"
            "  background: rgba(255, 59, 59, 60);"
            "}"
        )

        self._browser.clicked.connect(self.browser_clicked.emit)
        self._translator.clicked.connect(self.translator_clicked.emit)
        self._attendance.clicked.connect(self.attendance_clicked.emit)
        self._object_detection.clicked.connect(self.object_detection_clicked.emit)
        self._voice_assistant.clicked.connect(self.voice_assistant_clicked.emit)
        self._system.clicked.connect(self.system_menu_clicked.emit)
        self._close.clicked.connect(self.close_clicked.emit)

        for button in (
            self._browser,
            self._translator,
            self._attendance,
            self._object_detection,
            self._voice_assistant,
            self._system,
            self._close,
        ):
            layout.addWidget(button)

        apply_fade_in(self, 900)

    def _build_button(self, name: str, svg_provider: Callable[[], str], tooltip: str) -> QToolButton:
        button = QToolButton(self)
        icon = self._load_icon_by_name(name)
        if icon is None:
            icon = self._render_svg(svg_provider())
        button.setIcon(icon)
        button.setIconSize(QPixmap(36, 36).size())
        button.setToolTip(tooltip)
        button.setCursor(Qt.CursorShape.PointingHandCursor)
        button.setFixedSize(80, 80)
        button.setStyleSheet(
            "QToolButton {"
            "  color: rgb(120, 210, 255);"
            "  background: rgba(120, 210, 255, 20);"
            "  border: 1px solid rgba(120, 210, 255, 200);"
            "  border-radius: 40px;"
            "  font-size: 15px;"
            "  font-weight: 600;"
            "}"
            "QToolButton:hover {"
            "  background: rgba(120, 210, 255, 42);"
            "  border: 1px solid rgba(160, 230, 255, 240);"
            "}"
        )
        return button

    def _load_icon_by_name(self, name: str) -> QIcon | None:
        base = Path(__file__).resolve().parents[1] / "assets" / "icon"
        svg_path = base / f"{name}.svg"
        png_path = base / f"{name}.png"
        if svg_path.exists():
            return QIcon(str(svg_path))
        if png_path.exists():
            return QIcon(str(png_path))
        return None

    @staticmethod
    def _render_svg(svg_markup: str) -> QIcon:
        renderer = QSvgRenderer(bytearray(svg_markup, encoding="utf-8"))
        pixmap = QPixmap(36, 36)
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
    def _svg_object_detection() -> str:
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
    def _svg_voice_assistant() -> str:
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
            "<circle cx='32' cy='32' r='22' fill='none' stroke='#D0F8FF' stroke-width='4'/>"
            "<path d='M32 22v6M32 36v6M22 32h6M36 32h6'"
            " stroke='#D0F8FF' stroke-width='3' fill='none'/>"
            "<circle cx='32' cy='32' r='6' stroke='#D0F8FF' stroke-width='3' fill='none'/>"
            "</svg>"
        )

    @staticmethod
    def _svg_close() -> str:
        return (
            "<svg width='64' height='64' viewBox='0 0 64 64' xmlns='http://www.w3.org/2000/svg'>"
            "<circle cx='32' cy='32' r='22' fill='none' stroke='#FF3B3B' stroke-width='4'/>"
            "<path d='M22 22 L42 42 M42 22 L22 42' stroke='#FF3B3B' stroke-width='4' stroke-linecap='round'/>"
            "</svg>"
        )
