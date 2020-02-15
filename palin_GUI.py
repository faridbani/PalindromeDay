import logic
import sys
from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QLineEdit
from PyQt5.QtWidgets import QPushButton, QTextEdit, QVBoxLayout, QHBoxLayout


class PalGui:
    """ The GUI class to use interactive date setting """

    # The main application
    app = QApplication(sys.argv)
    # The Windows
    w_base = QWidget()
    w_left = QWidget()
    w_right = QWidget()
    # A label to get information
    lab1 = QLabel("To calculate all Palindrome days \n Please giv the begin and end year")


    lab4 = QLabel("The result:")
    # Create layouts for windows
    lay = QHBoxLayout()
    lay_left = QVBoxLayout()
    lay_right = QVBoxLayout()
    # The first textfield to giv begin date (year)
    y_b = QLineEdit()
    lab2 = QLabel(y_b)
    lab2.setText("The begin year:")
    lab2.setAlignment(QtCore.Qt.AlignBottom)
    # The second textfield to giv the end date (year)
    y_e = QLineEdit("")
    lab3 = QLabel(y_e)
    lab3.setText("The end year:")
    lab3.setAlignment(QtCore.Qt.AlignBottom)
    # The Calculate button
    calc_b = QPushButton("Calculate")

    # The Clean button
    clean_b = QPushButton("Clean")
    res = QTextEdit("")
    res.setReadOnly(True)

    def __init__(self):
        self.result = []

        # The left Box
        self.lay_left.addWidget(self.lab1)
        self.lay_left.addWidget(self.lab2)
        # set the first textfield
        self.lay_left.addWidget(self.y_b)
        self.lay_left.addWidget(self.lab3)
        # Set the second textfield
        self.lay_left.addWidget(self.y_e)
        # Set the layout of the windows
        self.lay_left.addWidget(self.calc_b)

        # The right box
        self.lay_right.addWidget(self.lab4)

        self.lay_right.addWidget(self.res)
        self.lay_right.addWidget(self.clean_b)
        self.w_right.setLayout(self.lay_right)
        self.w_left.setLayout(self.lay_left)

        self.lay.addWidget(self.w_left)
        self.lay.addWidget(self.w_right)
        self.w_base.setWindowTitle("Palindrome days")
        self.w_base.setLayout(self.lay)
        self.calc_b.clicked.connect(self.calculate)
        self.clean_b.clicked.connect(self.clean)
        self.w_base.show()
        self.app.setActiveWindow(self.w_base)
        sys.exit(self.app.exec_())

    def calculate(self):
        yb = int(self.y_b.text())
        ye = int(self.y_e.text())
        log = logic.Logic(yb, ye)
        self.result = log.run()
        for line in self.result:
            self.res.append(line)

    def clean(self):
        self.res.setText("")


if __name__ == '__main__':
    PalGui()
