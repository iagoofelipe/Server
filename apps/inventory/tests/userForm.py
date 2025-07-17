from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import QTimer

from ..views.forms.userForm import UserForm

class Test:
    def __init__(self):
        self.app = QApplication()
        self.form = UserForm()
        self.win = QMainWindow()
        self.timer = QTimer(self.app)
        
        self.form.continueRequired.connect(self.continueRequired)
        self.form.searchRequired.connect(self.searchRequired)
        self.form.createRequired.connect(self.createRequired)

        self.win.setCentralWidget(self.form.setup())

    def continueRequired(self):
        pass

    def searchRequired(self, cpf:str):
        self.cpf = cpf

        print('searching cpf:', cpf)
        self.timer.singleShot(1000, self.searchFinished)

    def searchFinished(self):
        mode = self.form.MODE_SEARCH_NOT_FOUND

        if self.cpf == '12345678901':
            mode = self.form.MODE_SEARCH_FOUND
            self.form.setName('Iago Carvalho')

        self.form.setMode(mode)

    def createRequired(self, name:str, cpf:str):
        self.cpf = cpf
        print(f'creating {name=} {cpf=}...')
        self.timer.singleShot(1000, self.createFinished)

    def createFinished(self):
        mode = self.form.MODE_CREATE_SUCCESS

        if self.cpf == '12345678901':
            mode = self.form.MODE_CREATE_FAIL
        
        self.form.setMode(mode)



    def exec(self):
        self.win.show()
        self.app.exec()



def test_userForm():
    test = Test()
    test.exec()