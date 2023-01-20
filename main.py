import sys
import time

from PyQt5 import QtCore, QtGui, QtWidgets

from ui import *
        

class Handler(QtCore.QThread):
    mysignal = QtCore.pyqtSignal(list)

    def __init__(self, parent=None):
        super().__init__(parent)

    def run(self):
        arrage =list(range(0, 10))
        self.mysignal.emit(arrage)


class GUI(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.pushButton.clicked.connect(self.start_handler)


        # Когда в Handler выполняется emit(), то код ниже
        # ловит сигнал и передает его в "self.add_item"
        self.mythread = Handler()
        self.mythread.mysignal.connect(self.add_item)


    def start_handler(self):
        self.mythread.start()

    def add_item(self, value):
        for i in value:
            self.ui.plainTextEdit.appendPlainText(str(i))

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = GUI()
    myapp.show()
    sys.exit(app.exec_())
    
