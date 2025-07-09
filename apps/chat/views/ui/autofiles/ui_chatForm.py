# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'chatForm.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QLineEdit,
    QPlainTextEdit, QPushButton, QSizePolicy, QTabWidget,
    QVBoxLayout, QWidget)

class Ui_ChatForm(object):
    def setupUi(self, ChatForm):
        if not ChatForm.objectName():
            ChatForm.setObjectName(u"ChatForm")
        ChatForm.resize(680, 599)
        self.verticalLayout = QVBoxLayout(ChatForm)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(ChatForm)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.widget_2 = QWidget(ChatForm)
        self.widget_2.setObjectName(u"widget_2")
        self.horizontalLayout_2 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.lineEdit = QLineEdit(self.widget_2)
        self.lineEdit.setObjectName(u"lineEdit")

        self.horizontalLayout_2.addWidget(self.lineEdit)

        self.btnSearch = QPushButton(self.widget_2)
        self.btnSearch.setObjectName(u"btnSearch")

        self.horizontalLayout_2.addWidget(self.btnSearch)


        self.verticalLayout.addWidget(self.widget_2)

        self.tabWidget = QTabWidget(ChatForm)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.verticalLayout_2 = QVBoxLayout(self.tab)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.text = QPlainTextEdit(self.tab)
        self.text.setObjectName(u"text")
        self.text.setReadOnly(True)

        self.verticalLayout_2.addWidget(self.text)

        self.tabWidget.addTab(self.tab, "")

        self.verticalLayout.addWidget(self.tabWidget)

        self.widget = QWidget(ChatForm)
        self.widget.setObjectName(u"widget")
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.lineMsg = QLineEdit(self.widget)
        self.lineMsg.setObjectName(u"lineMsg")

        self.horizontalLayout.addWidget(self.lineMsg)

        self.btnSend = QPushButton(self.widget)
        self.btnSend.setObjectName(u"btnSend")

        self.horizontalLayout.addWidget(self.btnSend)


        self.verticalLayout.addWidget(self.widget)

        QWidget.setTabOrder(self.lineEdit, self.btnSearch)
        QWidget.setTabOrder(self.btnSearch, self.tabWidget)
        QWidget.setTabOrder(self.tabWidget, self.text)
        QWidget.setTabOrder(self.text, self.lineMsg)
        QWidget.setTabOrder(self.lineMsg, self.btnSend)

        self.retranslateUi(ChatForm)

        QMetaObject.connectSlotsByName(ChatForm)
    # setupUi

    def retranslateUi(self, ChatForm):
        ChatForm.setWindowTitle(QCoreApplication.translate("ChatForm", u"Form", None))
        self.label.setText(QCoreApplication.translate("ChatForm", u"0 connected users", None))
        self.lineEdit.setText("")
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("ChatForm", u"Chat...", None))
        self.btnSearch.setText(QCoreApplication.translate("ChatForm", u"search", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("ChatForm", u"Server", None))
        self.lineMsg.setPlaceholderText(QCoreApplication.translate("ChatForm", u"Type a message...", None))
        self.btnSend.setText(QCoreApplication.translate("ChatForm", u"send", None))
    # retranslateUi

