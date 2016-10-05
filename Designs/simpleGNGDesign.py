# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI/SimpleGNGUI.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(556, 532)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 4, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 4)
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 4, 2, 1, 1)
        self.label = QtWidgets.QLabel(Form)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 4, 0, 1, 1)
        self.trialLengthEdit = QtWidgets.QLineEdit(Form)
        self.trialLengthEdit.setObjectName("trialLengthEdit")
        self.gridLayout.addWidget(self.trialLengthEdit, 5, 1, 1, 1)
        self.nTrialsEdit = QtWidgets.QLineEdit(Form)
        self.nTrialsEdit.setObjectName("nTrialsEdit")
        self.gridLayout.addWidget(self.nTrialsEdit, 5, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 4, 3, 1, 1)
        self.onsetEdit = QtWidgets.QLineEdit(Form)
        self.onsetEdit.setObjectName("onsetEdit")
        self.gridLayout.addWidget(self.onsetEdit, 5, 2, 1, 1)
        self.lickFractionEdit = QtWidgets.QLineEdit(Form)
        self.lickFractionEdit.setObjectName("lickFractionEdit")
        self.gridLayout.addWidget(self.lickFractionEdit, 5, 4, 1, 1)
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 4, 4, 1, 1)
        self.offsetEdit = QtWidgets.QLineEdit(Form)
        self.offsetEdit.setObjectName("offsetEdit")
        self.gridLayout.addWidget(self.offsetEdit, 5, 3, 1, 1)
        self.reverseValenceCheck = QtWidgets.QCheckBox(Form)
        self.reverseValenceCheck.setText("")
        self.reverseValenceCheck.setObjectName("reverseValenceCheck")
        self.gridLayout.addWidget(self.reverseValenceCheck, 5, 5, 1, 1)
        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 4, 5, 1, 1)
        self.line_2 = QtWidgets.QFrame(Form)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.gridLayout.addWidget(self.line_2, 3, 0, 1, 6)
        self.label_13 = QtWidgets.QLabel(Form)
        self.label_13.setObjectName("label_13")
        self.gridLayout.addWidget(self.label_13, 2, 0, 1, 6)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_5.setText(_translate("Form", "Trial Length (s)"))
        self.label_3.setText(_translate("Form", "Simple Go / No-Go"))
        self.label_2.setText(_translate("Form", "Trial Onset (s)"))
        self.label.setText(_translate("Form", "Number of Trials"))
        self.trialLengthEdit.setText(_translate("Form", "2.0"))
        self.nTrialsEdit.setText(_translate("Form", "300"))
        self.label_4.setText(_translate("Form", "Trial Offset (s)"))
        self.onsetEdit.setText(_translate("Form", "0.1"))
        self.lickFractionEdit.setText(_translate("Form", "0.1"))
        self.label_6.setText(_translate("Form", "Lick Fraction"))
        self.offsetEdit.setText(_translate("Form", "0.1"))
        self.label_7.setText(_translate("Form", "Reverse Valence"))
        self.label_13.setText(_translate("Form", "Valve Map Setup : 1 = Odour 1, 2 = Odour 2"))

