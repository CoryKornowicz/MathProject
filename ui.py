# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/Cory/Library/Mobile Documents/com~apple~CloudDocs/Freshman Year College/Spring 2019/Calc 2/Project/ProjectGUI.ui',
# licensing of '/Users/Cory/Library/Mobile Documents/com~apple~CloudDocs/Freshman Year College/Spring 2019/Calc 2/Project/ProjectGUI.ui' applies.
#
# Created: Sat Apr 20 19:20:25 2019
#      by: pyside2-uic  running on PySide2 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets
import functions


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(432, 327)
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(10, 10, 411, 51))
        self.lineEdit.setObjectName("lineEdit")
        self.textEdit = QtWidgets.QTextEdit(Dialog)
        self.textEdit.setGeometry(QtCore.QRect(10, 190, 411, 131))
        self.textEdit.setObjectName("textEdit")
        self.calculateButton = QtWidgets.QPushButton(Dialog)
        self.calculateButton.setGeometry(QtCore.QRect(10, 70, 113, 32))
        self.calculateButton.setObjectName("calculateButton")
        self.calculateButton.clicked.connect(self.accept)

        self.retranslateUi(Dialog)


    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtWidgets.QApplication.translate("Dialog", "Dialog", None, -1))
        self.calculateButton.setText(QtWidgets.QApplication.translate("Dialog", "Calculate", None, -1))

    def accept(self):
        functions.calculateFunction(self.lineEdit.text())


