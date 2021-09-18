from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets,uic
from PyQt5.QtCore import *
import jumble_module
import msgBox

#Vairables
app = QtWidgets.QApplication([])
window = uic.loadUi("E:\Programming\Python\Jumble Game\jumble.ui")

def showDialog():
    jumble = jumble_module.jumbleWord()
    window.jumble.setText(jumble)
    window.okButton.clicked.connect(buttons.Ok)
    window.resetButton.clicked.connect(buttons.Reset)

class buttons():    
    def Reset():
        #window.lineEdit.clear()
        showDialog()

    def Ok():
        inputText = window.lineEdit.text()
        window.lineEdit.clear()
        f=open("__cache__.txt","r")
        word = f.readline()
        f.close()
        if word == inputText:
            msgBox.showCorrect()
            showDialog()
        else:
            msgBox.showIncorrect()
            showDialog()
showDialog()
window.show()
app.exec()