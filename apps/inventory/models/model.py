from PySide6.QtCore import QObject, Signal
from threading import Thread
import logging as log

from .client import ServerClient
from .sysinfo import Program, getPrograms, getProperties
from ..backend.consts import DEFAULT_PROPS

class AppModel(QObject):
    initilizationFinished = Signal(bool, str)
    
    def __init__(self):
        super().__init__()
        self.__client = ServerClient()

        self.__programs = None
        self.__system = None

        self.__client.connected.connect(self.on_client_connected)
        self.__client.connectionError.connect(self.on_client_connectionError)

    @property
    def programsData(self) -> tuple[Program]: return self.__programs

    @property
    def systemData(self) -> dict[str, dict[str, str]]: return self.__system

    def initialize(self):
        self.__client.initialize()

    def close(self):
        self.__client.close()

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

        self.initilizationFinished.emit(success, '')

    def on_client_connected(self):
        Thread(target=self.__initialize).start()

    def on_client_connectionError(self, error:str):
        self.initilizationFinished.emit(False, error)
