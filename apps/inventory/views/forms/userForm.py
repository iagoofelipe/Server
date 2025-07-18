from PySide6.QtCore import QObject, Signal
from PySide6.QtWidgets import QWidget, QMessageBox

from ..src.autofiles.ui_UserForm import Ui_UserForm
from ...backend.consts import UI_ID_USER_FORM

class UserForm(QObject):
    UI_ID = UI_ID_USER_FORM

    continueRequired = Signal(str, str)     # name, cpf
    searchRequired = Signal(str)            # cpf
    createRequired = Signal(str, str)       # name, cpf

    MODE_INITIAL = 0
    MODE_SEARCH = 1
    MODE_SEARCH_FOUND = 2
    MODE_SEARCH_NOT_FOUND = 3
    MODE_CREATE = 4
    MODE_CREATE_SUCCESS = 5
    MODE_CREATE_FAIL = 6
    MODE_CONTINUE = 7

    __MODE_MSGS = {
        MODE_SEARCH_FOUND: 'Data found with success',
        MODE_SEARCH_NOT_FOUND: 'It was not possible locate the CPF, please create a new user or provide a different value',
        MODE_CREATE_SUCCESS: 'User created with success',
        MODE_CREATE_FAIL: 'It was not possible create the user, please verify the inputs and try again',
    }

    def __init__(self, parent:QObject=None):
        super().__init__(parent)
        self.__ui = Ui_UserForm()
        self.__wid = None

    def setup(self, parent:QWidget=None):
        self.__wid = wid = QWidget(parent)

        self.__ui.setupUi(wid)

        self.__ui.btnContinue.clicked.connect(self.on_btnContinue_clicked)
        self.__ui.btnSearch.clicked.connect(self.on_btnSearch_clicked)
        self.__ui.btnCreate.clicked.connect(self.on_btnCreate_clicked)
        self.__ui.btnClear.clicked.connect(self.on_btnClear_clicked)

        self.setMode(self.MODE_INITIAL)

        return wid
    
    def on_btnContinue_clicked(self):
        self.continueRequired.emit(self.__ui.lineName.text(), self.__ui.lineCpf.text())

    def on_btnSearch_clicked(self):
        cpf = self.__ui.lineCpf.text()
        
        if not self.checkCpf(cpf):
            return
        
        self.setMode(self.MODE_SEARCH)
        self.searchRequired.emit(cpf)

    def on_btnClear_clicked(self):
        self.__ui.lineCpf.clear()
        self.__ui.lineName.clear()
        self.setMode(self.MODE_INITIAL)

    def checkCpf(self, cpf:str):
        if cpf.isdigit() and len(cpf) == 11:
            return True
        
        QMessageBox(QMessageBox.Icon.Warning, 'Validation Error', 'CPF must be eleven numbers!', parent=self.__wid).exec()
        return False

    def on_btnCreate_clicked(self):
        cpf = self.__ui.lineCpf.text()
        name = self.__ui.lineName.text()

        if not self.checkCpf(cpf):
            return
        
        if not name:
            QMessageBox(QMessageBox.Icon.Warning, 'Validation Error', 'Name cannot be empty!', parent=self.__wid).exec()
            return
        
        self.setMode(self.MODE_CREATE)
        self.createRequired.emit(name, cpf)

    def setMode(self, mode:int):
        # create = True
        # search = True
        # _continue = True
        # clear = True
        # cpf = True
        # name = True

        # if mode == self.MODE_INITIAL:
        #     _continue = False
        #     create = False
        #     name = False
        #     clear = False

        # elif mode in (self.MODE_SEARCH_FOUND, self.MODE_CREATE_SUCCESS):
        #     cpf = False
        #     name = False
        #     create = False
        #     search = False

        # elif mode in (self.MODE_SEARCH_NOT_FOUND, self.MODE_CREATE_FAIL):
        #     _continue = False

        # elif mode in (self.MODE_SEARCH, self.MODE_CREATE, self.MODE_CONTINUE):
        #     create = False
        #     search = False
        #     _continue = False
        #     cpf = False
        #     name = False
        #     clear = False

        # else:
        #     raise ValueError()

        # self.__ui.btnCreate.setVisible(create)
        # self.__ui.btnSearch.setVisible(search)
        # self.__ui.btnContinue.setVisible(_continue)
        # self.__ui.btnClear.setVisible(clear)
        # self.__ui.lineCpf.setVisible(cpf)
        # self.__ui.lineName.setVisible(name)

        lineCpf = self.__ui.lineCpf
        lineName = self.__ui.lineName
        labelName = self.__ui.labelName
        btnClear = self.__ui.btnClear
        btnCreate = self.__ui.btnCreate
        btnSearch = self.__ui.btnSearch
        btnContinue = self.__ui.btnContinue

        btns = { btnClear, btnCreate, btnSearch, btnContinue }
        _all = { lineCpf, lineName, labelName } | btns

        if mode == self.MODE_INITIAL:
            lineCpf.setEnabled(True)
            self.__iter('hide', *_all - {lineCpf, btnSearch})
            self.__iter('show', btnSearch)
            self.__iter('setEnabled', lineCpf, btnSearch, args=(True, ))

        elif mode in (self.MODE_SEARCH_FOUND, self.MODE_CREATE_SUCCESS):
            self.__iter('hide', btnCreate, btnSearch)
            self.__iter('show', lineName, labelName, btnClear, btnContinue)
            self.__iter('setEnabled', lineCpf, lineName, args=(False, ))
            self.__iter('setEnabled', btnClear, btnContinue, args=(True, ))

        elif mode in (self.MODE_SEARCH_NOT_FOUND, self.MODE_CREATE_FAIL):
            self.__iter('hide', btnContinue)
            self.__iter('show', *_all - {btnContinue})
            self.__iter('setEnabled', *_all - {labelName, btnContinue}, args=(True, ))

        elif mode == self.MODE_SEARCH:
            self.__iter('hide', *_all - { lineCpf, btnSearch })
            self.__iter('setEnabled', lineCpf, btnSearch, args=(False, ))

        elif mode in (self.MODE_CREATE, self.MODE_CONTINUE):
            objs = {lineCpf, lineName, labelName, btnClear, btnContinue}
            self.__iter('show', *objs)
            self.__iter('hide', *_all - objs)
            self.__iter('setEnabled', *_all - { labelName }, args=(False, ))

        self.__ui.labelMessage.setText(self.__MODE_MSGS.get(mode, ''))

    def setName(self, name:str):
        self.__ui.lineName.setText(name)


    def __iter(self, funcName:str, *wids:QWidget, args:tuple=(), kwargs:dict={}):
        for wid in wids:
            getattr(wid, funcName)(*args, **kwargs)