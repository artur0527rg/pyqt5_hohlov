import sys

from PyQt5 import QtCore, QtGui, QtWidgets

from ui import *
        

class GUI(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.actionOpen_file.triggered.connect(self.test)

    def test(self):
        self.ui.statusbar.showMessage('Work')


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = GUI()
    myapp.show()
    sys.exit(app.exec_())
    
