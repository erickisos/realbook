import sys

from PySide6.QtCore import QUrl
from PySide6.QtQml import QQmlApplicationEngine
from PySide6.QtWidgets import QApplication

from .controllers.time import TimeBackend


def main():
    app = QApplication(sys.argv)
    engine = QQmlApplicationEngine()

    engine.load(QUrl('qml/main.qml'))

    time_backend = TimeBackend()
    engine.rootObjects()[0].setProperty('timeBackend', time_backend)

    if not engine.rootObjects():
        sys.exit(-1)

    time_backend.update_time()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
