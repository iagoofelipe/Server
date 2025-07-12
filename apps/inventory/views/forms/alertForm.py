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
        self.__timer = QTimer(self.__label)

        layout.addWidget(self.__label)
        self.__timer.setInterval(1000)
        self.__timer.timeout.connect(self.on_timer_timeout)
        self.setText('initializing components')

        return wid
    
    def setText(self, arg:str, loadingMode=True):
        timerActive = self.__timer.isActive()

        if loadingMode and not timerActive:
                self.__timer.start()

        if not loadingMode and timerActive:
                self.__timer.stop()

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
