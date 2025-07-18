"""

Inventory Server - Save machine informations like operating system, product key and etc.
The server links users data with the machine, making a inventory of machines.

"""

from typing import Sequence

from base.server import Server

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
