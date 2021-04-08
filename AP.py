# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AP.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from resources import logos
from resources import MainWindowResources
from resources import MapsResizeResources

class Ui_AP(object):
    def setupUi(self, MainWindow):
        MainWindow.setWindowIcon(QtGui.QIcon('karatauicon.png'))
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(700, 513)
        MainWindow.setMinimumSize(QtCore.QSize(700, 513))
        MainWindow.setMaximumSize(QtCore.QSize(700, 513))
        MainWindow.setStyleSheet("QWidget{\n"
"background-color: rgb(65, 102, 245);\n"
"background-image: url(:/logos/karatau_logo_small___копия-removebg-preview.png)\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")
        self.privetstvieButton = QtWidgets.QPushButton(self.centralwidget)
        self.privetstvieButton.setGeometry(QtCore.QRect(10, 50, 171, 31))
        self.privetstvieButton.setMinimumSize(QtCore.QSize(0, 30))
        self.privetstvieButton.setMaximumSize(QtCore.QSize(16777198, 16777215))
        self.privetstvieButton.setStyleSheet("QPushButton{\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgb(246, 250, 5);\n"
"background-image: url(:/arrow right/images/Karatau yellow background.png);\n"
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
        self.privetstvieButton.setObjectName("privetstvieButton")
        self.sorbciaButton = QtWidgets.QPushButton(self.centralwidget)
        self.sorbciaButton.setGeometry(QtCore.QRect(10, 100, 171, 31))
        self.sorbciaButton.setMinimumSize(QtCore.QSize(0, 30))
        self.sorbciaButton.setStyleSheet("QPushButton{\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgb(246, 250, 5);\n"
"background-image: url(:/arrow right/images/Karatau yellow background.png);\n"
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
        self.sorbciaButton.setObjectName("sorbciaButton")
        self.desorbciaButton = QtWidgets.QPushButton(self.centralwidget)
        self.desorbciaButton.setGeometry(QtCore.QRect(10, 150, 171, 31))
        self.desorbciaButton.setMinimumSize(QtCore.QSize(0, 30))
        self.desorbciaButton.setStyleSheet("QPushButton{\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgb(246, 250, 5);\n"
"background-image: url(:/arrow right/images/Karatau yellow background.png);\n"
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
        self.desorbciaButton.setObjectName("desorbciaButton")
        self.Logos = QtWidgets.QLabel(self.centralwidget)
        self.Logos.setGeometry(QtCore.QRect(10, 450, 101, 41))
        self.Logos.setStyleSheet("QLabel {url(:/logos/logos-2.png);}")
        self.Logos.setText("")
        self.Logos.setPixmap(QtGui.QPixmap(":/logos/logos-2.png"))
        self.Logos.setScaledContents(True)
        self.Logos.setObjectName("Logos")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(190, 0, 511, 521))
        self.label.setStyleSheet("Background-image:url(:/MapsResize/images/MapsУмень/АП.jpg)")
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/MapsResize/images/MapsУмень/АП.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.podgotovkaButton = QtWidgets.QPushButton(self.centralwidget)
        self.podgotovkaButton.setGeometry(QtCore.QRect(10, 200, 171, 31))
        self.podgotovkaButton.setMinimumSize(QtCore.QSize(0, 30))
        self.podgotovkaButton.setStyleSheet("QPushButton{\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgb(246, 250, 5);\n"
"background-image: url(:/arrow right/images/Karatau yellow background.png);\n"
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
        self.podgotovkaButton.setObjectName("podgotovkaButton")

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Афинажный цех"))
        self.privetstvieButton.setText(_translate("MainWindow", "Приветствие"))
        self.sorbciaButton.setText(_translate("MainWindow", "Каскад"))
        self.desorbciaButton.setText(_translate("MainWindow", "Фильтр-пресс"))
        self.podgotovkaButton.setText(_translate("MainWindow", "Подготовка"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_AP()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())