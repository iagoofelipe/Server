import logging as log

from base.socketIO import SocketIO
from .database import Database

from .consts import *

class InventoryClient(SocketIO):
    _database = Database()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__userId = None

    def onCommandReceived(self, cmd, args):
        if cmd == CMD_MACHINE_DATA:
            log.info(f'{self.preffix} saving machine data <Machine mac={args['mac']}>...')
            
            success = self._database.newMachine(self.__userId, args)
            self.sendCommand(CMD_MACHINE_DATA, dict(success=success, error=''))

        elif cmd == CMD_USER_VALIDATE:
            cpf = args['cpf']
            r = self._database.validateUser(cpf)
            valid = r is not None
            self.__userId, name = r if valid else (None, None)

            log.info(f'{self.preffix} validating user <User {cpf=}> result: {valid=} id={self.__userId}')
            self.sendCommand(CMD_USER_VALIDATE, dict(valid=valid, name=name))

        elif cmd == CMD_USER_CREATE:
            name = args['name']
            cpf = args['cpf']
            success = self._database.createUser(name, cpf)

            log.info(f'{self.preffix} create user <User {name=} {cpf=}>, success {success}')
            self.sendCommand(CMD_USER_CREATE, dict(success=success))
        
        return super().onCommandReceived(cmd, args)