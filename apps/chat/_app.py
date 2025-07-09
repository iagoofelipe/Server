from PySide6.QtWidgets import QApplication, QWidget
from PySide6.QtCore import QObject, Signal
from typing import Sequence

from base.socketIO import SocketIO
from base.consts import SERVER_CMD_SEP
from base.tools import config

from .autofiles.ui_chatForm import Ui_ChatForm

CMD_MESSAGE = SERVER_CMD_SEP + 'MESSAGE'
CMD_NUM_USERS = SERVER_CMD_SEP + 'NUM_USERS'

class QClient(QObject):
    messageReceived = Signal(str, str)
    numUsersChanged = Signal(int)

    def __init__(self):
        super().__init__()

class ChatAppClient(SocketIO):
    # EVT_MESSAGE_RECEIVED = 100
    # EVT_NUM_USERS_CHANGED = 101

    def __init__(self, events:QClient):
        super().__init__(pref='ChatAppClient')
        self.__evts = events

    def onCommandReceived(self, cmd:str, args):
        super().onCommandReceived(cmd, args)
        
        if cmd == CMD_MESSAGE:
            self.__evts.messageReceived.emit(args['sender'], args['message'])

        elif cmd == CMD_NUM_USERS:
            self.__evts.numUsersChanged.emit(args['num'])

class Window:
    def __init__(self, events:QClient, client:ChatAppClient):
        self.__ui = Ui_ChatForm()
        self.__wid = QWidget()
        self.__client = client
        self.__evts = events

        self.__evts.messageReceived.connect(self.on_messageReceived)
        self.__evts.numUsersChanged.connect(self.on_numUsersChanged)


    def exec(self):
        self.__ui.setupUi(self.__wid)

        self.__ui.lineMsg.returnPressed.connect(self.__ui.btnSend.clicked)
        self.__ui.btnSend.clicked.connect(self.on_btnSend_clicked)
        self.__wid.show()

    def on_btnSend_clicked(self):
        msg = self.__ui.lineMsg.text()
        self.__client.sendCommand(CMD_MESSAGE, {'message': msg})
        self.__ui.lineMsg.setText('')

    def on_messageReceived(self, sender:str, message:str):
        self.__ui.textLog.appendPlainText(f'[{sender}] {message}')

    def on_numUsersChanged(self, num:int):
        self.__ui.label.setText(f'Server Chat - {num} connected users')

class ChatApp:
    def __init__(self, argv:Sequence[str]=None):
        config('ChatApp', True, argv=argv)
        
        self.__evts = QClient()
        self.__client = ChatAppClient(self.__evts)
        self.__app = QApplication()
        self.__win = Window(self.__evts, self.__client)

        self.__app.aboutToQuit.connect(self.on_exitRequired)

    def on_exitRequired(self):
        self.__client.close()

    def exec(self):
        self.__win.exec()
        self.__client.startloop()
        self.__app.exec()