from PySide2 import QtCore, QtGui, QtWidgets
import functions as fn
import sympy.parsing.latex as pl
from sympy.functions import sin, cos, ln
# import sympy as sy
from sympy import *
import numpy as np
import matplotlib.pyplot as plt

# TODO: Add in Helping Statements and Default Values

from PySide2 import QtCore, QtGui, QtWidgets

plt.style.use("ggplot")

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(709, 530)
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(10, 70, 691, 41))
        self.lineEdit.setObjectName("lineEdit")
        self.textEdit = QtWidgets.QTextEdit(Dialog)
        self.textEdit.setGeometry(QtCore.QRect(10, 140, 691, 381))
        self.textEdit.setObjectName("textEdit")
        self.calculateButton = QtWidgets.QPushButton(Dialog)
        self.calculateButton.setGeometry(QtCore.QRect(10, 110, 113, 32))
        self.calculateButton.setObjectName("calculateButton")
        self.calculateButton.clicked.connect(self.accept)
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(120, 110, 113, 32))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.clear_boxes)
        self.spinBox_2 = QtWidgets.QSpinBox(Dialog)
        self.spinBox_2.setGeometry(QtCore.QRect(230, 10, 48, 24))
        self.spinBox_2.setObjectName("spinBox_2")
        self.spinBox = QtWidgets.QSpinBox(Dialog)
        self.spinBox.setGeometry(QtCore.QRect(300, 10, 48, 24))
        self.spinBox.setObjectName("spinBox")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(10, 10, 221, 21))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(280, 10, 60, 21))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(10, 30, 161, 21))
        self.label_3.setObjectName("label_3")
        self.spinBox_3 = QtWidgets.QSpinBox(Dialog)
        self.spinBox_3.setGeometry(QtCore.QRect(170, 30, 48, 24))
        self.spinBox_3.setObjectName("spinBox_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(10, 50, 60, 16))
        self.label_4.setObjectName("label_4")
        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(420, 10, 111, 21))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(360, 10, 60, 21))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(360, 40, 60, 16))
        self.label_6.setObjectName("label_6")
        self.lineEdit_3 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_3.setGeometry(QtCore.QRect(420, 40, 113, 21))
        self.lineEdit_3.setObjectName("lineEdit_3")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtWidgets.QApplication.translate("Dialog", "Dialog", None, -1))
        self.calculateButton.setText(QtWidgets.QApplication.translate("Dialog", "Calculate", None, -1))
        self.pushButton.setText(QtWidgets.QApplication.translate("Dialog", "Clear", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("Dialog", "Display the range of iterations from", None, -1))
        self.label_2.setText(QtWidgets.QApplication.translate("Dialog", "to", None, -1))
        self.label_3.setText(QtWidgets.QApplication.translate("Dialog", "How many total iterations", None, -1))
        self.label_4.setText(QtWidgets.QApplication.translate("Dialog", "Function:", None, -1))
        self.label_5.setText(QtWidgets.QApplication.translate("Dialog", "X-Offset", None, -1))
        self.label_6.setText(QtWidgets.QApplication.translate("Dialog", "Iterate By", None, -1))

    def accept(self):
        # functions.calculateFunction(self.lineEdit.text())
        # functions.plot()
        # Define the variable and the function to approximate
        # text = str(self.lineEdit.text())
        # self.print_to_text_field("Evaluating [" + text + "]")
        # Need
        #  [x]function name
        #  [x]range
        #  [0]by counter
        #  [0]n count
        #

        try:
            text = pl.parse_latex(self.lineEdit.text())
            assert text is not None, "Function should not be empty"
        except AssertionError as error:
            # Output expected AssertionErrors.
            self.print_to_text_field("Function should not be empty")
            return
        except Exception as exception:
            # Output unexpected Exceptions.
            self.print_to_text_field("Function is improperly formatted")
            return

        from_num = self.spinBox.text()
        to_num = self.spinBox_2.text()

        try:
            by_num = self.lineEdit_2.text()
            assert by_num is not None, "By number should at least be 1"
        except AssertionError as error:
            # Output expected AssertionErrors.
            self.print_to_text_field("By number should at least be 1")
            return

        try:
            x_off = self.lineEdit_3.text()
            assert x_off is not None, "X-Off number should at least be 0"
        except AssertionError as error:
            # Output expected AssertionErrors.
            self.print_to_text_field("By number should at least be 0")
            return


    def print_to_text_field(self, text):
        self.textEdit.setFocus()
        self.textEdit.setText(text)

    def clear_boxes(self):
        self.lineEdit.setFocus()
        self.lineEdit.clear()
        self.lineEdit.setText("")
        self.lineEdit.clearFocus()
        self.textEdit.setFocus()
        self.textEdit.clear()
        self.textEdit.setText("")
        self.textEdit.clearFocus()

    # Factorial function
    @staticmethod
    def factorial(n):
        if n <= 0:
            return 1
        else:
            return n * factorial(n - 1)

    # Taylor approximation at x0 of the function 'function'
    @staticmethod
    def taylor(function, x0, n, x=Symbol('x')):
        i = 0
        p = 0
        while i <= n:
            p = p + (function.diff(x, i).subs(x, x0)) / (factorial(i)) * (x - x0) ** i
            i += 1
        return p

    def plot(self, f, x0=0, n=20, by=1, x_lims=[-10, 10], y_lims=[-10, 10], npoints=800, x=Symbol('x')):
        x1 = np.linspace(x_lims[0], x_lims[1], npoints)
        # Approximate up until n starting from 1 and using steps of by
        for j in range(1, n + 1, by):
            func = self.taylor(f, x0, j)
            taylor_lambda = lambdify(x, func, "numpy")
            print('Taylor expansion at n=' + str(j), func)
            plt.plot(x1, taylor_lambda(x1), label='Order ' + str(j))
        # Plot the function to approximate (sine, in this case)
        func_lambda = lambdify(x, f, "numpy")
        plt.plot(x1, func_lambda(x1), label='Function of x')

        plt.xlim(x_lims)
        plt.ylim(y_lims)
        plt.xlabel('x')
        plt.ylabel('y')
        plt.legend()
        plt.grid(True)
        plt.title('Taylor series approximation')
        plt.show()
