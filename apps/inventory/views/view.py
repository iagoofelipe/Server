from PySide6.QtWidgets import QMainWindow
from PySide6.QtCore import QObject, Signal

from ..models.model import AppModel
from .forms.inventoryForm import InventoryForm
from .forms.alertForm import AlertForm
from .forms.userForm import UserForm

class AppView(QObject):
    def __init__(self, model:AppModel):
        super().__init__()
        self.__currentUi = None
        self.__model = model
        self.__inventoryForm = InventoryForm(self)
        self.__alertForm = AlertForm(self)
        self.__userForm = UserForm(self)
        self.__win = QMainWindow()

        self.__inventoryForm.backRequired.connect(self.on_inventoryForm_backRequired)

    def initialize(self):
        self.setupUiById(self.__alertForm.UI_ID)
        self.__win.setMinimumSize(800, 600)
        self.__win.show()

    def inventoryForm(self): return self.__inventoryForm
    def alertForm(self): return self.__alertForm
    def userForm(self): return self.__userForm

    def showMessage(self, text:str):
        match self.__currentUi:
            case self.__alertForm.UI_ID:
                self.__alertForm.setText(text)
            
            case self.__inventoryForm.UI_ID:
                self.__inventoryForm.setText(text)

            case _:
                self.__win.statusBar().showMessage(text)

    def setupUiById(self, uiId:int):
        if self.__currentUi == uiId:
            return
        
        match uiId:
            case self.__inventoryForm.UI_ID:
                wid = self.__inventoryForm.setup()

            case self.__alertForm.UI_ID:
                wid = self.__alertForm.setup()

            case self.__userForm.UI_ID:
                wid = self.__userForm.setup()

            case _:
                raise ValueError()
        
        self.__currentUi = uiId
        self.__win.setCentralWidget(wid)

    def on_inventoryForm_backRequired(self):
        self.setupUiById(self.__userForm.UI_ID)