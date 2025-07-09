from PySide6.QtCore import QObject, Signal

from base.socketIO import SocketIO

from .consts import *

class ServerClient(QObject):
    messageReceived = Signal(str, str)
    numUsersChanged = Signal(int)

    class Connection(SocketIO):
        def __init__(self, cls):
            super().__init__()
            self.__cls = cls

        def onCommandReceived(self, cmd:str, args):
            if cmd == CMD_MESSAGE:
                self.__cls.messageReceived.emit(args['sender'], args['message'])

            elif cmd == CMD_NUM_USERS:
                self.__cls.numUsersChanged.emit(args['num'])

            return super().onCommandReceived(cmd, args)

    
    def __init__(self, parent:QObject=None):
        super().__init__(parent)
        self.__con = self.Connection(self)

    def sendMessage(self, message:str):
        self.__con.sendCommand(CMD_MESSAGE, {'message': message})

    def initialize(self):
        self.__con.startloop()

    def close(self):
        self.__con.close()