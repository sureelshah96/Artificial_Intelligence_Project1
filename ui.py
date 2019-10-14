# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1013, 822)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.titleLb = QtWidgets.QLabel(self.centralwidget)
        self.titleLb.setGeometry(QtCore.QRect(170, 40, 672, 40))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.titleLb.setFont(font)
        self.titleLb.setAlignment(QtCore.Qt.AlignCenter)
        self.titleLb.setObjectName("titleLb")
        self.authorLb = QtWidgets.QLabel(self.centralwidget)
        self.authorLb.setGeometry(QtCore.QRect(600, 90, 240, 27))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.authorLb.setFont(font)
        self.authorLb.setAlignment(QtCore.Qt.AlignCenter)
        self.authorLb.setObjectName("authorLb")
        self.game_modeCB = QtWidgets.QComboBox(self.centralwidget)
        self.game_modeCB.setGeometry(QtCore.QRect(50, 160, 171, 29))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(14)
        self.game_modeCB.setFont(font)
        self.game_modeCB.setObjectName("game_modeCB")
        self.game_modeCB.addItem("")
        self.game_modeCB.addItem("")
        self.game_modeCB.addItem("")
        self.game_modeLb = QtWidgets.QLabel(self.centralwidget)
        self.game_modeLb.setGeometry(QtCore.QRect(50, 120, 150, 27))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.game_modeLb.setFont(font)
        self.game_modeLb.setObjectName("game_modeLb")
        self.search_methodCB = QtWidgets.QComboBox(self.centralwidget)
        self.search_methodCB.setGeometry(QtCore.QRect(50, 270, 91, 29))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(14)
        self.search_methodCB.setFont(font)
        self.search_methodCB.setObjectName("search_methodCB")
        self.search_methodCB.addItem("")
        self.search_methodLb = QtWidgets.QLabel(self.centralwidget)
        self.search_methodLb.setGeometry(QtCore.QRect(50, 220, 210, 27))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.search_methodLb.setFont(font)
        self.search_methodLb.setObjectName("search_methodLb")
        self.imageLb = QtWidgets.QLabel(self.centralwidget)
        self.imageLb.setGeometry(QtCore.QRect(350, 140, 620, 620))
        self.imageLb.setMinimumSize(QtCore.QSize(620, 620))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(48)
        self.imageLb.setFont(font)
        self.imageLb.setAlignment(QtCore.Qt.AlignCenter)
        self.imageLb.setObjectName("imageLb")
        self.select_image1Lb = QtWidgets.QLabel(self.centralwidget)
        self.select_image1Lb.setGeometry(QtCore.QRect(50, 330, 200, 50))
        self.select_image1Lb.setMinimumSize(QtCore.QSize(200, 50))
        self.select_image1Lb.setMaximumSize(QtCore.QSize(16777215, 60))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.select_image1Lb.setFont(font)
        self.select_image1Lb.setObjectName("select_image1Lb")
        self.select_imageSB = QtWidgets.QSpinBox(self.centralwidget)
        self.select_imageSB.setGeometry(QtCore.QRect(240, 410, 58, 29))
        self.select_imageSB.setMinimumSize(QtCore.QSize(0, 20))
        self.select_imageSB.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.select_imageSB.setFont(font)
        self.select_imageSB.setAlignment(QtCore.Qt.AlignCenter)
        self.select_imageSB.setMinimum(1)
        self.select_imageSB.setMaximum(28)
        self.select_imageSB.setObjectName("select_imageSB")
        self.select_image2Lb = QtWidgets.QLabel(self.centralwidget)
        self.select_image2Lb.setGeometry(QtCore.QRect(50, 400, 180, 50))
        self.select_image2Lb.setMinimumSize(QtCore.QSize(180, 50))
        self.select_image2Lb.setMaximumSize(QtCore.QSize(16777215, 60))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.select_image2Lb.setFont(font)
        self.select_image2Lb.setObjectName("select_image2Lb")
        self.select_image3Lb = QtWidgets.QLabel(self.centralwidget)
        self.select_image3Lb.setGeometry(QtCore.QRect(50, 470, 221, 50))
        self.select_image3Lb.setMinimumSize(QtCore.QSize(0, 50))
        self.select_image3Lb.setMaximumSize(QtCore.QSize(16777215, 60))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.select_image3Lb.setFont(font)
        self.select_image3Lb.setObjectName("select_image3Lb")
        self.select_imageLE = QtWidgets.QLineEdit(self.centralwidget)
        self.select_imageLE.setGeometry(QtCore.QRect(50, 530, 261, 30))
        self.select_imageLE.setMinimumSize(QtCore.QSize(0, 30))
        self.select_imageLE.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(14)
        self.select_imageLE.setFont(font)
        self.select_imageLE.setObjectName("select_imageLE")
        self.areaLb = QtWidgets.QLabel(self.centralwidget)
        self.areaLb.setGeometry(QtCore.QRect(50, 580, 191, 50))
        self.areaLb.setMinimumSize(QtCore.QSize(180, 50))
        self.areaLb.setMaximumSize(QtCore.QSize(16777215, 60))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.areaLb.setFont(font)
        self.areaLb.setObjectName("areaLb")
        self.areaSB = QtWidgets.QSpinBox(self.centralwidget)
        self.areaSB.setGeometry(QtCore.QRect(250, 590, 81, 29))
        self.areaSB.setMinimumSize(QtCore.QSize(0, 20))
        self.areaSB.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.areaSB.setFont(font)
        self.areaSB.setAlignment(QtCore.Qt.AlignCenter)
        self.areaSB.setMinimum(0)
        self.areaSB.setMaximum(23333)
        self.areaSB.setStepType(QtWidgets.QAbstractSpinBox.DefaultStepType)
        self.areaSB.setProperty("value", 8)
        self.areaSB.setObjectName("areaSB")
        self.load_imageBtn = QtWidgets.QPushButton(self.centralwidget)
        self.load_imageBtn.setGeometry(QtCore.QRect(60, 670, 120, 60))
        self.load_imageBtn.setMinimumSize(QtCore.QSize(120, 60))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.load_imageBtn.setFont(font)
        self.load_imageBtn.setObjectName("load_imageBtn")
        self.solveBtn = QtWidgets.QPushButton(self.centralwidget)
        self.solveBtn.setGeometry(QtCore.QRect(210, 670, 120, 60))
        self.solveBtn.setMinimumSize(QtCore.QSize(120, 60))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.solveBtn.setFont(font)
        self.solveBtn.setObjectName("solveBtn")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.game_modeCB.setCurrentIndex(0)
        self.search_methodCB.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.titleLb.setText(_translate("MainWindow", "Welcome to Tangram Puzzle Solver"))
        self.authorLb.setText(_translate("MainWindow", "Presented by wzy"))
        self.game_modeCB.setCurrentText(_translate("MainWindow", "7 elements"))
        self.game_modeCB.setItemText(0, _translate("MainWindow", "7 elements"))
        self.game_modeCB.setItemText(1, _translate("MainWindow", "13 elements"))
        self.game_modeCB.setItemText(2, _translate("MainWindow", "Any input"))
        self.game_modeLb.setText(_translate("MainWindow", "Game Mode:"))
        self.search_methodCB.setCurrentText(_translate("MainWindow", "DFS"))
        self.search_methodCB.setItemText(0, _translate("MainWindow", "DFS"))
        self.search_methodLb.setText(_translate("MainWindow", "Search Method:"))
        self.imageLb.setText(_translate("MainWindow", "Image"))
        self.select_image1Lb.setText(_translate("MainWindow", "Select image:"))
        self.select_image2Lb.setText(_translate("MainWindow", "from database:"))
        self.select_image3Lb.setText(_translate("MainWindow", "load from path:"))
        self.areaLb.setText(_translate("MainWindow", "Tangram areas:"))
        self.load_imageBtn.setText(_translate("MainWindow", "Load"))
        self.solveBtn.setText(_translate("MainWindow", "Solve"))