from PySide6.QtCore import QObject, Signal

from ..models.model import AppModel
from ..views.view import AppView

class AppController(QObject):
    def __init__(self, model:AppModel, view:AppView):
        super().__init__()
        self.__model = model
        self.__view = view

        # connecting events
        model.client.messageReceived.connect(self.on_client_messageReceived)
        model.client.numUsersChanged.connect(self.on_client_numUsersChanged)
        view.sendMessageRequired.connect(self.on_view_sendMessageRequired)

    def close(self):
        self.__model.close()

    def initialize(self):
        self.__view.initialize()
        self.__model.initialize()

    def on_client_messageReceived(self, sender:str, message:str):
        self.__view.appendMessage(sender, message)

    def on_client_numUsersChanged(self, num:int):
        self.__view.setNumUsers(num)

    def on_view_sendMessageRequired(self, msg:str):
        self.__model.client.sendMessage(msg)