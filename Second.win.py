from instr import *
from Second_win import *
from PyQt5.QtCore import Qt, QTimer, QTime, QLocale
from PyQt5.QtGui import QDoubleValidator, QIntValidator, QFont
from PyQt5.QtWidgets import (
        QApplication, QWidget,
        QHBoxLayout, QVBoxLayout, QGridLayout,
        QGroupBox, QRadioButton,
        QPushButton, QLabel, QListWidget, QLineEdit)

def TestWin():
        but = QPushButton(txt_starttest1)
        but2 = QPushButton(txt_starttest2)
        but3 = QPushButton(txt_starttest3)
        but4 = QPushButton(txt_sendresults)
        text = QLabel(txt_name)
        text2 = QLabel(txt_test1)
        text3 = QLabel(txt_test2)
        text4 = QLabel(txt_test3)