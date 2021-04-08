from PyQt5 import QtCore, QtGui, QtWidgets
from resources import logos
from resources import MainWindowResources
from resources import MapsResizeResources


class Ui_UPVR(object):
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
        MainWindow.setWindowTitle(_translate("MainWindow", "УПВР"))
        self.label.setText(_translate("MainWindow",
         "          УПВР - узел подготовки выщелачивающего раствора.\n "
         "   В данном блоке находится ТУЗ (технологический узел\n"
         "    закисления). В ТУЗ, кислота смешивается с отработанным\n"
         "    выщелачивающим раствором и перекачивается в УРВР\n"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_UPVR()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
