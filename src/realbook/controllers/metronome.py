import time
from decimal import Decimal
from typing import Optional

from PySide6.QtCore import QObject, Signal, Slot

from ..logic import tempo


class MetronomeBackend(QObject):
    tempoTapped = Signal()
    tempoUpdated = Signal(int, arguments='tempo')

    def __init__(self):
        super().__init__()
        self.__current_tempo = Decimal('90')
        self.__last_timestamp = None

        self.tempoTapped.connect(self.recalc_tempo)

    @Slot()
    def recalc_tempo(self):
        timestamp = Decimal(time.time())
        self.current_tempo = tempo.calculate(timestamp, self.last_timestamp)
        self.last_timestamp = timestamp

    @property
    def current_tempo(self) -> Decimal:
        return self.__current_tempo

    @current_tempo.setter
    def current_tempo(self, new_tempo: Decimal):
        if new_tempo > 20:
            self.__current_tempo += new_tempo
            self.__current_tempo /= Decimal('2')
            self.tempoUpdated.emit(int(self.__current_tempo))

    @property
    def last_timestamp(self) -> Optional[Decimal]:
        return self.__last_timestamp

    @last_timestamp.setter
    def last_timestamp(self, timestamp: Decimal):
        self.__last_timestamp = timestamp
