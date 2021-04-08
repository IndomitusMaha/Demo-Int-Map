from PyQt5 import QtCore, QtGui, QtWidgets
from resources import logos
from resources import MainWindowResources
from resources import MapsResizeResources


class Ui_SZhR2(object):
    def setupUi(self, MainWindow):
        MainWindow.setWindowIcon(QtGui.QIcon('karatauicon.png'))
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(850, 300)
        MainWindow.setMinimumSize(QtCore.QSize(850, 300))
        MainWindow.setMaximumSize(QtCore.QSize(850, 300))

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 850, 300))
        self.label.setStyleSheet("QLabel{\n"
            "color: rgb(0, 0, 0);\n"
            "font: 1000 18pt \"Times New Roman\" ;\n""}")
        self.label.setText("exrctfvygbuhnjmk,l")
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "СЖР"))
        self.label.setText(_translate("MainWindow",
         "          СЖР - склад жидких реагентов. Здесь хранится \n "
         "   кислота. Кислотовозы доставляют ее сюда. Отсюда же,\n"
         "    она перегоняется на полигон с помощью насосов и \n"
         "    кислотной линии. \n"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_SZhR2()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
