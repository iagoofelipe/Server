from PySide6.QtCore import QObject, Signal
from threading import Thread
import logging as log

from .client import ServerClient
from .sysinfo import Program, getPrograms, getProperties
from ..backend.consts import DEFAULT_PROPS

class AppModel(QObject):
    initilizationFinished = Signal(bool)
    
    def __init__(self):
        super().__init__()
        self.__client = ServerClient()

        self.__programs = None
        self.__system = None

    @property
    def programsData(self) -> tuple[Program]: return self.__programs

    @property
    def systemData(self) -> dict[str, dict[str, str]]: return self.__system

    def initialize(self):
        Thread(target=self.__initialize).start()

    def __initialize(self):
        try:
            self.__programs = getPrograms()
            self.__system = {k : getProperties(**values) for k, values in DEFAULT_PROPS.items()}
            success = True

        except Exception as e:
            log.error(f'[AppModel] it was not possible collect the system data, error: {e}')
            self.__programs = None
            self.__system = None
            success = False

        self.initilizationFinished.emit(success)
