from PySide6.QtCore import QObject, Signal

class ServerClient(QObject):

    class Connection(SocketIO):
        def __init__(self, cls):
            super().__init__()
            self.__cls = cls

        def onCommandReceived(self, cmd:str, args):
            ...

        def onConnected(self):
            ...