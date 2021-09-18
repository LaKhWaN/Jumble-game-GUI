from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets,uic
from PyQt5.QtCore import *
import jumble_module

#Vairables
app = QtWidgets.QApplication([])
window = uic.loadUi("E:\Programming\Python\Jumble Game\jumble.ui")

correct_msgBox = QMessageBox()
correct_msgBox.setIcon(QMessageBox.Information)
correct_msgBox.setText("Correct Answer!")
correct_msgBox.setStandardButtons(QMessageBox.Ok)

incorrect_msgBox = QMessageBox()
incorrect_msgBox.setIcon(QMessageBox.Critical)
incorrect_msgBox.setText("Incorrect Answer!")
incorrect_msgBox.setStandardButtons(QMessageBox.Ok)

def showCorrect():
	correct_msgBox.show()
	correct_msgBox.exec()
def showIncorrect():
	incorrect_msgBox.show()
	incorrect_msgBox.exec()