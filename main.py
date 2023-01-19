import sys

from PyQt5 import QtCore, QtGui, QtWidgets

from ui import *
        

class GUI(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.pushButton.clicked.connect(self.open_file)
        self.ui.pushButton_2.clicked.connect(self.save_file)
        self.ui.pushButton_3.clicked.connect(self.open_files)
        self.ui.pushButton_4.clicked.connect(self.color)
        self.ui.pushButton_5.clicked.connect(self.open_folder)

    def open_file(self):
        file_path = QtWidgets.QFileDialog.getOpenFileName(self, 'header', 'filename', 'Image (*.png *.jpeg *.jpg)\nPython (*.py)\nUI (*.ui)')
        print(file_path)

    def save_file(self):
        file_path = QtWidgets.QFileDialog.getSaveFileName(self, 'title', 'filename', 'Document *.txt')
        print(file_path)

        with open(file_path[0], 'w') as file:
            file.write('')

    def open_files(self):
        file_path = QtWidgets.QFileDialog.getOpenFileNames(self, 'header', 'filename', 'Python *.py')
        print(file_path)

    def open_folder(self):
        directory = QtWidgets.QFileDialog.getExistingDirectory(self)
        print(directory)

    def color(self):
        color = QtWidgets.QColorDialog(self).getColor()
        print(color.red(), color.green(), color.blue(), color.alpha())


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = GUI()
    myapp.show()
    sys.exit(app.exec_())
    
