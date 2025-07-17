from PySide6.QtCore import QObject, Signal

from base.socketIO import SocketIO
from ..backend.consts import *

class ServerClient(QObject):
    connected = Signal()
    connectionError = Signal(str)
    saveMachineFinished = Signal(bool, str) # success, error
    validateUserFinished = Signal(bool, str) # success, userName
    createUserFinished = Signal(bool)

    class Connection(SocketIO):
        def __init__(self, cls:'ServerClient'):
            super().__init__()
            self.__cls = cls

        def onCommandReceived(self, cmd:str, args):
            if cmd == CMD_SYSINFO:
                self.__cls.saveMachineFinished.emit(args['success'], args['error'])

            elif cmd == CMD_USER_VALIDATE:
                self.__cls.validateUserFinished.emit(args['valid'], args['userName'])

            elif cmd == CMD_USER_CREATE:
                self.__cls.createUserFinished.emit(args['success'])

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

    def validateUser(self, cpf:str):
        self.__con.sendCommand(CMD_USER_VALIDATE, {'cpf': cpf})
    
    def createUser(self, name:str, cpf:str):
        self.__con.sendCommand(CMD_USER_CREATE, {'name': name, 'cpf': cpf})

    def _saveMachine(self, programs, machine, mac, user):
        self.__con.sendCommand(CMD_SYSINFO, dict(programs=programs, machine=machine, mac=mac, user=user))
