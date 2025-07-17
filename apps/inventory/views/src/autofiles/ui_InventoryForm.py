# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'InventoryForm.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QFormLayout, QGroupBox,
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QSpacerItem, QTabWidget,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_InventoryForm(object):
    def setupUi(self, InventoryForm):
        if not InventoryForm.objectName():
            InventoryForm.setObjectName(u"InventoryForm")
        InventoryForm.resize(729, 674)
        self.verticalLayout_3 = QVBoxLayout(InventoryForm)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.groupBox = QGroupBox(InventoryForm)
        self.groupBox.setObjectName(u"groupBox")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.formLayout = QFormLayout(self.groupBox)
        self.formLayout.setObjectName(u"formLayout")
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label)

        self.lineName = QLineEdit(self.groupBox)
        self.lineName.setObjectName(u"lineName")
        self.lineName.setReadOnly(True)

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.lineName)

        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.label_2)

        self.lineCpf = QLineEdit(self.groupBox)
        self.lineCpf.setObjectName(u"lineCpf")
        self.lineCpf.setReadOnly(True)

        self.formLayout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.lineCpf)


        self.verticalLayout_3.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(InventoryForm)
        self.groupBox_2.setObjectName(u"groupBox_2")
        sizePolicy.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy)
        self.formLayout_2 = QFormLayout(self.groupBox_2)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.label_3 = QLabel(self.groupBox_2)
        self.label_3.setObjectName(u"label_3")

        self.formLayout_2.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label_3)

        self.lineMac = QLineEdit(self.groupBox_2)
        self.lineMac.setObjectName(u"lineMac")
        self.lineMac.setReadOnly(True)

        self.formLayout_2.setWidget(0, QFormLayout.ItemRole.FieldRole, self.lineMac)


        self.verticalLayout_3.addWidget(self.groupBox_2)

        self.tabWidget = QTabWidget(InventoryForm)
        self.tabWidget.setObjectName(u"tabWidget")
        self.widTabSystem = QWidget()
        self.widTabSystem.setObjectName(u"widTabSystem")
        self.tabWidget.addTab(self.widTabSystem, "")
        self.widTabPrograms = QWidget()
        self.widTabPrograms.setObjectName(u"widTabPrograms")
        self.verticalLayout_2 = QVBoxLayout(self.widTabPrograms)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.tablePrograms = QTableWidget(self.widTabPrograms)
        if (self.tablePrograms.columnCount() < 4):
            self.tablePrograms.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.tablePrograms.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tablePrograms.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tablePrograms.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tablePrograms.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.tablePrograms.setObjectName(u"tablePrograms")
        self.tablePrograms.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tablePrograms.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tablePrograms.setSelectionBehavior(QAbstractItemView.SelectRows)

        self.verticalLayout_2.addWidget(self.tablePrograms)

        self.tabWidget.addTab(self.widTabPrograms, "")

        self.verticalLayout_3.addWidget(self.tabWidget)

        self.widget = QWidget(InventoryForm)
        self.widget.setObjectName(u"widget")
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.btnSave = QPushButton(self.widget)
        self.btnSave.setObjectName(u"btnSave")

        self.horizontalLayout.addWidget(self.btnSave)


        self.verticalLayout_3.addWidget(self.widget)


        self.retranslateUi(InventoryForm)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(InventoryForm)
    # setupUi

    def retranslateUi(self, InventoryForm):
        InventoryForm.setWindowTitle(QCoreApplication.translate("InventoryForm", u"Form", None))
        self.groupBox.setTitle(QCoreApplication.translate("InventoryForm", u"User", None))
        self.label.setText(QCoreApplication.translate("InventoryForm", u"Name", None))
        self.label_2.setText(QCoreApplication.translate("InventoryForm", u"CPF", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("InventoryForm", u"Machine", None))
        self.label_3.setText(QCoreApplication.translate("InventoryForm", u"MAC", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.widTabSystem), QCoreApplication.translate("InventoryForm", u"System", None))
        ___qtablewidgetitem = self.tablePrograms.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("InventoryForm", u"DisplayName", None));
        ___qtablewidgetitem1 = self.tablePrograms.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("InventoryForm", u"DisplayVersion", None));
        ___qtablewidgetitem2 = self.tablePrograms.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("InventoryForm", u"InstallDate", None));
        ___qtablewidgetitem3 = self.tablePrograms.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("InventoryForm", u"Publisher", None));
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.widTabPrograms), QCoreApplication.translate("InventoryForm", u"Programs", None))
        self.btnSave.setText(QCoreApplication.translate("InventoryForm", u"save", None))
    # retranslateUi

