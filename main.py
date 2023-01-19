import sys

from PyQt5 import QtCore, QtGui, QtWidgets

from ui import *
from mod import * 
        

class GUI(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Обработчики
        self.ui.pushButton.clicked.connect(self.modal)
        self.ui.pushButton_2.clicked.connect(self.qt_modal)


    def qt_modal(self):
        window = Modal_Window(self)
        window.show()

    def modal(self):
        window = QtWidgets.QWidget(self, QtCore.Qt.Window)
        window.setWindowTitle('title')
        window.setWindowModality(2)
        window.resize(500, 500)
        window.show()



class Modal_Window(QtWidgets.QWidget):
    def __init__(self, parent=GUI):
        super().__init__(parent, QtCore.Qt.Window)
        self.modal = Ui_Form()
        self.modal.setupUi(self)
        # Блокируем родительское окно
        self.setWindowModality(2)
        # 0 - не использовать модальное окно
        # 1 - использовать модальное окно тольк для предидущих окон
        # 2 - использовать моадльное окно для всех окно

        




if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = GUI()
    myapp.show()
    sys.exit(app.exec_())
    
