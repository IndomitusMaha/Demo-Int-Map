from PyQt5 import QtCore, QtGui, QtWidgets
from resources import logos
from resources import MainWindowResources
from resources import MapsResizeResources


class Ui_URVR(object):
    def setupUi(self, MainWindow):
        MainWindow.setWindowIcon(QtGui.QIcon('karatauicon.png'))
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(880, 300)
        MainWindow.setMinimumSize(QtCore.QSize(880, 300))
        MainWindow.setMaximumSize(QtCore.QSize(880, 300))

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 880, 300))
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
        MainWindow.setWindowTitle(_translate("MainWindow", "УРВР"))
        self.label.setText(_translate("MainWindow",
         "         УРВР - узел распределения выщелачивающего раствора.\n "
         "   ВР из УПВР, через данный блок идет в закачные скважины.\n"
         "         Также, используется блок УПРР. Данный блок совмещает\n"
         "    функции УРВР и УППР."))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_URVR()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
