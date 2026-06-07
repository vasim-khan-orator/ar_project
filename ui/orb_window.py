from __future__ import annotations

from PyQt6.QtCore import QEasingCurve, QPropertyAnimation, Qt, pyqtProperty
from PyQt6.QtGui import QColor, QPainter, QPaintEvent, QRadialGradient
from PyQt6.QtWidgets import QWidget


class OrbWindow(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.setFixedSize(240, 240)
        self.setWindowFlags(
            Qt.WindowType.FramelessWindowHint
            | Qt.WindowType.WindowStaysOnTopHint
            | Qt.WindowType.Tool
        )
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground, True)
        self.setAttribute(Qt.WidgetAttribute.WA_NoSystemBackground, True)
        self.setAutoFillBackground(False)
        self.setStyleSheet("background: transparent;")

        self._pulse = 0.0
        self._pulse_animation = QPropertyAnimation(self, b"pulse", self)
        self._pulse_animation.setStartValue(0.0)
        self._pulse_animation.setEndValue(1.0)
        self._pulse_animation.setDuration(2400)
        self._pulse_animation.setEasingCurve(QEasingCurve.Type.InOutSine)
        self._pulse_animation.setLoopCount(-1)
        self._pulse_animation.start()

    def paintEvent(self, event: QPaintEvent) -> None:
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing, True)

        center = self.rect().center().toPointF()
        radius = min(self.width(), self.height()) / 2.0
        pulse_scale = 1.0 + (self._pulse * 0.08)

        glow_gradient = QRadialGradient(center, radius * pulse_scale)
        glow_gradient.setColorAt(0.0, QColor(120, 220, 255, 210))
        glow_gradient.setColorAt(0.5, QColor(70, 160, 255, 110))
        glow_gradient.setColorAt(1.0, QColor(0, 0, 0, 0))

        painter.setPen(Qt.PenStyle.NoPen)
        painter.setBrush(glow_gradient)
        painter.drawEllipse(center, radius * pulse_scale, radius * pulse_scale)

        core_gradient = QRadialGradient(center, radius * 0.6)
        core_gradient.setColorAt(0.0, QColor(190, 245, 255, 210))
        core_gradient.setColorAt(0.6, QColor(90, 190, 255, 170))
        core_gradient.setColorAt(1.0, QColor(20, 60, 120, 70))
        painter.setBrush(core_gradient)
        painter.drawEllipse(center, radius * 0.6, radius * 0.6)

    def get_pulse(self) -> float:
        return self._pulse

    def set_pulse(self, value: float) -> None:
        self._pulse = value
        self.update()

    pulse = pyqtProperty(float, fget=get_pulse, fset=set_pulse)
