import sys
import time

from PyQt5 import QtCore, QtGui, QtWidgets

from ui import *

class MyWin(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.handler)
        self.ui.pushButton_2.clicked.connect(self.setcolor)
         
    def handler(self):
        self.ui.pushButton.setDisabled(True)
        self.ui.plainTextEdit.appendPlainText('text')
        self.ui.label.setText('text')

    def setcolor(self):
        self.ui.pushButton.setText('11111')
        self.ui.pushButton.setStyleSheet('background-color: red; color: white;')
        self.ui.pushButton.setDisabled(False)
        
        

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp =MyWin()
    myapp.show()
    sys.exit(app.exec_())
    
