import sys
import time
import random

from PyQt5 import QtCore, QtGui, QtWidgets

from ui import *

class MyWin(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.gettext)
        self.ui.checkBox.clicked.connect(self.output)

    def output(self):
        name = self.ui.checkBox.text()
        self.ui.radioButton.setText(str(random.randint(0, 100)))
        print(name)

    def gettext(self):
        if self.ui.checkBox.isChecked():
            checkbox_1 = self.ui.checkBox.text()
        else:
            checkbox_1 = ''

        if self.ui.checkBox_2.isChecked():
            checkbox_2 = self.ui.checkBox_2.text()
        else:
            checkbox_2 = ''

        if self.ui.radioButton.isChecked():
            radiobutton_1 = self.ui.radioButton.text()
        else:
            radiobutton_1 = ''

        if self.ui.radioButton_2.isChecked():
            radiobutton_2 = self.ui.radioButton_2.text()
        else:
            radiobutton_2 = ''

        result = f'{checkbox_1}{checkbox_2}{radiobutton_1}{radiobutton_2} Hello world'

        self.ui.plainTextEdit.appendPlainText(result)      
        

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyWin()
    myapp.show()
    sys.exit(app.exec_())
    
