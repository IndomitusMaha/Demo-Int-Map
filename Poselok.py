# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Poselok.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from resources import GTPResources
from resources import MapsResizeResources
from resources import OrangeBackgroundResources
from GBK import Ui_GBK

class Ui_Poselok(object):
    def setupUi(self, MainWindow):
        MainWindow.setWindowIcon(QtGui.QIcon('karatauicon.png'))
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 500)
        MainWindow.setMinimumSize(QtCore.QSize(800, 500))
        MainWindow.setMaximumSize(QtCore.QSize(800, 500))
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setMinimumSize(QtCore.QSize(800, 500))
        self.centralwidget.setMaximumSize(QtCore.QSize(800, 16777215))
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")
        self.labelMap = QtWidgets.QLabel(self.centralwidget)
        self.labelMap.setEnabled(True)
        self.labelMap.setGeometry(QtCore.QRect(0, 0, 800, 500))
        self.labelMap.setMinimumSize(QtCore.QSize(800, 500))
        self.labelMap.setMaximumSize(QtCore.QSize(800, 500))
        self.labelMap.setStyleSheet("background-image: url(:/MapsResize/images/MapsУмень/Вахтовый Поселок.jpg)")
        self.labelMap.setText("")
        self.labelMap.setPixmap(QtGui.QPixmap(":/MapsResize/images/MapsУмень/Вахтовый Поселок.jpg"))
        self.labelMap.setScaledContents(True)
        self.labelMap.setObjectName("labelMap")

        self.obshezhitieLabel = QtWidgets.QLabel(self.centralwidget)
        self.obshezhitieLabel.setGeometry(QtCore.QRect(150, 340, 145, 26))
        self.obshezhitieLabel.setMaximumSize(QtCore.QSize(700, 16777215))
        self.obshezhitieLabel.setStyleSheet("background-image: url(:/arrow right/Karatau blue background.png);\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgb(65, 102, 245);\n"
"font: 100 14pt \"Arial\" ")
        self.obshezhitieLabel.setObjectName("obshezhitieLabel")

        self.gbkButton = QtWidgets.QPushButton(self.centralwidget)
        self.gbkButton.setEnabled(True)
        self.gbkButton.setGeometry(QtCore.QRect(540, 350, 71, 40))
        self.gbkButton.setMinimumSize(QtCore.QSize(0, 30))
        self.gbkButton.setStyleSheet("QPushButton{\n"
"background-image: url(:/arrow right/Karatau blue background.png);\n"
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
"border-radius:20px;\n"
"}")
        self.gbkButton.setObjectName("gbkButton")
        self.gbkButton.clicked.connect(self.gbk)

        self.sportKompleksLabel = QtWidgets.QLabel(self.centralwidget)
        self.sportKompleksLabel.setGeometry(QtCore.QRect(200, 250, 251, 26))
        self.sportKompleksLabel.setStyleSheet("background-image: url(:/arrow right/Karatau blue background.png);\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgb(65, 102, 245);\n"
"font: 100 14pt \"Arial\" ")
        self.sportKompleksLabel.setObjectName("sportKompleksLabel")
        self.kottedzhiLabel = QtWidgets.QLabel(self.centralwidget)
        self.kottedzhiLabel.setGeometry(QtCore.QRect(390, 140, 121, 26))
        self.kottedzhiLabel.setStyleSheet("background-image: url(:/arrow right/Karatau blue background.png);\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgb(65, 102, 245);\n"
"font: 100 14pt \"Arial\" ")
        self.kottedzhiLabel.setObjectName("kottedzhiLabel")
        self.techVodaLabel_2 = QtWidgets.QLabel(self.centralwidget)
        self.techVodaLabel_2.setGeometry(QtCore.QRect(580, 200, 111, 26))
        self.techVodaLabel_2.setStyleSheet("background-image: url(:/arrow right/Karatau blue background.png);\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgb(65, 102, 245);\n"
"font: 100 14pt \"Arial\" ")
        self.techVodaLabel_2.setObjectName("techVodaLabel_2")
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

    def gbk(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_GBK()
        self.ui.setupUi(self.window)
        self.window.show()


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Вахтовый поселок"))
        self.obshezhitieLabel.setText(_translate("MainWindow", " Общежитие"))
        self.gbkButton.setText(_translate("MainWindow", "ГБК"))
        self.sportKompleksLabel.setText(_translate("MainWindow", " Спортивный комплекс"))
        self.kottedzhiLabel.setText(_translate("MainWindow", "  Коттеджи"))
        self.techVodaLabel_2.setText(_translate("MainWindow", " Тех. Вода"))
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
    ui = Ui_Poselok()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
