# -*- coding: utf-8 -*-
# Filename:AppMain.py

import sys
#from PyQt5 import QtCore, QtGui, QtWidgets
from ui.AriesMain import *

def main():
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
