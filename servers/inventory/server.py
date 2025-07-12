"""

Inventory Server - Save machine informations like operating system, product key and etc.
The server links users data with the machine, making a inventory of machines.

"""

from typing import Sequence
import socket

from base.server import Server
from base.socketIO import SocketIO
from base.consts import SERVER_CMD_SEP

CMD_SYSINFO = SERVER_CMD_SEP + 'SYSINFO'

class InventoryServer(Server):
    PACKAGE = 'Inventory'

    def __init__(self, argv:Sequence[str]=None):
        super().__init__(argv=argv)

    #-----------------------------------------------------------------------------------
    # Client Events
    def onClientCommandReceived(self, sender:SocketIO, cmd:str, args):
        if cmd == CMD_SYSINFO:
            print('sysinfo required', args)

    #-----------------------------------------------------------------------------------
    # Server Events
    def onConnectionReceived(self, socket:socket.socket, address:tuple[str, int]):
        super().onConnectionReceived(socket, address)

        id = address[1]
        client = self._clients[id]

        client.connect(SocketIO.EVT_COMMAND_RECEIVED, self.onClientCommandReceived)
    #-----------------------------------------------------------------------------------
