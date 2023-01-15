import sys

from PyQt5 import QtCore, QtGui, QtWidgets

from ui import *


class GUI(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        #Глобальные переменные
        self.progres_flag = False
        self.progres_value = 0
        self.ui.progressBar.setValue(self.progres_value)

        # Оброботчики кнопок
        self.ui.pushButton.clicked.connect(self.add_item)
        self.ui.pushButton_2.clicked.connect(self.clear_box)
        self.ui.pushButton_3.clicked.connect(self.set_style)



    def add_item(self):
        if len(self.ui.lineEdit.text())>0:
            # Возвращаем return если прогресс бар заполнен
            if self.ui.progressBar.value() == 100:
                self.ui.plainTextEdit.clear()
                self.ui.plainTextEdit.appendPlainText('Список заполнен!')
                return
            # Проверяем есть ли элемент в списке
            line_text = self.ui.lineEdit.text()
            elements_count = self.ui.comboBox.count()

            for element in range(0, elements_count):
                self.ui.comboBox.setCurrentIndex(element)
                local_text = self.ui.comboBox.currentText()

                if local_text == line_text:
                    self.ui.plainTextEdit.appendPlainText('Объект уже есть в списке!')
                    return

            # Если ни одно из уловий выше не выполнилось - добавляем в comboBox
            self.progres_value += 25
            self.ui.comboBox.addItem(line_text)
            self.ui.plainTextEdit.appendPlainText('Объект успешно добавлен.')
            self.ui.progressBar.setValue(self.progres_value)
        else:
            self.ui.plainTextEdit.appendPlainText('Строка не может быть пустрой!')
        
    def clear_box(self):
        self.progres_value = 0 
        self.ui.comboBox.clear()
        self.ui.plainTextEdit.clear()
        self.ui.plainTextEdit.appendPlainText('Все объекты удалены!')
        self.ui.progressBar.setValue(self.progres_value)

    def set_style(self):
        default_style = '''
            QProgressBar{

            }
        '''

        style = '''
            QProgressBar::chunk{
                background-color:red;
                width: 10px;
                margin: 1px;
            }
        '''

        if not self.progres_flag:
            self.ui.progressBar.setStyleSheet(style)
            self.progres_flag = True
        else:
            self.ui.progressBar.setStyleSheet(default_style)
            self.progres_flag= False


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = GUI()
    myapp.show()
    sys.exit(app.exec_())
    
