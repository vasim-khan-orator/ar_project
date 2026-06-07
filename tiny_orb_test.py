from __future__ import annotations

import sys

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QColor, QPainter, QPaintEvent, QRadialGradient
from PyQt6.QtWidgets import QApplication, QWidget


class TinyOrb(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.setFixedSize(150, 150)
        self.setWindowFlags(
            Qt.WindowType.FramelessWindowHint
            | Qt.WindowType.WindowStaysOnTopHint
            | Qt.WindowType.Tool
        )
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground, True)
        self.setAttribute(Qt.WidgetAttribute.WA_NoSystemBackground, True)
        self.setAutoFillBackground(False)
        self.setStyleSheet("background: transparent;")

    def paintEvent(self, event: QPaintEvent) -> None:
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing, True)

        center = self.rect().center().toPointF()
        radius = min(self.width(), self.height()) / 2.0

        glow = QRadialGradient(center, radius)
        glow.setColorAt(0.0, QColor(120, 220, 255, 220))
        glow.setColorAt(0.5, QColor(70, 160, 255, 120))
        glow.setColorAt(1.0, QColor(0, 0, 0, 0))

        painter.setPen(Qt.PenStyle.NoPen)
        painter.setBrush(glow)
        painter.drawEllipse(center, radius * 0.9, radius * 0.9)


def main() -> int:
    app = QApplication(sys.argv)

    orb = TinyOrb()
    screen = app.primaryScreen()
    if screen is not None:
        screen_rect = screen.availableGeometry()
        orb.move(
            screen_rect.center().x() - orb.width() // 2,
            screen_rect.center().y() - orb.height() // 2,
        )
    orb.show()

    return app.exec()


if __name__ == "__main__":
    raise SystemExit(main())
