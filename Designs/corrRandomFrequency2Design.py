# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI/CorrRandomFrequency2UI.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1730, 1093)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.line_3 = QtWidgets.QFrame(Form)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.gridLayout.addWidget(self.line_3, 12, 0, 1, 4)
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 4, 2, 1, 1)
        self.line_2 = QtWidgets.QFrame(Form)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.gridLayout.addWidget(self.line_2, 3, 0, 1, 4)
        self.nTrialsEdit = QtWidgets.QLineEdit(Form)
        self.nTrialsEdit.setObjectName("nTrialsEdit")
        self.gridLayout.addWidget(self.nTrialsEdit, 5, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 4, 1, 1, 1)
        self.label = QtWidgets.QLabel(Form)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 4, 0, 1, 1)
        self.label_10 = QtWidgets.QLabel(Form)
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 8, 2, 1, 1)
        self.label_13 = QtWidgets.QLabel(Form)
        self.label_13.setObjectName("label_13")
        self.gridLayout.addWidget(self.label_13, 2, 0, 1, 4)
        self.onsetEdit = QtWidgets.QLineEdit(Form)
        self.onsetEdit.setObjectName("onsetEdit")
        self.gridLayout.addWidget(self.onsetEdit, 5, 2, 1, 1)
        self.label_3 = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 4)
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 4, 3, 1, 1)
        self.offsetEdit = QtWidgets.QLineEdit(Form)
        self.offsetEdit.setObjectName("offsetEdit")
        self.gridLayout.addWidget(self.offsetEdit, 5, 3, 1, 1)
        self.line = QtWidgets.QFrame(Form)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout.addWidget(self.line, 6, 0, 1, 4)
        self.trialLengthEdit = QtWidgets.QLineEdit(Form)
        self.trialLengthEdit.setObjectName("trialLengthEdit")
        self.gridLayout.addWidget(self.trialLengthEdit, 5, 1, 1, 1)
        self.label_11 = QtWidgets.QLabel(Form)
        self.label_11.setObjectName("label_11")
        self.gridLayout.addWidget(self.label_11, 13, 2, 1, 1)
        self.hzUpperBand1Edit = QtWidgets.QLineEdit(Form)
        self.hzUpperBand1Edit.setObjectName("hzUpperBand1Edit")
        self.gridLayout.addWidget(self.hzUpperBand1Edit, 9, 1, 1, 1)
        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 13, 3, 1, 1)
        self.hzLowerEdit = QtWidgets.QLineEdit(Form)
        self.hzLowerEdit.setObjectName("hzLowerEdit")
        self.gridLayout.addWidget(self.hzLowerEdit, 9, 0, 1, 1)
        self.label_8 = QtWidgets.QLabel(Form)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 8, 3, 1, 1)
        self.shatterHzEdit = QtWidgets.QLineEdit(Form)
        self.shatterHzEdit.setObjectName("shatterHzEdit")
        self.gridLayout.addWidget(self.shatterHzEdit, 9, 3, 1, 1)
        self.nControlTrialsEdit = QtWidgets.QLineEdit(Form)
        self.nControlTrialsEdit.setObjectName("nControlTrialsEdit")
        self.gridLayout.addWidget(self.nControlTrialsEdit, 14, 2, 1, 1)
        self.label_12 = QtWidgets.QLabel(Form)
        self.label_12.setObjectName("label_12")
        self.gridLayout.addWidget(self.label_12, 8, 0, 1, 1)
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 13, 0, 1, 1)
        self.label_9 = QtWidgets.QLabel(Form)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 8, 1, 1, 1)
        self.fractionSimpleTrialsEdit = QtWidgets.QLineEdit(Form)
        self.fractionSimpleTrialsEdit.setObjectName("fractionSimpleTrialsEdit")
        self.gridLayout.addWidget(self.fractionSimpleTrialsEdit, 14, 3, 1, 1)
        self.lickFractionEdit = QtWidgets.QLineEdit(Form)
        self.lickFractionEdit.setObjectName("lickFractionEdit")
        self.gridLayout.addWidget(self.lickFractionEdit, 14, 0, 1, 1)
        self.spCorrelatedCheck = QtWidgets.QCheckBox(Form)
        self.spCorrelatedCheck.setText("")
        self.spCorrelatedCheck.setChecked(True)
        self.spCorrelatedCheck.setObjectName("spCorrelatedCheck")
        self.gridLayout.addWidget(self.spCorrelatedCheck, 9, 2, 1, 1)
        self.hzUpperBand2Edit = QtWidgets.QLineEdit(Form)
        self.hzUpperBand2Edit.setObjectName("hzUpperBand2Edit")
        self.gridLayout.addWidget(self.hzUpperBand2Edit, 10, 1, 1, 1)
        self.hzUpperBand3Edit = QtWidgets.QLineEdit(Form)
        self.hzUpperBand3Edit.setObjectName("hzUpperBand3Edit")
        self.gridLayout.addWidget(self.hzUpperBand3Edit, 11, 1, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_2.setText(_translate("Form", "Trial Onset (s)"))
        self.nTrialsEdit.setText(_translate("Form", "300"))
        self.label_5.setText(_translate("Form", "Trial Length (s)"))
        self.label.setText(_translate("Form", "Number of Trials"))
        self.label_10.setText(_translate("Form", "S+ Correlated"))
        self.label_13.setText(_translate("Form", "Valve Map Setup : 0 = Blank, 1 = Odour 1, 2 = Odour 2, 3 = Control Odour 1, 4 = Control Blank "))
        self.onsetEdit.setText(_translate("Form", "0.1"))
        self.label_3.setText(_translate("Form", "8 Valve Correlated vs. Uncorrelated - Randomised Frequency"))
        self.label_4.setText(_translate("Form", "Trial Offset (s)"))
        self.offsetEdit.setText(_translate("Form", "0.1"))
        self.trialLengthEdit.setText(_translate("Form", "2.0"))
        self.label_11.setText(_translate("Form", "Number of Control Trials"))
        self.hzUpperBand1Edit.setText(_translate("Form", "20"))
        self.label_7.setText(_translate("Form", "Fraction \'Simple\' Trials"))
        self.hzLowerEdit.setText(_translate("Form", "2"))
        self.label_8.setText(_translate("Form", "Shatter Duty (Hz)"))
        self.shatterHzEdit.setText(_translate("Form", "500"))
        self.nControlTrialsEdit.setText(_translate("Form", "12"))
        self.label_12.setText(_translate("Form", "B1 Lower Limit (Hz)"))
        self.label_6.setText(_translate("Form", "Lick Fraction"))
        self.label_9.setText(_translate("Form", "B1/2/3 Upper Limit (Hz)"))
        self.fractionSimpleTrialsEdit.setText(_translate("Form", "0.5"))
        self.lickFractionEdit.setText(_translate("Form", "0.1"))
        self.hzUpperBand2Edit.setText(_translate("Form", "40"))
        self.hzUpperBand3Edit.setText(_translate("Form", "80"))
