"""

Inventory Server - Save machine informations like operating system, product key and etc.
The server links users data with the machine, making a inventory of machines.

"""

from typing import Sequence
import socket
import time
import json

from base.server import Server

from .consts import *
from .client import InventoryClient
from .database import Database

class InventoryServer(Server):
    PACKAGE = 'Inventory'
    Client = InventoryClient
    _database = Database()

    def __init__(self, argv:Sequence[str]=None):
        super().__init__(True, argv=argv)

    def startloop(self):
        if not self._database.initialize():
            return

        return super().startloop()

    #-----------------------------------------------------------------------------------
    # Client Events
    # def onClientCommandReceived(self, sender:InventoryClient, cmd:str, args):
    #     if cmd == CMD_SYSINFO:
    #         print('sysinfo required')

    #         with open('data.json', 'w') as f:
    #             json.dump(args, f, indent=4)

    #         time.sleep(3)
    #         sender.sendCommand(CMD_SYSINFO, {'success': True, 'error': ''})

    #-----------------------------------------------------------------------------------
    # Server Events
    # def onConnectionReceived(self, socket:socket.socket, address:tuple[str, int]):
    #     super().onConnectionReceived(socket, address)

    #     id = address[1]
    #     client = self._clients[id]

    #     client.connect(InventoryClient.EVT_COMMAND_RECEIVED, self.onClientCommandReceived)
    #-----------------------------------------------------------------------------------
