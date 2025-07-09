from typing import Sequence
import socket
import logging as log

from base.server import Server
from base.socketIO import SocketIO
from base.consts import SERVER_CMD_SEP

CMD_MESSAGE = SERVER_CMD_SEP + 'MESSAGE'
CMD_NUM_USERS = SERVER_CMD_SEP + 'NUM_USERS'

class ChatServer(Server):
    PACKAGE = 'Chat'

    def __init__(self, argv:Sequence[str]=None):
        super().__init__(argv=argv)

    #-----------------------------------------------------------------------------------
    # Client Events
    def onClientCommandReceived(self, sender:SocketIO, cmd:str, args):
        if cmd == CMD_MESSAGE:
            self.sendCommandToAll(cmd=CMD_MESSAGE, data={'sender': str(sender.id), 'message': args['message']})

        elif cmd == CMD_NUM_USERS:
            self.sendCommandTo(sender.id, data={'num': len(self._clients)})
        
        else:
            log.warning(f'{self._pref} undefined cmd received <{cmd=} {args=}>')

    #-----------------------------------------------------------------------------------
    # Server Events
    def onConnectionReceived(self, socket:socket.socket, address:tuple[str, int]):
        super().onConnectionReceived(socket, address)

        id = address[1]
        client = self._clients[id]

        client.connect(SocketIO.EVT_COMMAND_RECEIVED, self.onClientCommandReceived)

        self.sendCommandToAll(cmd=CMD_MESSAGE, data={'sender': 'SERVER', 'message': f'a new connection has been made! User id {id}'})
        self.sendCommandToAll(cmd=CMD_NUM_USERS, data={'num': len(self._clients)})


    def onClientConnectionFinished(self, client:SocketIO):
        super().onClientConnectionFinished(client)

        self.sendCommandToAll(cmd=CMD_MESSAGE, data={'sender': 'SERVER', 'message': f'the user id {client.id} just left the server'})
        self.sendCommandToAll(cmd=CMD_NUM_USERS, data={'num': len(self._clients)})
    
    #-----------------------------------------------------------------------------------
    