from PySide6.QtCore import QObject, Signal, Qt
from PySide6.QtWidgets import QWidget, QTableWidgetItem, QGroupBox, QVBoxLayout, QFormLayout, QLabel, QLineEdit

from ..src.autofiles.ui_InventoryForm import Ui_InventoryForm
from ...backend.consts import UI_ID_INVENTORY_FORM
from ...models.sysinfo import Program

class InventoryForm(QObject):
    UI_ID = UI_ID_INVENTORY_FORM

    def __init__(self, parent:QObject=None):
        super().__init__(parent)
        self.__ui = Ui_InventoryForm()

    def setup(self, parent:QWidget=None):
        wid = QWidget(parent)

        self.__ui.setupUi(wid)
        self.__systemLayout = QVBoxLayout(self.__ui.widTabSystem)

        return wid
    
    def setSystemData(self, data:dict[str, dict[str, str]]):
        for className, props in data.items():
            groupBox = QGroupBox(className, self.__ui.widTabSystem)
            layout = QFormLayout(groupBox)

            self.__systemLayout.addWidget(groupBox)

            for k, v in props.items():
                layout.addRow(k, QLabel(v, groupBox))
                

    def setProgramsData(self, data:tuple[Program]):
        table = self.__ui.tablePrograms

        table.setRowCount(len(data))
        for row, program in enumerate(data):
            table.setItem(row, 0, QTableWidgetItem(program.DisplayName))
            table.setItem(row, 1, QTableWidgetItem(program.DisplayVersion))
            table.setItem(row, 2, QTableWidgetItem(program.InstallDate))
            table.setItem(row, 3, QTableWidgetItem(program.Publisher))

        table.sortByColumn(0, Qt.SortOrder.AscendingOrder)
        table.resizeColumnsToContents()