from PySide6.QtCore import QObject, Signal
from PySide6.QtWidgets import QWidget

from ..models.model import AppModel
from .ui.autofiles.ui_chatForm import Ui_ChatForm

class AppView(QObject):
    sendMessageRequired = Signal(str)

    def __init__(self, model:AppModel):
        super().__init__()
        self.__model = model
        self.__ui = Ui_ChatForm()


    def initialize(self):
        self.__wid = QWidget()
        self.__ui.setupUi(self.__wid)
        
        # connecting events
        self.__ui.lineMsg.returnPressed.connect(self.__ui.btnSend.clicked)
        self.__ui.btnSend.clicked.connect(self.on_btnSend_clicked)
        
        self.__wid.show()

    def appendMessage(self, sender:str, message:str):
        self.__ui.text.appendPlainText(f'[{sender}] {message}')

    def setNumUsers(self, num:int):
        self.__ui.label.setText(f'{num} connected users')

    def on_btnSend_clicked(self):
        self.sendMessageRequired.emit(self.__ui.lineMsg.text())
        self.__ui.lineMsg.clear()