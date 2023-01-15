import sys

from PyQt5 import QtCore, QtGui, QtWidgets

from ui import *


class GUI(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.number = 0

        self.ui.pushButton.clicked.connect(self.add_item)
        self.ui.pushButton_2.clicked.connect(self.clear_all)

        self.tabel_index = 0
        self.row_count = 1
        self.ui.pushButton_3.clicked.connect(self.add_tabel_item)
        self.ui.pushButton_4.clicked.connect(self.clear_table)

    def add_item(self):
        radio_base = [
            self.ui.radioButton, self.ui.radioButton_2,
            self.ui.radioButton_3, self.ui.radioButton_4
        ]
        for radio in radio_base:
            if radio.isChecked():
                name = radio.text()
                icon = QtGui.QIcon(f'{name}.png')
                print(f'{name}.png')
                self.ui.listWidget.addItem(f"{name} - {self.number}")
                self.ui.listWidget.setCurrentRow(self.number)
                item = self.ui.listWidget.currentItem()
                item.setIcon(icon)
                self.number += 1

    def clear_all(self):
        self.ui.listWidget.clear()
        self.number = 0

    def add_tabel_item(self):
        ID = None
        NAME = None
        AGE = None
        
        if (len(self.ui.lineEdit.text()))>0:
            ID = self.ui.lineEdit.text()
        else: return

        if (len(self.ui.lineEdit_2.text()))>0:
            NAME = self.ui.lineEdit_2.text()
        else: return

        if (len(self.ui.lineEdit_3.text()))>0:
            AGE = self.ui.lineEdit_3.text()
        else: return

        self.ui.tableWidget.setRowCount(self.row_count)
        self.ui.tableWidget.setItem(self.tabel_index, 0, QtWidgets.QTableWidgetItem(ID))
        self.ui.tableWidget.setItem(self.tabel_index, 1, QtWidgets.QTableWidgetItem(NAME))
        self.ui.tableWidget.setItem(self.tabel_index, 2, QtWidgets.QTableWidgetItem(AGE))
        
        self.tabel_index += 1
        self.row_count += 1

    def clear_table(self):
        self.tabel_index = 0
        self.row_count = 1
        self.ui.tableWidget.clear()
        self.ui.tableWidget.setHorizontalHeaderItem(0, QtWidgets.QTableWidgetItem('ID'))
        self.ui.tableWidget.setHorizontalHeaderItem(1, QtWidgets.QTableWidgetItem('Name'))
        self.ui.tableWidget.setHorizontalHeaderItem(2, QtWidgets.QTableWidgetItem('Age'))

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = GUI()
    myapp.show()
    sys.exit(app.exec_())
    
