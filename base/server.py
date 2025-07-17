import socket, os
import logging as log
from typing import Sequence

from base.tools import config
from base.consts import *
from base.socketIO import SocketIO

class Server:
    """ Abstract server class """

    PACKAGE = None
    Client = SocketIO

    def __init__(self, hasDatabase=False, argv:Sequence[str]=None):
        if self.PACKAGE is None:
            raise NotImplementedError('Server.PACKAGE must be set')
        
        config(self.PACKAGE, database=hasDatabase, argv=argv)
        self._pref = f'[{self.PACKAGE}.Server]'
        self._clients:dict[int, SocketIO] = {}
        
        self._ip = os.environ['SERVER_IP']
        self._port = int(os.environ['SERVER_PORT'])

    def sendCommandTo(self, id:int, cmd:str, data=None):
        self._clients[id].sendCommand(cmd, data)

    def sendCommandToAll(self, cmd:str, data=None):
        for client in self._clients.values():
            client.sendCommand(cmd, data)

    def startloop(self):
        """ main loop from the server """

        self.__server = server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # setting up the server
        server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server.bind((self._ip, self._port))
        server.listen(SERVER_MAX_LISTEN)

        log.info(f'{self._pref} listening to {self._ip}:{self._port}')

        # connections loop
        while True:
            try:
                self.onConnectionReceived(*self.__server.accept())

            except KeyboardInterrupt:
                break

        self.close()

    def close(self):
        for client in self._clients.values():
            client.close()
        
        self._clients.clear()

    def onConnectionReceived(self, socket:socket.socket, address:tuple[str, int]) -> None:
        id = address[1]
        self._clients[id] = client = self.Client(socket, id)

        log.info(f"{self._pref} ({id}) client connected")
        client.connect(SocketIO.EVT_CONNECTION_ERROR, self.onClientConnectionError)
        client.connect(SocketIO.EVT_CONNECTION_FINISHED, self.onClientConnectionFinished)
        client.startloop()
    
    def onClientConnectionError(self, client:SocketIO, error:str) -> None: ...

    def onClientConnectionFinished(self, client:SocketIO):
        log.info(f"{self._pref} ({client.id}) removing client from the client's relation...")
        self._clients.pop(client.id)