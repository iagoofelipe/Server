from PySide6.QtCore import QObject, Signal
from threading import Thread
import logging as log

from .client import ServerClient
from .sysinfo import Program, getPrograms, getProperties, getMac
from ..backend.consts import DEFAULT_PROPS

class AppModel(QObject):
    initilizationFinished = Signal(bool, str)
    
    def __init__(self):
        super().__init__()
        self.__client = ServerClient()

        self.__programs = None
        self.__machine = None
        self.__mac = None

        self.setUser('', '')
        self.__client.connected.connect(self.on_client_connected)
        self.__client.connectionError.connect(self.on_client_connectionError)

    @property
    def programs(self) -> tuple[Program]: return self.__programs

    @property
    def mac(self) -> str: return self.__mac

    @property
    def machine(self) -> dict[str, dict[str, str]]: return self.__machine

    @property
    def user(self) -> tuple[str, str]: return self.__name, self.__cpf

    @property
    def server(self): return self.__client

    def saveMachine(self):
        self.__client._saveMachine({'fields': Program._fields,'data': self.programs}, self.machine, self.mac, {'cpf': self.__cpf})

    def initialize(self):
        self.__client.initialize()

    def close(self):
        self.__client.close()

    def setUser(self, name:str, cpf:str):
        self.__name = name
        self.__cpf = cpf

    def __initialize(self):
        success = True
        error = ''

        try:
            self.__programs = getPrograms()
            self.__machine = {k : getProperties(**values) for k, values in DEFAULT_PROPS.items()}
            self.__mac = getMac()

        except Exception as e:
            log.error(f'[AppModel] it was not possible collect the machine data, error: {e}')
            success = False
            error = str(e)

        self.initilizationFinished.emit(success, error)

    def on_client_connected(self):
        Thread(target=self.__initialize).start()

    def on_client_connectionError(self, error:str):
        self.initilizationFinished.emit(False, error)
