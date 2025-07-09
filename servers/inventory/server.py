"""

Inventory Server - Save machine informations like operating system, product key and etc.
The server links users data with the machine, making a inventory of machines.

"""

from typing import Sequence

from base.server import Server
from base.socketIO import SocketIO

class InventoryServer(Server):
    PACKAGE = 'Inventory'

    def __init__(self, argv:Sequence[str]=None):
        super().__init__(argv=argv)

    #-----------------------------------------------------------------------------------
    # Client Events
    def onClientCommandReceived(self, sender:SocketIO, cmd:str, args):
        ...

    #-----------------------------------------------------------------------------------