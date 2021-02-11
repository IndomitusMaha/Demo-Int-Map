# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

from PyQt5 import QtCore, QtGui, QtWidgets
import os
import subprocess

from resources import logos
from resources import MainWindowResources
from resources import MainWindowResourcesResize
from OtherWindow import Ui_OtherWindow
from GTPPoligon import Ui_GTPPoligon
from Global import Ui_GlobalMap
from Karatau import Ui_Karatau
from CPPR import  Ui_CPPR
from AP import Ui_AP
from GBK import Ui_GBK
from UnderConstruction import Ui_UnderConstruction

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setWindowIcon(QtGui.QIcon('karatauicon.png'))
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(760, 513)
        MainWindow.setStyleSheet("QWidget{\n"
"background-color: rgb(65, 102, 245);\n"
"background-image: url(:/logos/karatau_logo_small___копия-removebg-preview.png)\n"
"}")
        self.i = 1
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")

        #self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2 = QtWidgets.QGridLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")

        self.wlcomeToAppLabel = QtWidgets.QLabel(self.centralwidget)
        self.wlcomeToAppLabel.setMinimumSize(QtCore.QSize(0, 50))
        self.wlcomeToAppLabel.setStyleSheet("QLabel{\n"
"font: 14pt \"Segoe UI Emoji\";\n"
"color: rgb(0, 0, 0);\n"
"background-image: url(:/arrow right/images/Karatau yellow background.png);\n"
"border-style:outset;\n"
"border-radius:10px;\n"
"\n"
"}")
        self.wlcomeToAppLabel.setObjectName("wlcomeToAppLabel")
        self.wlcomeToAppLabel.setMaximumSize(QtCore.QSize(1000, 100))
        self.verticalLayout_2.addWidget(self.wlcomeToAppLabel, 0, 0)

        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")

        #self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2, 1, 0)

        """""
        self.imageLabel = QtWidgets.QLabel(self.centralwidget)
        self.imageLabel.setMinimumSize(QtCore.QSize(0, 300))
        self.imageLabel.setText("")
        self.imageLabel.setObjectName("imageLabel")

        self.verticalLayout_2.addWidget(self.imageLabel)
        """""


        self.imageLabel = QtWidgets.QLabel(self.centralwidget)
        self.imageLabel.setMinimumSize(QtCore.QSize(0, 300))
        self.imageLabel.setMaximumSize(QtCore.QSize(1100, 1600))
        self.imageLabel.setPixmap(QtGui.QPixmap(":/Resize/images/ФотоУмень/01.jpg"))
        #self.imageLabel.setPixmap(QtGui.QPixmap(":/arrow right/images/ФотоКаратау/01.jpg"))
        self.imageLabel.setScaledContents(True)
        self.imageLabel.setObjectName("imageLabel")
        self.imageLabel.setText("")

        self.verticalLayout_2.addWidget(self.imageLabel, 3, 0)

        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")

        self.verticalLayout_2.addWidget(self.line, 4, 0)

        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 0, 4, 1, 1)

        self.previousImgButton = QtWidgets.QPushButton(self.centralwidget)
        self.previousImgButton.setMinimumSize(QtCore.QSize(60, 45))
        self.previousImgButton.setStyleSheet("QPushButton{\n"
"color: rgb(0, 0, 0);\n"
"border-image: url(:/arrow right/images/yel arr left.png);\n"
"border-style:outset;\n"
"border-radius:8px;\n"
"font: 10pt \"Arial\" ;\n"
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
        self.previousImgButton.setText("")
        self.previousImgButton.setObjectName("previousImgButton")
        self.previousImgButton.clicked.connect(self.countminus)
        self.previousImgButton.clicked.connect(self.ch_Image)

        self.gridLayout_2.addWidget(self.previousImgButton, 0, 0, 1, 1)
        self.nextImgButton = QtWidgets.QPushButton(self.centralwidget)
        self.nextImgButton.setMinimumSize(QtCore.QSize(60, 45))
        self.nextImgButton.setStyleSheet("QPushButton{\n"
"color: rgb(0, 0, 0);\n"
"border-image: url(:/arrow right/images/yel arr right.png);\n"
"border-style:outset;\n"
"border-radius:8px;\n"
"font: 10pt \"Arial\" ;\n"
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
        self.nextImgButton.setText("")
        self.nextImgButton.setObjectName("nextImgButton")
        self.nextImgButton.clicked.connect(self.countplus)
        self.nextImgButton.clicked.connect(self.ch_Image)

        self.gridLayout_2.addWidget(self.nextImgButton, 0, 2, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem1, 1, 3, 1, 1)

        self.goToSiteButton = QtWidgets.QPushButton(self.centralwidget)
        self.goToSiteButton.setStyleSheet("QPushButton{\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgb(246, 250, 5);\n"
"border-style:outset;\n"
"border-radius:8px;\n"
"font: 80 10pt \"Arial\" ;\n"
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
        self.goToSiteButton.setObjectName("goToSiteButton")
        self.goToSiteButton.clicked.connect(self.goToSite) #функция в другом модуле

        self.gridLayout_2.addWidget(self.goToSiteButton, 1, 4, 1, 1)
        self.emptySpaceLabel = QtWidgets.QLabel(self.centralwidget)
        self.emptySpaceLabel.setText("")
        self.emptySpaceLabel.setObjectName("emptySpaceLabel")
        self.gridLayout_2.addWidget(self.emptySpaceLabel, 0, 3, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem2, 0, 1, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout_2, 5, 0)
        self.gridLayout.addLayout(self.verticalLayout_2, 0, 2, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")

        self.modeLabel = QtWidgets.QLabel(self.centralwidget)
        self.modeLabel.setMinimumSize(QtCore.QSize(35, 24))
        self.modeLabel.setStyleSheet("QLabel{\n"
"font: 75 14pt \"Segoe UI Emoji\";\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgb(246, 250, 5);\n"
"border-style:outset;\n"
"border-radius:10px;\n"
"\n"
"}\n"
"")
        self.modeLabel.setObjectName("modeLabel")

        self.verticalLayout.addWidget(self.modeLabel)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.workerRadioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.workerRadioButton.setStyleSheet("QRadioButton{\n"
"color: rgb(0, 0, 0);\n"
"border-style:outset;\n"
"border-radius:10px;\n"
"font: 10pt \"Arial\";\n"
"}\n"
"")
        self.workerRadioButton.setObjectName("workerRadioButton")

        self.horizontalLayout.addWidget(self.workerRadioButton)
        self.guestRadioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.guestRadioButton.setMinimumSize(QtCore.QSize(56, 0))
        self.guestRadioButton.setStyleSheet("QRadioButton{\n"
"color: rgb(0, 0, 0);\n"
"border-style:outset;\n"
"border-radius:10px;\n"
"font: 10pt \"Arial\" ;\n"
"}\n"
"")
        self.guestRadioButton.setObjectName("guestRadioButton")
        self.horizontalLayout.addWidget(self.guestRadioButton)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.welcomeVideoButton = QtWidgets.QPushButton(self.centralwidget)
        self.welcomeVideoButton.setStyleSheet("QPushButton{\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgb(246, 250, 5);\n"
"border-style:outset;\n"
"border-radius:10px;\n"
"font: 14pt \"Arial\" ;\n"
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
        self.welcomeVideoButton.setObjectName("welcomeVideoButton")
        self.welcomeVideoButton.clicked.connect(self.welcomeVideo)

        self.verticalLayout.addWidget(self.welcomeVideoButton)

        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem3)

        self.gtpMapButton = QtWidgets.QPushButton(self.centralwidget)
        self.gtpMapButton.setMinimumSize(QtCore.QSize(0, 30))
        self.gtpMapButton.setStyleSheet("QPushButton{\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgb(246, 250, 5);\n"
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
        self.gtpMapButton.setObjectName("gtpMapButton")
        self.gtpMapButton.clicked.connect(self.gtpPoligon)

        self.verticalLayout.addWidget(self.gtpMapButton)

        self.cpprMapButton = QtWidgets.QPushButton(self.centralwidget)
        self.cpprMapButton.setMinimumSize(QtCore.QSize(0, 30))
        self.cpprMapButton.setStyleSheet("QPushButton{\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgb(246, 250, 5);\n"
"border-style:outset;\n"
"border-radius:10px;\n"
"font: 14pt \"Arial\" ;\n"
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
        self.cpprMapButton.setObjectName("cpprMapButton")
        self.cpprMapButton.clicked.connect(self.cppr)

        self.verticalLayout.addWidget(self.cpprMapButton)

        self.apMapButton = QtWidgets.QPushButton(self.centralwidget)
        self.apMapButton.setMinimumSize(QtCore.QSize(0, 30))
        self.apMapButton.setStyleSheet("QPushButton{\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgb(246, 250, 5);\n"
"border-style:outset;\n"
"border-radius:10px;\n"
"font: 14pt \"Arial\" ;\n"
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
        self.apMapButton.setObjectName("apMapButton")
        self.apMapButton.clicked.connect(self.ap)

        self.verticalLayout.addWidget(self.apMapButton)

        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem4)
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.verticalLayout.addWidget(self.line_3)

        self.goToKaratauMapButton = QtWidgets.QPushButton(self.centralwidget)
        self.goToKaratauMapButton.setMinimumSize(QtCore.QSize(0, 50))
        self.goToKaratauMapButton.setStyleSheet("QPushButton{\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgb(246, 250, 5);\n"
"border-style:outset;\n"
"border-radius:10px;\n"
"font: 14pt \"Segoe UI Emoji\" ;\n"
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
        self.goToKaratauMapButton.setObjectName("goToKaratauMapButton")
        self.goToKaratauMapButton.clicked.connect(self.karatauMap)

        self.verticalLayout.addWidget(self.goToKaratauMapButton)

        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.gridLayout.addWidget(self.line_2, 0, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 760, 21))
        self.menubar.setStyleSheet("QMenuBar{background-color: rgb(246, 250, 5);\n"
                                   "background-image: url(:/arrow right/images/Karatau yellow background.png);\n"
                                   "}\n"
                                   "QMenuBar:hover{\n"
                                   "color:rgb(0, 0, 05);\n"
                                   "background-color: rgb(245, 169, 17);\n"
                                   "\n"
                                   "}")
        self.menubar.setObjectName("menubar")

        self.menuMaps = QtWidgets.QMenu(self.menubar)
        self.menuMaps.setObjectName("menuMaps")

        self.menuAboutUs = QtWidgets.QMenu(self.menubar)
        self.menuAboutUs.setObjectName("menuAboutUs")

        self.menuObjects = QtWidgets.QMenu(self.menubar)
        self.menuObjects.setObjectName("menuObjects")

        self.menuActionGTP = QtWidgets.QMenu(self.menuObjects)
        self.menuActionGTP.setObjectName("menuActionGTP")

        self.menuActionFKhL = QtWidgets.QMenu(self.menuObjects)
        self.menuActionFKhL.setObjectName("menuActionFKhL")

        self.menuDepartments = QtWidgets.QMenu(self.menubar)
        self.menuDepartments.setObjectName("menuDepartments")

        self.menuWhatIsIt = QtWidgets.QMenu(self.menubar)
        self.menuWhatIsIt.setObjectName("menuWhatIsIt")

        MainWindow.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setStyleSheet("")
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.actionGlobalMap = QtWidgets.QAction(MainWindow)
        self.actionGlobalMap.setObjectName("actionGlobalMap")
        self.actionGlobalMap.triggered.connect(self.globalMap)

        self.actionCPPR = QtWidgets.QAction(MainWindow)
        self.actionCPPR.setObjectName("actionCPPR")
        self.actionCPPR.triggered.connect(self.cppr)

        self.actionAP = QtWidgets.QAction(MainWindow)
        self.actionAP.setObjectName("actionAP")
        self.actionAP.triggered.connect(self.ap)

        self.actionGBK = QtWidgets.QAction(MainWindow)
        self.actionGBK.setObjectName("actionGBK")
        self.actionGBK.triggered.connect(self.gbk)

        self.actionPoligon = QtWidgets.QAction(MainWindow)
        self.actionPoligon.setObjectName("actionPoligon")
        self.actionPoligon.triggered.connect(self.gtpPoligon)

        self.actionRaskomandirovka = QtWidgets.QAction(MainWindow)
        self.actionRaskomandirovka.setObjectName("actionRaskomandirovka")
        self.actionRaskomandirovka.triggered.connect(self.underConstruction)

        self.actionFKhLFirstFloor = QtWidgets.QAction(MainWindow)
        self.actionFKhLFirstFloor.setObjectName("actionFKhLFirstFloor")
        self.actionFKhLFirstFloor.triggered.connect(self.underConstruction)

        self.actionFKhLSecondFloor = QtWidgets.QAction(MainWindow)
        self.actionFKhLSecondFloor.setObjectName("actionFKhLSecondFloor")
        self.actionFKhLSecondFloor.triggered.connect(self.underConstruction)

        self.KIPiA = QtWidgets.QAction(MainWindow)
        self.KIPiA.setCheckable(False)
        self.KIPiA.triggered.connect(self.underConstruction)
        self.KIPiA.setObjectName("KIPiA")

        self.SGE = QtWidgets.QAction(MainWindow)
        self.SGE.setObjectName("SGE")
        self.SGE.triggered.connect(self.underConstruction)

        self.SGM = QtWidgets.QAction(MainWindow)
        self.SGM.setObjectName("SGM")
        self.SGM.triggered.connect(self.underConstruction)

        self.actionKaratauMap = QtWidgets.QAction(MainWindow)
        self.actionKaratauMap.setObjectName("actionKaratauMap")
        self.actionKaratauMap.triggered.connect(self.karatauMap)

        self.menuMaps.addAction(self.actionGlobalMap)
        self.menuMaps.addAction(self.actionKaratauMap)
        self.menuActionGTP.addAction(self.actionPoligon)
        self.menuActionGTP.addAction(self.actionRaskomandirovka)
        self.menuActionFKhL.addAction(self.actionFKhLFirstFloor)
        self.menuActionFKhL.addAction(self.actionFKhLSecondFloor)
        self.menuObjects.addAction(self.menuActionGTP.menuAction())
        self.menuObjects.addAction(self.actionCPPR)
        self.menuObjects.addAction(self.actionAP)
        self.menuObjects.addSeparator()
        self.menuObjects.addAction(self.actionGBK)
        self.menuObjects.addAction(self.menuActionFKhL.menuAction())
        self.menuDepartments.addAction(self.KIPiA)
        self.menuDepartments.addAction(self.SGE)
        self.menuDepartments.addAction(self.SGM)
        self.menubar.addAction(self.menuMaps.menuAction())
        self.menubar.addAction(self.menuAboutUs.menuAction())
        self.menubar.addAction(self.menuObjects.menuAction())
        self.menubar.addAction(self.menuDepartments.menuAction())
        self.menubar.addAction(self.menuWhatIsIt.menuAction())


        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def countminus(self):
        self.i = self.i-1
        if self.i < 1:
            self.i = 1

    def countplus(self):
        self.i = self.i+1
        if self.i > 4:
            self.i = 4

    def ch_Image(self):
        print(self.i)
        if self.i == 1:
            self.imageLabel = QtWidgets.QLabel(self.centralwidget)
            self.imageLabel.setMinimumSize(QtCore.QSize(0, 300))
            self.imageLabel.setMaximumSize(QtCore.QSize(1100, 1600))
            self.imageLabel.setPixmap(QtGui.QPixmap(":/Resize/images/ФотоУмень/01.jpg"))
            self.imageLabel.setScaledContents(True)
            self.imageLabel.setObjectName("imageLabel")
            self.imageLabel.setText("")

            self.verticalLayout_2.addWidget(self.imageLabel, 3, 0)
        if self.i == 2:
            self.imageLabel = QtWidgets.QLabel(self.centralwidget)
            self.imageLabel.setMinimumSize(QtCore.QSize(0, 300))
            self.imageLabel.setMaximumSize(QtCore.QSize(1100, 1600))
            self.imageLabel.setPixmap(QtGui.QPixmap(":/Resize/images/ФотоУмень/02.jpg"))
            self.imageLabel.setScaledContents(True)
            self.imageLabel.setObjectName("imageLabel")
            self.imageLabel.setText("")

            self.verticalLayout_2.addWidget(self.imageLabel, 3, 0)
        if self.i == 3:
            self.imageLabel = QtWidgets.QLabel(self.centralwidget)
            self.imageLabel.setMinimumSize(QtCore.QSize(0, 300))
            self.imageLabel.setMaximumSize(QtCore.QSize(1100, 1600))
            self.imageLabel.setPixmap(QtGui.QPixmap(":/Resize/images/ФотоУмень/03.jpg"))
            self.imageLabel.setScaledContents(True)
            self.imageLabel.setObjectName("imageLabel")
            self.imageLabel.setText("")

            self.verticalLayout_2.addWidget(self.imageLabel, 3, 0)
        if self.i == 4:
            self.imageLabel = QtWidgets.QLabel(self.centralwidget)
            self.imageLabel.setMinimumSize(QtCore.QSize(0, 300))
            self.imageLabel.setMaximumSize(QtCore.QSize(1100, 1600))
            self.imageLabel.setPixmap(QtGui.QPixmap(":/Resize/images/ФотоУмень/04.jpg"))
            self.imageLabel.setScaledContents(True)
            self.imageLabel.setObjectName("imageLabel")
            self.imageLabel.setText("")

            self.verticalLayout_2.addWidget(self.imageLabel, 3, 0)

    def cppr(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_CPPR()
        self.ui.setupUi(self.window)
        self.window.show()

    def ap(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_AP()
        self.ui.setupUi(self.window)
        self.window.show()

    def globalMap(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_GlobalMap()
        self.ui.setupUi(self.window)
        self.window.show()

    def karatauMap(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Karatau()
        self.ui.setupUi(self.window)
        self.window.show()

    def gbk(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_GBK()
        self.ui.setupUi(self.window)
        self.window.show()

    def underConstruction(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_UnderConstruction()
        self.ui.setupUi(self.window)
        self.window.show()

    def gtpPoligon(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_GTPPoligon()
        self.ui.setupUi(self.window)
        #MainWindow.hide()
        self.window.show()
     
    def welcomeVideo(self):
        script_path = os.path.abspath(__file__)
        script_dir = os.path.split(script_path)[0]
        rel_path = "resources//videos//Казатомпром.mp4"
        abs_file_path = os.path.join(script_dir, rel_path)
        #os.startfile(abs_file_path)
        subprocess.Popen(["cmd", "/C", "start " + rel_path], shell=True)

    def goToSite(self):
        script_path = os.path.abspath(__file__)
        script_dir = os.path.split(script_path)[0]
        rel_path = "resources//links//Karatau.url"
        abs_file_path = os.path.join(script_dir, rel_path)
        # os.startfile(abs_file_path)
        # subprocess.call(abs_file_path, shell=True)
        subprocess.Popen(["cmd", "/C", "start " + rel_path], shell=True)



    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.wlcomeToAppLabel.setText(_translate("MainWindow", "  Добро пожаловать в интерактивный гайд по руднику Каратау     "))
        self.goToSiteButton.setText(_translate("MainWindow", "Перейти на сайт"))
        self.modeLabel.setText(_translate("MainWindow", "        Режим"))
        self.workerRadioButton.setText(_translate("MainWindow", "Сотрудник"))
        self.guestRadioButton.setText(_translate("MainWindow", "Гость"))
        self.welcomeVideoButton.setText(_translate("MainWindow", "Приветствие    "))
        self.gtpMapButton.setText(_translate("MainWindow", "ГТП"))
        self.cpprMapButton.setText(_translate("MainWindow", "ЦППР"))
        self.apMapButton.setText(_translate("MainWindow", "АП"))
        self.goToKaratauMapButton.setText(_translate("MainWindow", "Карта"))
        #menu widget
        self.menuMaps.setTitle(_translate("MainWindow", "Карты"))
        self.menuAboutUs.setTitle(_translate("MainWindow", "О нас"))
        self.menuObjects.setTitle(_translate("MainWindow", "Цеха и объекты"))
        self.menuActionGTP.setTitle(_translate("MainWindow", "ГТП"))
        self.menuActionFKhL.setTitle(_translate("MainWindow", "ФХЛ"))
        self.menuDepartments.setTitle(_translate("MainWindow", "Службы"))
        self.menuWhatIsIt.setTitle(_translate("MainWindow", "Что это такое?"))
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
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
