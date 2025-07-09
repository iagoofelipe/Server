from PySide6.QtWidgets import QApplication
from typing import Sequence

from base.tools import config

from .models.model import AppModel
from .views.view import AppView
from .controllers.controller import AppController

class ChatApp(QApplication):
    def __init__(self, argv:Sequence[str]=None):
        super().__init__()
        config('ChatApp', True, argv=argv)

        self.__model = AppModel()
        self.__view = AppView(self.__model)
        self.__controller = AppController(self.__model, self.__view)

        self.aboutToQuit.connect(self.__controller.close)
    
    def exec(self):
        self.__controller.initialize()

        return super().exec()