from PySide6.QtCore import QObject, Signal

from ..models.model import AppModel
from ..views.view import AppView
from ..backend.consts import UI_ID_INVENTORY_FORM, UI_ID_USER_FORM

class AppController(QObject):
    def __init__(self, model:AppModel, view:AppView):
        super().__init__()
        self.__model = model
        self.__view = view
        server = model.server
        inventoryForm = view.inventoryForm()
        userForm = view.userForm()

        model.initilizationFinished.connect(self.on_model_initializationFinished)
        # model.sysinfoFinished.connect(self.on_model_sysinfoFinished)
        inventoryForm.saveRequired.connect(self.on_inventoryForm_saveRequired)
        userForm.continueRequired.connect(self.on_userForm_continueRequired)
        userForm.searchRequired.connect(self.on_userForm_searchRequired)
        userForm.createRequired.connect(self.on_userForm_createRequired)
        server.validateUserFinished.connect(self.on_server_validateUserFinished)
        server.createUserFinished.connect(self.on_server_createUserFinished)
        server.saveMachineFinished.connect(self.on_server_saveMachineFinished)


    def initialize(self):
        self.__view.initialize()
        self.__model.initialize()

    def on_model_initializationFinished(self, success:bool, error:str):
        if success:
            self.__view.setupUiById(UI_ID_USER_FORM)
            # form = self.__view.inventoryForm()

            # self.__view.setupUiById(UI_ID_INVENTORY_FORM)
            # form.setMachine(self.__model.machine)
            # form.setPrograms(self.__model.programs)
        
        else:
            form = self.__view.alertForm()
            form.setText(error, False)

    def on_inventoryForm_saveRequired(self):
        form = self.__view.inventoryForm()

        self.__view.showMessage('sending data to server...')
        form.blockServerSenders(True)
        self.__model.saveMachine()
        # self.__model.sendToServer(form.getUser())

    def on_server_saveMachineFinished(self, success:bool, error:str):
        if success:
            self.__view.showMessage('data saved with success!')
        
        else:
            self.__view.showMessage('could not save data, error: %s' % error)
            self.__view.inventoryForm().blockServerSenders(False)

    def on_userForm_continueRequired(self, name:str, cpf:str):
        form = self.__view.inventoryForm()
        model = self.__model

        model.setUser(name, cpf)
        self.__view.setupUiById(UI_ID_INVENTORY_FORM)

        form.setMachine(model.machine)
        form.setPrograms(model.programs)
        form.setMac(model.mac)
        form.setUser(name, cpf)

    def on_userForm_searchRequired(self, cpf:str):
        self.__model.server.validateUser(cpf)

    def on_server_validateUserFinished(self, result:bool, userName:str):
        form = self.__view.userForm()

        if result:
            form.setMode(form.MODE_SEARCH_FOUND)
            form.setName(userName)

        else:
            form.setMode(form.MODE_SEARCH_NOT_FOUND)

    def on_userForm_createRequired(self, name:str, cpf:str):
        self.__model.server.createUser(name, cpf)

    def on_server_createUserFinished(self, result:bool):
        form = self.__view.userForm()

        form.setMode(form.MODE_CREATE_SUCCESS if result else form.MODE_CREATE_FAIL)

    def close(self):
        self.__model.close()