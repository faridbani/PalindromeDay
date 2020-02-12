import logic
import sys
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
    lab2 = QLabel("The begin year:")
    lab3 = QLabel("The end year")
    lab4 = QLabel("The result:")
    # Create layouts for windows
    lay = QHBoxLayout()
    lay_left = QVBoxLayout()
    lay_right = QVBoxLayout()
    # The first textfield to giv begin date (year)
    y_b = QLineEdit("")
    # The second textfield to giv the end date (year)
    y_e = QLineEdit("")
    # The Calculate button
    calc_b = QPushButton("Calculate")

    # The Clean button
    clean_b = QPushButton("Clean")
    res = QTextEdit("")
    res.setReadOnly(True)

    def __init__(self):
        # A instance of class Logic to calculate palindrome days
        self.log = logic.Logic(2020, 2050)
        self.result = []
        # Set application layout
        self.app.setStyle("Fusion")

        #self.y_b.setMaximumHeight(35)
        #self.y_e.setMaximumHeight(35)
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
        ye = (self.y_e.text())
        self.result = self.log.run()
        print(self.result)
        for line in self.result:
            self.res.append(line)


    def clean(self):
        self.res.setText("")


if __name__ == '__main__':
    PalGui()
