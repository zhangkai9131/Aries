# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'aries.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from resources.Global import *

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(446, 222)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(446, 222))
        MainWindow.setMaximumSize(QtCore.QSize(446, 222))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(10, 10, 331, 141))
        self.textEdit.setObjectName("textEdit")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(360, 10, 77, 141))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.Btn_GetData = QtWidgets.QPushButton(self.layoutWidget)
        self.Btn_GetData.setObjectName("Btn_GetData")
        self.verticalLayout.addWidget(self.Btn_GetData)
        self.Btn_Load = QtWidgets.QPushButton(self.layoutWidget)
        self.Btn_Load.setObjectName("Btn_Load")
        self.verticalLayout.addWidget(self.Btn_Load)
        self.Btn_Eff = QtWidgets.QPushButton(self.layoutWidget)
        self.Btn_Eff.setObjectName("Btn_Eff")
        self.verticalLayout.addWidget(self.Btn_Eff)
        self.Btn_Unload = QtWidgets.QPushButton(self.layoutWidget)
        self.Btn_Unload.setObjectName("Btn_Unload")
        self.verticalLayout.addWidget(self.Btn_Unload)
        self.Btn_Cmp = QtWidgets.QPushButton(self.layoutWidget)
        self.Btn_Cmp.setObjectName("Btn_Cmp")
        self.verticalLayout.addWidget(self.Btn_Cmp)
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(90, 160, 251, 20))
        self.lineEdit.setReadOnly(True)
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(14, 164, 71, 16))
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 446, 17))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.Btn_GetData.clicked.connect(self.on_GetData)

    def on_GetData(self):
        #调TS接口取所有stock数据,保存在output/CSV
        print("GetData")

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Btn_GetData.setText(_translate("MainWindow", "取数"))
        self.Btn_Load.setText(_translate("MainWindow", "装载"))
        self.Btn_Eff.setText(_translate("MainWindow", "生效"))
        self.Btn_Unload.setText(_translate("MainWindow", "卸数"))
        self.Btn_Cmp.setText(_translate("MainWindow", "对比"))
        self.label.setText(_translate("MainWindow", "当前版本号"))

