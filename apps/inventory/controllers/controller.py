from PySide6.QtCore import QObject, Signal

from ..models.model import AppModel
from ..views.view import AppView
from ..backend.consts import UI_ID_INVENTORY_FORM

class AppController(QObject):
    def __init__(self, model:AppModel, view:AppView):
        super().__init__()
        self.__model = model
        self.__view = view

        model.initilizationFinished.connect(self.on_model_initializationFinished)

    def initialize(self):
        self.__view.initialize()
        self.__model.initialize()

    def on_model_initializationFinished(self, success:bool):
        if success:
            form = self.__view.inventoryForm()

            self.__view.setupUiById(UI_ID_INVENTORY_FORM)
            form.setSystemData(self.__model.systemData)
            form.setProgramsData(self.__model.programsData)
        
        else:
            form = self.__view.alertForm()
            form.setText('error')