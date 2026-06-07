from __future__ import annotations

from PyQt6.QtCore import QEasingCurve, QPropertyAnimation
from PyQt6.QtWidgets import QGraphicsDropShadowEffect, QGraphicsOpacityEffect, QWidget


def apply_fade_in(widget: QWidget, duration_ms: int = 700) -> None:
    effect = QGraphicsOpacityEffect(widget)
    effect.setOpacity(0.0)
    widget.setGraphicsEffect(effect)

    animation = QPropertyAnimation(effect, b"opacity", widget)
    animation.setStartValue(0.0)
    animation.setEndValue(1.0)
    animation.setDuration(duration_ms)
    animation.setEasingCurve(QEasingCurve.Type.OutCubic)
    animation.start(QPropertyAnimation.DeletionPolicy.DeleteWhenStopped)


def apply_pulse_glow(widget: QWidget, base_radius: int = 12, peak_radius: int = 22) -> None:
    shadow = QGraphicsDropShadowEffect(widget)
    shadow.setBlurRadius(base_radius)
    shadow.setOffset(0, 0)
    shadow.setColor(widget.palette().highlight().color())
    widget.setGraphicsEffect(shadow)

    animation = QPropertyAnimation(shadow, b"blurRadius", widget)
    animation.setStartValue(base_radius)
    animation.setEndValue(peak_radius)
    animation.setDuration(1800)
    animation.setEasingCurve(QEasingCurve.Type.InOutSine)
    animation.setLoopCount(-1)
    animation.start()
