import sympy.parsing.latex as pl
from sympy import *
import numpy as np
import matplotlib.pyplot as plt

plt.style.use("ggplot")

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(709, 530)
        self.verticalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 711, 521))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.spinBox_3 = QtWidgets.QSpinBox(self.verticalLayoutWidget)
        self.spinBox_3.setObjectName("spinBox_3")
        self.gridLayout.addWidget(self.spinBox_3, 1, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 0, 4, 1, 1)
        self.spinBox_2 = QtWidgets.QSpinBox(self.verticalLayoutWidget)
        self.spinBox_2.setObjectName("spinBox_2")
        self.gridLayout.addWidget(self.spinBox_2, 0, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 2, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.spinBox = QtWidgets.QSpinBox(self.verticalLayoutWidget)
        self.spinBox.setObjectName("spinBox")
        self.gridLayout.addWidget(self.spinBox, 0, 3, 1, 1)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout.addWidget(self.lineEdit_2, 0, 5, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 1, 4, 1, 1)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.gridLayout.addWidget(self.lineEdit_3, 1, 5, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout)
        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_2.addWidget(self.label_4)
        self.lineEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit.setMinimumSize(QtCore.QSize(0, 30))
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout_2.addWidget(self.lineEdit)
        self.calculateButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.calculateButton.setObjectName("calculateButton")
        self.verticalLayout_2.addWidget(self.calculateButton)
        self.pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_2.addWidget(self.pushButton)
        self.textEdit = QtWidgets.QTextEdit(self.verticalLayoutWidget)
        self.textEdit.setObjectName("textEdit")
        self.verticalLayout_2.addWidget(self.textEdit)

        self.calculateButton.clicked.connect(self.accept)
        self.pushButton.clicked.connect(self.clear_boxes)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtWidgets.QApplication.translate("Dialog", "Dialog", None, -1))
        self.label_5.setText(QtWidgets.QApplication.translate("Dialog", "X-Offset", None, -1))
        self.label_2.setText(QtWidgets.QApplication.translate("Dialog", "to", None, -1))
        self.label_3.setText(QtWidgets.QApplication.translate("Dialog", "How many total iterations", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("Dialog", "Display the range of iterations from", None, -1))
        self.label_6.setText(QtWidgets.QApplication.translate("Dialog", "Iterate By", None, -1))
        self.label_4.setText(QtWidgets.QApplication.translate("Dialog", "Function:", None, -1))
        self.calculateButton.setText(QtWidgets.QApplication.translate("Dialog", "Calculate", None, -1))
        self.pushButton.setText(QtWidgets.QApplication.translate("Dialog", "Clear", None, -1))

    def accept(self):
        # functions.calculateFunction(self.lineEdit.text())
        # functions.plot()
        # Define the variable and the function to approximate
        # text = str(self.lineEdit.text())
        # self.print_to_text_field("Evaluating [" + text + "]")
        # Need
        #   reset values on clearing

        try:
            text = pl.parse_latex(self.lineEdit.text())
            assert text is not None, "Function should not be empty\n"
        except AssertionError as error:
            # Output expected AssertionErrors.
            self.print_to_text_field("Function should not be empty\n")
            return
        except Exception as exception:
            # Output unexpected Exceptions.
            self.print_to_text_field("Function is improperly formatted\n")
            return

        to_num = int(self.spinBox.text())
        from_num = int(self.spinBox_2.text())

        try:
            by_num = int(self.lineEdit_3.text())
            assert by_num is not None, "By number should at least be 1\n"
        except AssertionError as error:
            # Output expected AssertionErrors.
            self.print_to_text_field("By number should at least be 1\n")
            return

        try:
            x_off = int(self.lineEdit_2.text())
            assert x_off is not None, "X-Off number should at least be 0\n"
        except AssertionError as error:
            # Output expected AssertionErrors.
            self.print_to_text_field("By number should at least be 0\n")
            return

        try:
            iterations = int(self.spinBox_3.text())
            assert iterations > 0, "Must have at least 1 iteration\n"
        except AssertionError as error:
            # Output expected AssertionErrors.
            self.print_to_text_field("Must have at least 1 iteration\n")
            return

        string = f'Running Taylor Series on {text} by {by_num} over the range of {from_num} to {to_num} ' \
            f'for {iterations} iterations\n'
        self.print_to_text_field(string)
        self.plot(text, x_off, iterations, by_num, from_num, to_num)


    def print_to_text_field(self, text):
        self.textEdit.setFocus()
        self.textEdit.insertPlainText(text)

    def clear_boxes(self):
        self.lineEdit.clear()
        self.lineEdit.repaint()
        self.textEdit.clear()
        self.textEdit.repaint()
    #     every line edit and every spin box
        self.lineEdit_2.clear()
        self.lineEdit_2.repaint()
        self.lineEdit_3.clear()
        self.lineEdit_3.repaint()

        self.spinBox.clear()
        self.spinBox.repaint()

        self.spinBox_2.clear()
        self.spinBox_2.repaint()

        self.spinBox_3.clear()
        self.spinBox_3.repaint()


    # Factorial function
    @staticmethod
    def factorial(n):
        if n <= 0:
            return 1
        else:
            return n * factorial(n - 1)

    # Taylor approximation at x0 of the function 'function'
    @staticmethod
    def taylor(func, x0, n, x=Symbol('x')):
        i = 0
        p = 0
        while i <= n:
            p = p + (func.diff(x, i).subs(x, x0)) / (factorial(i)) * (x - x0) ** i
            i += 1
        return p

    def plot(self, f, x0=0, n=10, by=1, min_num=0, max_num=1, x_lims=[-10, 10], y_lims=[-10, 10], npoints=1000, x=Symbol('x')):
        x1 = np.linspace(x_lims[0], x_lims[1], npoints)
        # Approximate up until n starting from 1 and using steps of by

        for j in range(1, n + 1, by):
            func = self.taylor(f, x0, j)
            taylor_lambda = lambdify(x, func, "numpy")
            string = f'Taylor expansion at n = {j} = {func}\n'
            self.print_to_text_field(string)

            if j in range(min_num, max_num + 1):
                plt.plot(x1, taylor_lambda(x1), label='Order ' + str(j))

        # Plot the function to approximate
        try:
            func_lambda = lambdify(x, f, "numpy")
            plt.plot(x1, func_lambda(x1), label='Function of x')
        except TypeError as err:
            self.print_to_text_field("Function is unable to be serialized\n")



        plt.xlim(x_lims)
        plt.ylim(y_lims)
        plt.xlabel('x')
        plt.ylabel('y')
        plt.legend()
        plt.grid(True)
        plt.title('Taylor series approximation')
        plt.show()
