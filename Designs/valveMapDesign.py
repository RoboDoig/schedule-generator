# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI/ValveMapUI.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(583, 189)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.valveValenceTable = QtWidgets.QTableWidget(Form)
        self.valveValenceTable.setColumnCount(8)
        self.valveValenceTable.setObjectName("valveValenceTable")
        self.valveValenceTable.setRowCount(1)
        item = QtWidgets.QTableWidgetItem()
        self.valveValenceTable.setVerticalHeaderItem(0, item)
        self.valveValenceTable.horizontalHeader().setCascadingSectionResizes(False)
        self.valveValenceTable.horizontalHeader().setDefaultSectionSize(31)
        self.valveValenceTable.horizontalHeader().setSortIndicatorShown(False)
        self.valveValenceTable.horizontalHeader().setStretchLastSection(False)
        self.valveValenceTable.verticalHeader().setStretchLastSection(False)
        self.gridLayout.addWidget(self.valveValenceTable, 1, 0, 1, 1)
        self.valveNumberSelect = QtWidgets.QSpinBox(Form)
        self.valveNumberSelect.setMinimum(1)
        self.valveNumberSelect.setProperty("value", 8)
        self.valveNumberSelect.setObjectName("valveNumberSelect")
        self.gridLayout.addWidget(self.valveNumberSelect, 0, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        item = self.valveValenceTable.verticalHeaderItem(0)
        item.setText(_translate("Form", "Valence"))

