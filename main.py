import sys
import time

from PyQt5 import QtCore, QtGui, QtWidgets

from ui import *

class MyWin(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # self.pushButton
        self.ui.pushButton.clicked.connect(self.handler)
         
    def handler(self):
        self.ui.pushButton.setDisabled(True);  time.sleep(5)
        self.ui.plainTextEdit.appendPlainText('text')
        self.ui.label.setText('text')
        
        

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp =MyWin()
    myapp.show()
    sys.exit(app.exec_())
    
