# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI/ConcGNGUI.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(541, 532)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 3, 3, 1, 1)
        self.label = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 7)
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 7)
        self.line = QtWidgets.QFrame(Form)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout.addWidget(self.line, 2, 0, 1, 7)
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 3, 2, 1, 1)
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 3, 1, 1, 1)
        self.label_9 = QtWidgets.QLabel(Form)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 3, 6, 1, 1)
        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 3, 4, 1, 1)
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 3, 0, 1, 1)
        self.label_8 = QtWidgets.QLabel(Form)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 3, 5, 1, 1)
        self.nTrialsEdit = QtWidgets.QLineEdit(Form)
        self.nTrialsEdit.setObjectName("nTrialsEdit")
        self.gridLayout.addWidget(self.nTrialsEdit, 4, 0, 1, 1)
        self.trialLengthEdit = QtWidgets.QLineEdit(Form)
        self.trialLengthEdit.setObjectName("trialLengthEdit")
        self.gridLayout.addWidget(self.trialLengthEdit, 4, 1, 1, 1)
        self.onsetEdit = QtWidgets.QLineEdit(Form)
        self.onsetEdit.setObjectName("onsetEdit")
        self.gridLayout.addWidget(self.onsetEdit, 4, 2, 1, 1)
        self.offsetEdit = QtWidgets.QLineEdit(Form)
        self.offsetEdit.setObjectName("offsetEdit")
        self.gridLayout.addWidget(self.offsetEdit, 4, 3, 1, 1)
        self.minConcEdit = QtWidgets.QLineEdit(Form)
        self.minConcEdit.setObjectName("minConcEdit")
        self.gridLayout.addWidget(self.minConcEdit, 4, 4, 1, 1)
        self.lickFractionEdit = QtWidgets.QLineEdit(Form)
        self.lickFractionEdit.setObjectName("lickFractionEdit")
        self.gridLayout.addWidget(self.lickFractionEdit, 4, 5, 1, 1)
        self.reverseValenceCheck = QtWidgets.QCheckBox(Form)
        self.reverseValenceCheck.setText("")
        self.reverseValenceCheck.setObjectName("reverseValenceCheck")
        self.gridLayout.addWidget(self.reverseValenceCheck, 4, 6, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_6.setText(_translate("Form", "Trial Offset (s)"))
        self.label.setText(_translate("Form", "Random Concentration Go/No-Go"))
        self.label_2.setText(_translate("Form", "Valve Map Setup : 1 = Odour, 2 = Odour 2"))
        self.label_5.setText(_translate("Form", "Trial Onset (s)"))
        self.label_4.setText(_translate("Form", "Trial Length (s)"))
        self.label_9.setText(_translate("Form", "Reverse Valence"))
        self.label_7.setText(_translate("Form", "Min. Conc."))
        self.label_3.setText(_translate("Form", "Number of Trials"))
        self.label_8.setText(_translate("Form", "Lick Fraction"))
        self.nTrialsEdit.setText(_translate("Form", "300"))
        self.trialLengthEdit.setText(_translate("Form", "2.0"))
        self.onsetEdit.setText(_translate("Form", "0.1"))
        self.offsetEdit.setText(_translate("Form", "0.1"))
        self.minConcEdit.setText(_translate("Form", "0.5"))
        self.lickFractionEdit.setText(_translate("Form", "0.1"))

