from PySide6.QtCore import QObject, Signal

from base.socketIO import SocketIO

class ServerClient(QObject):
    connected = Signal()
    connectionError = Signal(str)

    class Connection(SocketIO):
        def __init__(self, cls:'ServerClient'):
            super().__init__()
            self.__cls = cls

        def onCommandReceived(self, cmd:str, args):
            return super().onCommandReceived(cmd, args)
        
        def onConnected(self):
            self.__cls.connected.emit()
            return super().onConnected()
        
        def onConnectionError(self, error):
            self.__cls.connectionError.emit(error)
            return super().onConnectionError(error)

    def __init__(self, parent:QObject=None):
        super().__init__(parent)
        self.__con = self.Connection(self)

    def initialize(self):
        self.__con.startloop()

    def close(self):
        self.__con.close()

    def sendSystemData(self, programs, system, user):
        pass