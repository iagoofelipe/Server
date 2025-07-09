import socket, json, os
from threading import Thread
import logging as log

from base.events import EventDispatcher
from base.consts import *

class SocketIO(EventDispatcher):
    """ manage the socket connection, dispatching events based on commands receivers """

    EVT_CONNECTED = 0               # sender
    EVT_CONNECTION_ERROR = 1        # sender, error:str
    EVT_COMMAND_RECEIVED = 2        # sender, cmd:str, args:list|dict|None
    EVT_CONNECTION_FINISHED = 3     # sender

    def __init__(self, socket:socket.socket=None, id:int=None, pref:str='SocketIO'):
        super().__init__()
        self.__socket = socket
        self.__generateSocket = socket is None
        self.__id = id
        self.__ip = os.environ.get('SERVER_IP')
        self.__port = int(os.environ.get('SERVER_PORT', 0))
        self.__pref = f'[{pref}]' + (f' ({id})' if id is not None else '')
        self.__buffer = ''

    #-----------------------------------------------------------
    # Properties
    @property
    def id(self): return self.__id

    @property
    def preffix(self): return self.__pref

    #-----------------------------------------------------------
    # Events
    def onConnected(self):
        self.emit(self.EVT_CONNECTED, (self, ))

    def onConnectionError(self, error:str):
        self.emit(self.EVT_CONNECTION_ERROR, (self, error))

    def onCommandReceived(self, cmd:str, args) -> None:
        self.emit(self.EVT_COMMAND_RECEIVED, (self, cmd, args))

    def onConnectionFinished(self):
        self.emit(self.EVT_CONNECTION_FINISHED, (self, ))

    #-----------------------------------------------------------
    # Public Methods
    def close(self):
        if self.__socket is None:
            return
        
        self.sendCommand(CMD_CLOSE)
        self.__socket = None

        log.debug(f'{self.__pref} connection closed')


    def startloop(self):
        self.__thread = Thread(target=self.__loop)
        self.__thread.start()
    
    def sendCommand(self, cmd:str, data:list|dict|None=None):
        if data is None:
            str_data = cmd + SERVER_CMD_END
        else:
            str_data = f'{cmd}{SERVER_CMD_SEP}{json.dumps(data)}{SERVER_CMD_END}'
        
        log.info(f'{self.__pref} sending command <{cmd=} {data=}>...')
        self.__socket.sendall(str_data.encode())

    @staticmethod
    def getCommandFromStr(data:str) -> tuple[str, list|dict|None]:
        # getting command and args
        if data.count(SERVER_CMD_SEP) > 1:
            cmd, args = data[1:].split(SERVER_CMD_SEP, 1) # to ignore the first one

            # casting args from str to object
            cmd = SERVER_CMD_SEP + cmd
            args = json.loads(args)
        
        else:
            cmd, args = data, None

        return cmd, args
    
    #-----------------------------------------------------------
    # Private Methods
    def __loop(self):
        if self.__socket is None:
            if not self.__generateSocket:
                return
        
            log.info(f'{self.__pref} initializing connection with address {self.__ip}:{self.__port}...')
            try:
                self.__socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                self.__socket.connect((self.__ip, self.__port))
                log.info(f'{self.__pref} connected with success')
                self.onConnected()

            except Exception as e:
                log.error(f'{self.__pref} could not be connected, error: {e}')
                self.__socket = None
                self.onConnectionError(str(e))
                return
            
        try:
            keepLoop = True

            while keepLoop:
                data = self.__socket.recv(SERVER_BUFFER).decode()
                log.debug(f'{self.__pref} data received "{data}"')

                self.__buffer += data

                if not self.__buffer:
                    log.info(f'{self.__pref} empty data received, stoping loop...')
                    break

                if SERVER_CMD_END not in self.__buffer:
                    continue

                splitted = self.__buffer.split(SERVER_CMD_END)
                index_last = len(splitted) - 1

                for index, d in enumerate(splitted):

                    if index == index_last:
                        self.__buffer = d
                        break

                    if d == CMD_CLOSE:
                        log.info(f'{self.__pref} external close required...')
                        keepLoop = False
                        break

                    self.onCommandReceived(*self.getCommandFromStr(d))

        except Exception as e:
            log.debug(f'{self.__pref} connection error {e}')
            self.onConnectionError(str(e))
        
        if self.__socket is not None:
            self.__socket.close()
            self.__socket = None
        
        self.onConnectionFinished()

    #-----------------------------------------------------------
    