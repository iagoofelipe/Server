from base.socketIO import SocketIO
from .database import Database

from .consts import *

class InventoryClient(SocketIO):
    _database = Database()

    def onCommandReceived(self, cmd, args):
        if cmd == CMD_SYSINFO:
            print('saveMachine', args)
            self.sendCommand(CMD_SYSINFO, dict(success=True, error=''))

        elif cmd == CMD_USER_VALIDATE:
            name = self._database.validateUser(args['cpf'])
            valid = name is not None
            self.sendCommand(CMD_USER_VALIDATE, dict(valid=valid, userName=name if valid else ''))

        elif cmd == CMD_USER_CREATE:
            self.sendCommand(CMD_USER_CREATE, dict(success=self._database.createUser(args['name'], args['cpf'])))
        
        return super().onCommandReceived(cmd, args)