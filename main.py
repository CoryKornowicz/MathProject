# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/Cory/Library/Mobile Documents/com~apple~CloudDocs/Freshman Year College/Spring 2019/Calc 2/Project/ProjectGUI.ui',
# licensing of '/Users/Cory/Library/Mobile Documents/com~apple~CloudDocs/Freshman Year College/Spring 2019/Calc 2/Project/ProjectGUI.ui' applies.
#
# Created: Wed Apr 17 17:54:43 2019
#      by: pyside2-uic  running on PySide2 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(432, 327)
        self.buttoBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttoBox.setGeometry(QtCore.QRect(0, 0, 81, 71))
        self.buttoBox.setOrientation(QtCore.Qt.Vertical)
        self.buttoBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttoBox.setObjectName("buttoBox")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(80, 10, 341, 51))
        self.lineEdit.setObjectName("lineEdit")
        self.textEdit = QtWidgets.QTextEdit(Dialog)
        self.textEdit.setGeometry(QtCore.QRect(10, 70, 411, 131))
        self.textEdit.setObjectName("textEdit")

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.buttoBox, QtCore.SIGNAL("accepted()"), Dialog.accept)
        QtCore.QObject.connect(self.buttoBox, QtCore.SIGNAL("rejected()"), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtWidgets.QApplication.translate("Dialog", "Dialog", None, -1))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

