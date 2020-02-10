#import logic

from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QPushButton, QTextEdit, QHBoxLayout, QVBoxLayout


class P_GUI:
    def __init__(self):
        #log = logic.Logic()
        app = QApplication([])
        app.setStyle("Fusion")
        w = QWidget()
        lab = QLabel("Please giv the begin and end year")
        lay = QHBoxLayout()
        y_b = QTextEdit("2020")
        y_e = QTextEdit("2020")
        lay.addWidget(lab)
        lay.addWidget(y_b)
        lay.addWidget(y_e)
        w.setLayout(lay)
        w.show()
        app.setActiveWindow(w)
        app.exec_()


gui = P_GUI()
