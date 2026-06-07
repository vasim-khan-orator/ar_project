from __future__ import annotations

from PyQt6.QtCore import QObject
from PyQt6.QtWidgets import QApplication

from core.app_launcher import AppLauncher
from ui.dock_window import DockWindow
from ui.orb_window import OrbWindow
from ui.translator_widget import TranslatorWidget


class OverlayManager(QObject):
    def __init__(self) -> None:
        super().__init__()
        self._launcher = AppLauncher()

        self._orb_window = OrbWindow()
        self._dock_window = DockWindow()
        self._translator_widget = TranslatorWidget()

        self._dock_window.browser_clicked.connect(self._launcher.launch_chrome)
        self._dock_window.translator_clicked.connect(self._show_translator)

    def show(self) -> None:
        self._position_windows()
        self._orb_window.show()
        self._dock_window.show()

    def _position_windows(self) -> None:
        screen = QApplication.primaryScreen()
        if screen is None:
            return

        screen_rect = screen.availableGeometry()
        self._orb_window.move(
            screen_rect.center().x() - self._orb_window.width() // 2,
            screen_rect.center().y() - self._orb_window.height() // 2,
        )
        self._dock_window.move(
            screen_rect.center().x() - self._dock_window.width() // 2,
            screen_rect.bottom() - self._dock_window.height() - 40,
        )

    def _show_translator(self) -> None:
        self._translator_widget.show_centered()
