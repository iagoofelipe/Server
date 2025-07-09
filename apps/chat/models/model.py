from PySide6.QtCore import QObject, Signal

from ..backend.client import ServerClient

class AppModel(QObject):
    def __init__(self):
        super().__init__()
        self.__client = ServerClient(self)

    def initialize(self):
        self.__client.initialize()

    def close(self):
        self.__client.close()

    @property
    def client(self): return self.__client