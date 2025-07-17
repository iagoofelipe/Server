from PySide6.QtCore import QObject, Signal, Qt
from PySide6.QtWidgets import QWidget, QTableWidgetItem, QGroupBox, QVBoxLayout, QFormLayout, QLabel, QLineEdit

from ..src.autofiles.ui_InventoryForm import Ui_InventoryForm
from ...backend.consts import UI_ID_INVENTORY_FORM
from ...models.sysinfo import Program

class InventoryForm(QObject):
    UI_ID = UI_ID_INVENTORY_FORM

    saveRequired = Signal(str, str)

    def __init__(self, parent:QObject=None):
        super().__init__(parent)
        self.__ui = Ui_InventoryForm()

    def setup(self, parent:QWidget=None):
        wid = QWidget(parent)

        self.__ui.setupUi(wid)
        self.__machineLayout = QVBoxLayout(self.__ui.widTabSystem)

        self.__ui.btnSave.clicked.connect(self.on_btnSave_clicked)

        return wid
    
    def on_btnSave_clicked(self):
        self.saveRequired.emit(self.__ui.lineName.text(), self.__ui.lineCpf.text())

    def setMachine(self, data:dict[str, dict[str, str]]):
        for className, props in data.items():
            groupBox = QGroupBox(className, self.__ui.widTabSystem)
            layout = QFormLayout(groupBox)

            self.__machineLayout.addWidget(groupBox)

            for k, v in props.items():
                layout.addRow(k, QLabel(v, groupBox))

    def setPrograms(self, data:tuple[Program]):
        table = self.__ui.tablePrograms

        table.setRowCount(len(data))
        for row, program in enumerate(data):
            table.setItem(row, 0, QTableWidgetItem(program.DisplayName))
            table.setItem(row, 1, QTableWidgetItem(program.DisplayVersion))
            table.setItem(row, 2, QTableWidgetItem(program.InstallDate))
            table.setItem(row, 3, QTableWidgetItem(program.Publisher))

        table.sortByColumn(0, Qt.SortOrder.AscendingOrder)
        table.resizeColumnsToContents()

    def setUser(self, name:str, cpf:str):
        self.__ui.lineName.setText(name)
        self.__ui.lineCpf.setText(cpf)

    def setMac(self, mac:str):
        self.__ui.lineMac.setText(mac)

    def getUser(self):
        return dict(name=self.__ui.lineName.text(), cpf=self.__ui.lineCpf.text())
    
    def blockServerSenders(self, arg:bool):
        self.__ui.lineCpf.setDisabled(arg)
        self.__ui.lineName.setDisabled(arg)
        self.__ui.btnSave.setDisabled(arg)