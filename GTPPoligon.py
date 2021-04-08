# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GTPPoligon.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from resources import GTPResources
from resources import MainWindowResources
from resources import logos
from resources import OrangeBackgroundResources
from UPRR import Ui_UPRR
from UnderConstruction import Ui_UnderConstruction
from Svyaz import Ui_Svyaz
from SZhR2 import Ui_SZhR2


class Ui_GTPPoligon(object):
    def setupUi(self, MainWindow):
        MainWindow.setWindowIcon(QtGui.QIcon('karatauicon.png'))
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(760, 513)
        MainWindow.setMaximumSize(760, 490)
        MainWindow.setMinimumSize(760, 490)
        MainWindow.setStyleSheet("QWidget{\n"
"background-color: rgb(65, 102, 245);\n"
"background-image: url(:/logos/karatau_logo_small___копия-removebg-preview.png)\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 761, 491))
        self.label.setStyleSheet("background-image: url(:/GTP/images/GTP Map/poligon.jpg)")
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/GTP/images/GTP Map/poligon.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")

        self.uPRRButton = QtWidgets.QPushButton(self.centralwidget)
        self.uPRRButton.setGeometry(QtCore.QRect(610, 170, 81, 40))
        self.uPRRButton.setMinimumSize(QtCore.QSize(0, 30))
        self.uPRRButton.setStyleSheet("QPushButton{\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgb(65, 102, 245);\n"
"border-style:outset;\n"
"border-radius:10px;\n"
"font: 100 14pt \"Arial\" ;\n"
"}\n"
"QPushButton:hover{\n"
"background-image: url(:/orange/images/orangebackgroundbutton.jpg);"
"color:rgb(0, 0, 05);\n"
"background-color: rgb(245, 169, 17);\n"
"border-radius:5px;\n"
"}\n"
"QPushButton:pressed{\n"
"color:rgb(0, 0, 0);\n"
"background-color: rgb(255, 148, 164);\n"
"}")
        self.uPRRButton.setObjectName("uPRRButton")
        self.uPRRButton.clicked.connect(self.uprr)

        self.uPVRButton = QtWidgets.QPushButton(self.centralwidget)
        self.uPVRButton.setGeometry(QtCore.QRect(480, 80, 81, 40))
        self.uPVRButton.setMinimumSize(QtCore.QSize(0, 30))
        self.uPVRButton.setStyleSheet("QPushButton{\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgb(65, 102, 245);\n"
"border-style:outset;\n"
"border-radius:10px;\n"
"font: 100 14pt \"Arial\" ;\n"
"}\n"
"QPushButton:hover{\n"
"background-image: url(:/orange/images/orangebackgroundbutton.jpg);"
"color:rgb(0, 0, 05);\n"
"background-color: rgb(245, 169, 17);\n"
"border-radius:5px;\n"
"}\n"
"QPushButton:pressed{\n"
"color:rgb(0, 0, 0);\n"
"background-color: rgb(255, 148, 164);\n"
"}")
        self.uPVRButton.setObjectName("uPVRButton")
        self.uPVRButton.clicked.connect(self.underConstruction)

        self.uPPRButton = QtWidgets.QPushButton(self.centralwidget)
        self.uPPRButton.setGeometry(QtCore.QRect(130, 170, 71, 40))
        self.uPPRButton.setMinimumSize(QtCore.QSize(0, 30))
        self.uPPRButton.setStyleSheet("QPushButton{\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgb(65, 102, 245);\n"
"border-style:outset;\n"
"border-radius:10px;\n"
"font: 100 14pt \"Arial\" ;\n"
"}\n"
"QPushButton:hover{\n"
"color:rgb(0, 0, 05);\n"
"background-color: rgb(245, 169, 17);\n"
"border-radius:5px;\n"
"}\n"
"QPushButton:pressed{\n"
"color:rgb(0, 0, 0);\n"
"background-color: rgb(255, 148, 164);\n"
"}")
        self.uPPRButton.setObjectName("uPPRButton")
        self.uPPRButton.clicked.connect(self.underConstruction)

        self.sZhRButton = QtWidgets.QPushButton(self.centralwidget)
        self.sZhRButton.setGeometry(QtCore.QRect(670, 60, 81, 40))
        self.sZhRButton.setMinimumSize(QtCore.QSize(0, 30))
        self.sZhRButton.setStyleSheet("QPushButton{\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgb(65, 102, 245);\n"
"border-style:outset;\n"
"border-radius:10px;\n"
"font: 100 14pt \"Arial\" ;\n"
"}\n"
"QPushButton:hover{\n"
"color:rgb(0, 0, 05);\n"
"background-color: rgb(245, 169, 17);\n"
"border-radius:5px;\n"
"}\n"
"QPushButton:pressed{\n"
"color:rgb(0, 0, 0);\n"
"background-color: rgb(255, 148, 164);\n"
"}")
        self.sZhRButton.setObjectName("sZhRButton")
        self.sZhRButton.clicked.connect(self.sZhR2)

        self.gtpMapButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.gtpMapButton_5.setGeometry(QtCore.QRect(260, 110, 181, 40))
        self.gtpMapButton_5.setMinimumSize(QtCore.QSize(0, 30))
        self.gtpMapButton_5.setStyleSheet("QPushButton{\n"

"color: rgb(0, 0, 0);\n"
"background-image: url(:/arrow right/Karatau blue background.png);"
"background-color: rgb(65, 102, 245);\n"
"border-style:outset;\n"
"border-radius:10px;\n"
"font: 100 14pt \"Arial\" ;\n"
"}\n"
"QPushButton:hover{\n"
"background-image: url(:/orange/images/orangebackgroundbutton.jpg);"
"color:rgb(0, 0, 05);\n"
"background-color: rgb(245, 169, 17);\n"
"border-radius:5px;\n"
"}\n"
"QPushButton:pressed{\n"
"color:rgb(0, 0, 0);\n"
"background-color: rgb(255, 148, 164);\n"
"}")
        self.gtpMapButton_5.setObjectName("gtpMapButton_5")
        self.gtpMapButton_5.clicked.connect(self.underConstruction)

        self.gtpMapButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.gtpMapButton_6.setGeometry(QtCore.QRect(60, 10, 81, 40))
        self.gtpMapButton_6.setMinimumSize(QtCore.QSize(0, 30))
        self.gtpMapButton_6.setStyleSheet("QPushButton{\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgb(65, 102, 245);\n"
"border-style:outset;\n"
"border-radius:10px;\n"
"font: 100 14pt \"Arial\" ;\n"
"}\n"
"QPushButton:hover{\n"
"color:rgb(0, 0, 05);\n"
"background-color: rgb(245, 169, 17);\n"
"border-radius:5px;\n"
"}\n"
"QPushButton:pressed{\n"
"color:rgb(0, 0, 0);\n"
"background-color: rgb(255, 148, 164);\n"
"}")
        self.gtpMapButton_6.setObjectName("gtpMapButton_6")
        self.gtpMapButton_6.clicked.connect(self.svyaz)

        self.label.raise_()
        self.uPPRButton.raise_()
        self.sZhRButton.raise_()
        self.uPRRButton.raise_()
        self.uPVRButton.raise_()
        self.gtpMapButton_5.raise_()
        self.gtpMapButton_6.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def gtpPoligon(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_GTPPoligon()
        self.ui.setupUi(self.window)
        #MainWindow.hide()
        self.window.show()

    def uprr(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_UPRR()
        self.ui.setupUi(self.window)
        #MainWindow.hide()
        self.window.show()

    def svyaz(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Svyaz()
        self.ui.setupUi(self.window)
        self.window.show()

    def sZhR2(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_SZhR2()
        self.ui.setupUi(self.window)
        self.window.show()

    def underConstruction(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_UnderConstruction()
        self.ui.setupUi(self.window)
        self.window.show()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Полигон"))
        self.uPRRButton.setText(_translate("MainWindow", "УПРР"))
        self.uPVRButton.setText(_translate("MainWindow", "УПВР"))
        self.uPPRButton.setText(_translate("MainWindow", "УППР"))
        self.sZhRButton.setText(_translate("MainWindow", "СЖР"))
        self.gtpMapButton_5.setText(_translate("MainWindow", "Шламотстойник"))
        self.gtpMapButton_6.setText(_translate("MainWindow", "Связь"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_GTPPoligon()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())