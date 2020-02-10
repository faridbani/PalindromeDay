#import logic

from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QPushButton, QTextEdit, QVBoxLayout, QHBoxLayout


class PalGui:
    """ The GUI class to use interactive date setting """

    def __init__(self):
        # A instance of class Logic to handle the settings
        #log = logic.Logic()
        # The main application
        app = QApplication([])
        # Set application layout
        #app.setStyle("Fusion")
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
        y_b = QTextEdit("")
        y_b.setMaximumHeight(35)
        # The second textfield to giv the end date (year)
        y_e = QTextEdit("")
        y_e.setMaximumHeight(35)

        # The run button
        r_b = QPushButton("Run")

        # The left Box
        lay_left.addWidget(lab1)
        lay_left.addWidget(lab2)
        # set the first textfield
        lay_left.addWidget(y_b)
        lay_left.addWidget(lab3)
        # Set the second textfield
        lay_left.addWidget(y_e)
        # Set the layout of the windows
        lay_left.addWidget(r_b)

        # The right box
        lay_right.addWidget(lab4)
        res = QTextEdit("")
        lay_right.addWidget(res)
        w_right.setLayout(lay_right)
        w_left.setLayout(lay_left)

        lay.addWidget(w_left)
        lay.addWidget(w_right)
        w_base.setLayout(lay)

        w_base.show()
        app.setActiveWindow(w_base)
        app.exec_()


gui = PalGui()
