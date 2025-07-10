from PySide6.QtCore import QObject, Signal

from base.socketIO import SocketIO

class ServerClient(QObject):

    class Connection(SocketIO):
        def __init__(self, cls):
            super().__init__()
            self.__cls = cls

