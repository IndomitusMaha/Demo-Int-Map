# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'FKhL.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from resources import logos
from resources import MainWindowResources
from resources import MapsResizeResources


class Ui_FKhL(object):
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
        self.privetstvieButton.setGeometry(QtCore.QRect(10, 120, 171, 31))
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
        self.perviietazhButton = QtWidgets.QPushButton(self.centralwidget)
        self.perviietazhButton.setGeometry(QtCore.QRect(10, 170, 171, 31))
        self.perviietazhButton.setMinimumSize(QtCore.QSize(0, 30))
        self.perviietazhButton.setStyleSheet("QPushButton{\n"
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
        self.perviietazhButton.setObjectName("perviietazhButton")
        self.Logos = QtWidgets.QLabel(self.centralwidget)
        self.Logos.setGeometry(QtCore.QRect(10, 450, 101, 41))
        self.Logos.setStyleSheet("QLabel {url(:/logos/logos-2.png);}")
        self.Logos.setText("")
        self.Logos.setPixmap(QtGui.QPixmap(":/logos/logos-2.png"))
        self.Logos.setScaledContents(True)
        self.Logos.setObjectName("Logos")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(190, 0, 511, 511))
        self.label.setStyleSheet("Background-image:url(:/MapsResize/images/MapsУмень/ФХЛ.jpg)")
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/MapsResize/images/MapsУмень/ФХЛ.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.szhrButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.szhrButton_2.setGeometry(QtCore.QRect(10, 220, 171, 31))
        self.szhrButton_2.setMinimumSize(QtCore.QSize(0, 30))
        self.szhrButton_2.setStyleSheet("QPushButton{\n"
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
        self.szhrButton_2.setObjectName("szhrButton_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.actionGlobalMap = QtWidgets.QAction(MainWindow)
        self.actionGlobalMap.setObjectName("actionGlobalMap")
        self.actionCPPR = QtWidgets.QAction(MainWindow)
        self.actionCPPR.setObjectName("actionCPPR")
        self.actionAP = QtWidgets.QAction(MainWindow)
        self.actionAP.setObjectName("actionAP")
        self.actionGBK = QtWidgets.QAction(MainWindow)
        self.actionGBK.setObjectName("actionGBK")
        self.actionPoligon = QtWidgets.QAction(MainWindow)
        self.actionPoligon.setObjectName("actionPoligon")
        self.actionRaskomandirovka = QtWidgets.QAction(MainWindow)
        self.actionRaskomandirovka.setObjectName("actionRaskomandirovka")
        self.actionFKhLFirstFloor = QtWidgets.QAction(MainWindow)
        self.actionFKhLFirstFloor.setObjectName("actionFKhLFirstFloor")
        self.actionFKhLSecondFloor = QtWidgets.QAction(MainWindow)
        self.actionFKhLSecondFloor.setObjectName("actionFKhLSecondFloor")
        self.KIPiA = QtWidgets.QAction(MainWindow)
        self.KIPiA.setCheckable(False)
        self.KIPiA.setObjectName("KIPiA")
        self.SGE = QtWidgets.QAction(MainWindow)
        self.SGE.setObjectName("SGE")
        self.SGM = QtWidgets.QAction(MainWindow)
        self.SGM.setObjectName("SGM")
        self.actionKaratauMap = QtWidgets.QAction(MainWindow)
        self.actionKaratauMap.setObjectName("actionKaratauMap")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "ФХЛ"))
        self.privetstvieButton.setText(_translate("MainWindow", "Приветствие"))
        self.perviietazhButton.setText(_translate("MainWindow", "1-ый этаж"))
        self.szhrButton_2.setText(_translate("MainWindow", "2-ой этаж"))
        self.actionGlobalMap.setText(_translate("MainWindow", "Глобальная"))
        self.actionCPPR.setText(_translate("MainWindow", "ЦППР"))
        self.actionAP.setText(_translate("MainWindow", "АП"))
        self.actionGBK.setText(_translate("MainWindow", "ГБК"))
        self.actionPoligon.setText(_translate("MainWindow", "Полигон"))
        self.actionRaskomandirovka.setText(_translate("MainWindow", "Раскомандировка"))
        self.actionFKhLFirstFloor.setText(_translate("MainWindow", "Первый этаж"))
        self.actionFKhLSecondFloor.setText(_translate("MainWindow", "Второй этаж"))
        self.KIPiA.setText(_translate("MainWindow", "КИПиА"))
        self.SGE.setText(_translate("MainWindow", "СГЭ"))
        self.SGM.setText(_translate("MainWindow", "СГМ"))
        self.actionKaratauMap.setText(_translate("MainWindow", "Каратау"))
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_FKhL()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
