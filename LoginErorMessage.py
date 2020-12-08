import sys
from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets
from PyQt5 import QtGui
from PyQt5 import QtCore


class ErorWindow(QWidget):
    def __init__(self):
        super().__init__()
    #def setupUI(self, ErorWindow):
        self.setWindowIcon(QtGui.QIcon('karatauicon.png'))
        self.setWindowTitle("Using MessageBoxes")
        self.setGeometry(500,500,200,50)
        self.messageBox()



    def messageBox(self):
        mBox = QMessageBox.information(self, "Ошибка", "Вы ввели неправильный логин или пароль")
        #просто заебошь лэйбел



def main():
    App = QApplication(sys.argv)
    window=ErorWindow()
    sys.exit(App.exec_())

if __name__ == '__main__':
    main()

    """""
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ErorWindow = QtWidgets.QMainWindow()
    ui = Ui_ErorWindow()
    ui.setupUi(ErorWindow)
    ErorWindow.show()
    sys.exit(app.exec_())"""""