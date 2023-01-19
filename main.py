import sys

from PyQt5 import QtCore, QtGui, QtWidgets

from ui import *


class GUI(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.notification)
        self.ui.pushButton_2.clicked.connect(self.confirm)
        self.ui.pushButton_3.clicked.connect(self.message)
        self.ui.pushButton_4.clicked.connect(self.error_message)
        
    def notification(self):
        # Вызво оповещения
        QtWidgets.QMessageBox.about(self, 'title', 'message')
        QtWidgets.QMessageBox.warning(self, 'title', 'message')
        QtWidgets.QMessageBox.information(self, 'title', 'message')
        QtWidgets.QMessageBox.critical(self, 'title', 'message')

    def confirm(self):
        result = QtWidgets.QMessageBox.question(
            self,
            'Header',
            'Discription...',
            QtWidgets.QMessageBox.Yes,
            QtWidgets.QMessageBox.No
        )

        if result == QtWidgets.QMessageBox.Yes:
            print('Yes')
        else:
            print('No')

        # QtWidgets.QMessageBox.Ok
        # QtWidgets.QMessageBox.Open
        # QtWidgets.QMessageBox.Save
        # QtWidgets.QMessageBox.Cancel
        # QtWidgets.QMessageBox.Close
        # QtWidgets.QMessageBox.Yes
        # QtWidgets.QMessageBox.No
        # QtWidgets.QMessageBox.Abort
        # QtWidgets.QMessageBox.Retry
        # QtWidgets.QMessageBox.Ignore

    def message(self):
        # Вывод подробного сообщения с доп.инфо.
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Critical)
        msg.setWindowTitle('title')
        msg.setInformativeText('desroption')
        msg.setDetailedText('detailed...')
        msg.setStandardButtons(QtWidgets.QMessageBox.Ok | QtWidgets.QMessageBox.Cancel)
        item = msg.exec_()

        if item == QtWidgets.QMessageBox.Ok:
            print('Ok')
        elif item == QtWidgets.QMessageBox.Cancel:
            print('Cancel')

    def error_message(self):
        # Ошибка которая дает возможность отключить ее повторный вывод
        error = QtWidgets.QErrorMessage(self)
        error.setWindowTitle('Title')
        error.showMessage('error_message')


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = GUI()
    myapp.show()
    sys.exit(app.exec_())
    
