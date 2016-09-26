# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI/SchedGenUI.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1165, 841)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.scheduleParamsScrollArea = QtWidgets.QScrollArea(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scheduleParamsScrollArea.sizePolicy().hasHeightForWidth())
        self.scheduleParamsScrollArea.setSizePolicy(sizePolicy)
        self.scheduleParamsScrollArea.setMinimumSize(QtCore.QSize(600, 0))
        self.scheduleParamsScrollArea.setWidgetResizable(True)
        self.scheduleParamsScrollArea.setObjectName("scheduleParamsScrollArea")
        self.scheduleParamsContents = QtWidgets.QWidget()
        self.scheduleParamsContents.setGeometry(QtCore.QRect(0, 0, 598, 519))
        self.scheduleParamsContents.setObjectName("scheduleParamsContents")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.scheduleParamsContents)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.scheduleParamsScrollArea.setWidget(self.scheduleParamsContents)
        self.gridLayout.addWidget(self.scheduleParamsScrollArea, 2, 0, 3, 1)
        self.valveMapScrollArea = QtWidgets.QScrollArea(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.valveMapScrollArea.sizePolicy().hasHeightForWidth())
        self.valveMapScrollArea.setSizePolicy(sizePolicy)
        self.valveMapScrollArea.setMinimumSize(QtCore.QSize(400, 200))
        self.valveMapScrollArea.setWidgetResizable(True)
        self.valveMapScrollArea.setObjectName("valveMapScrollArea")
        self.valveMapContents = QtWidgets.QWidget()
        self.valveMapContents.setGeometry(QtCore.QRect(0, 0, 598, 198))
        self.valveMapContents.setObjectName("valveMapContents")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.valveMapContents)
        self.verticalLayout.setObjectName("verticalLayout")
        self.valveMapScrollArea.setWidget(self.valveMapContents)
        self.gridLayout.addWidget(self.valveMapScrollArea, 0, 0, 1, 1)
        self.generateScheduleButton = QtWidgets.QPushButton(self.centralwidget)
        self.generateScheduleButton.setObjectName("generateScheduleButton")
        self.gridLayout.addWidget(self.generateScheduleButton, 5, 0, 1, 1)
        self.scheduleTypesCombo = QtWidgets.QComboBox(self.centralwidget)
        self.scheduleTypesCombo.setMinimumSize(QtCore.QSize(150, 0))
        self.scheduleTypesCombo.setObjectName("scheduleTypesCombo")
        self.gridLayout.addWidget(self.scheduleTypesCombo, 1, 0, 1, 1)
        self.scheduleView = QtWidgets.QTableView(self.centralwidget)
        self.scheduleView.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.scheduleView.setAlternatingRowColors(True)
        self.scheduleView.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.scheduleView.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.scheduleView.setObjectName("scheduleView")
        self.scheduleView.horizontalHeader().setCascadingSectionResizes(True)
        self.gridLayout.addWidget(self.scheduleView, 0, 1, 3, 1)
        self.pulseView = PlotWidget(self.centralwidget)
        self.pulseView.setObjectName("pulseView")
        self.gridLayout.addWidget(self.pulseView, 3, 1, 3, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1165, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.generateScheduleButton.setText(_translate("MainWindow", "Generate"))

from pyqtgraph import PlotWidget
