import sys

from PyQt6.QtWidgets import QApplication

from core.overlay_manager import OverlayManager


def main() -> int:
    app = QApplication(sys.argv)
    manager = OverlayManager()
    manager.show()

    return app.exec()


if __name__ == "__main__":
    raise SystemExit(main())
