# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI/BasicGNGUI.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(600, 532)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 3, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 3, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 2)
        self.label = QtWidgets.QLabel(Form)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.onsetEdit = QtWidgets.QLineEdit(Form)
        self.onsetEdit.setObjectName("onsetEdit")
        self.gridLayout.addWidget(self.onsetEdit, 4, 0, 1, 1)
        self.offsetEdit = QtWidgets.QLineEdit(Form)
        self.offsetEdit.setObjectName("offsetEdit")
        self.gridLayout.addWidget(self.offsetEdit, 4, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 1, 1, 1, 1)
        self.nTrialsEdit = QtWidgets.QLineEdit(Form)
        self.nTrialsEdit.setObjectName("nTrialsEdit")
        self.gridLayout.addWidget(self.nTrialsEdit, 2, 0, 1, 1)
        self.trialLengthEdit = QtWidgets.QLineEdit(Form)
        self.trialLengthEdit.setObjectName("trialLengthEdit")
        self.gridLayout.addWidget(self.trialLengthEdit, 2, 1, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_4.setText(_translate("Form", "Trial Offset"))
        self.label_2.setText(_translate("Form", "Trial Onset"))
        self.label_3.setText(_translate("Form", "Basic Go / No-Go"))
        self.label.setText(_translate("Form", "Number of Trials"))
        self.label_5.setText(_translate("Form", "Trial Length"))
        self.nTrialsEdit.setText(_translate("Form", "1000"))

