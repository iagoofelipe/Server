from PySide6.QtCore import QObject, Signal, Qt, QTimer
from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel

from ...backend.consts import UI_ID_ALERT_FORM

class AlertForm(QObject):
    UI_ID = UI_ID_ALERT_FORM

    def __init__(self, parent:QObject=None):
        super().__init__(parent)

    def setup(self, parent:QWidget=None):
        wid = QWidget(parent)
        layout = QVBoxLayout(wid)
        self.__label = QLabel('', wid, alignment=Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter)
        self.setText('initializing components')
        timer = QTimer(self.__label)

        layout.addWidget(self.__label)
        timer.timeout.connect(self.on_timer_timeout)
        timer.start(1000)

        return wid
    
    def setText(self, arg:str):
        self.__count = 0
        self.__initialText = self.__text = arg
        self.__label.setText(arg)

    def on_timer_timeout(self):
        if self.__count == 3:
            self.__text = self.__initialText
            self.__count = 0

        else:
            self.__count += 1
            self.__text += '.'

        self.__label.setText(self.__text)
