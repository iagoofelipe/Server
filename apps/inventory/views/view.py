from PySide6.QtWidgets import QMainWindow
from PySide6.QtCore import QObject, Signal

from ..models.model import AppModel
from .forms.inventoryForm import InventoryForm
from .forms.alertForm import AlertForm

class AppView(QObject):
    def __init__(self, model:AppModel):
        super().__init__()
        self.__model = model
        self.__inventoryForm = InventoryForm(self)
        self.__alertForm = AlertForm(self)
        self.__win = QMainWindow()

    def initialize(self):
        self.setupUiById(self.__alertForm.UI_ID)
        self.__win.setMinimumSize(800, 600)
        self.__win.show()

    def inventoryForm(self): return self.__inventoryForm
    def alertForm(self): return self.__alertForm

    def setupUiById(self, uiId:int):
        match uiId:
            case self.__inventoryForm.UI_ID:
                wid = self.__inventoryForm.setup()

            case self.__alertForm.UI_ID:
                wid = self.__alertForm.setup()

            case _:
                raise ValueError()
        
        self.__win.setCentralWidget(wid)