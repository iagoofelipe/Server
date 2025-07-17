# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'UserForm.ui'
##
## Created by: Qt User Interface Compiler version 6.9.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

class Ui_UserForm(object):
    def setupUi(self, UserForm):
        if not UserForm.objectName():
            UserForm.setObjectName(u"UserForm")
        UserForm.resize(527, 491)
        self.verticalLayout = QVBoxLayout(UserForm)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_3 = QLabel(UserForm)
        self.label_3.setObjectName(u"label_3")
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.label_3.setFont(font)

        self.verticalLayout.addWidget(self.label_3)

        self.label_4 = QLabel(UserForm)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout.addWidget(self.label_4)

        self.widget = QWidget(UserForm)
        self.widget.setObjectName(u"widget")
        self.gridLayout = QGridLayout(self.widget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)

        self.lineCpf = QLineEdit(self.widget)
        self.lineCpf.setObjectName(u"lineCpf")

        self.gridLayout.addWidget(self.lineCpf, 0, 1, 1, 1)

        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)

        self.lineName = QLineEdit(self.widget)
        self.lineName.setObjectName(u"lineName")

        self.gridLayout.addWidget(self.lineName, 1, 1, 1, 1)


        self.verticalLayout.addWidget(self.widget)

        self.labelMessage = QLabel(UserForm)
        self.labelMessage.setObjectName(u"labelMessage")

        self.verticalLayout.addWidget(self.labelMessage)

        self.verticalSpacer = QSpacerItem(20, 329, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.widget_2 = QWidget(UserForm)
        self.widget_2.setObjectName(u"widget_2")
        self.horizontalLayout = QHBoxLayout(self.widget_2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.btnClear = QPushButton(self.widget_2)
        self.btnClear.setObjectName(u"btnClear")

        self.horizontalLayout.addWidget(self.btnClear)

        self.btnCreate = QPushButton(self.widget_2)
        self.btnCreate.setObjectName(u"btnCreate")

        self.horizontalLayout.addWidget(self.btnCreate)

        self.btnSearch = QPushButton(self.widget_2)
        self.btnSearch.setObjectName(u"btnSearch")

        self.horizontalLayout.addWidget(self.btnSearch)

        self.btnContinue = QPushButton(self.widget_2)
        self.btnContinue.setObjectName(u"btnContinue")

        self.horizontalLayout.addWidget(self.btnContinue)


        self.verticalLayout.addWidget(self.widget_2)


        self.retranslateUi(UserForm)

        QMetaObject.connectSlotsByName(UserForm)
    # setupUi

    def retranslateUi(self, UserForm):
        UserForm.setWindowTitle(QCoreApplication.translate("UserForm", u"Form", None))
        self.label_3.setText(QCoreApplication.translate("UserForm", u"User", None))
        self.label_4.setText(QCoreApplication.translate("UserForm", u"Provide the user data to continue the process", None))
        self.label_2.setText(QCoreApplication.translate("UserForm", u"CPF", None))
        self.label.setText(QCoreApplication.translate("UserForm", u"Name", None))
        self.labelMessage.setText("")
        self.btnClear.setText(QCoreApplication.translate("UserForm", u"clear", None))
        self.btnCreate.setText(QCoreApplication.translate("UserForm", u"create", None))
        self.btnSearch.setText(QCoreApplication.translate("UserForm", u"search", None))
        self.btnContinue.setText(QCoreApplication.translate("UserForm", u"continue", None))
    # retranslateUi

