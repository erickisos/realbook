from time import localtime, strftime

from PySide6.QtCore import QObject, QTimer, Signal


class TimeBackend(QObject):
    timeUpdated = Signal(str, arguments='time')

    def __init__(self):
        super().__init__()
        self.timer = QTimer()
        self.timer.setInterval(100)
        self.timer.timeout.connect(self.update_time)
        self.timer.start()

    def update_time(self):
        self.timeUpdated.emit(self.get_time())

    def get_time(self):
        return strftime('%H:%M:%S', localtime())
