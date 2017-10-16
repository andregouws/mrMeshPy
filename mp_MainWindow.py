# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mp_MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MrMeshMainWindow(object):
    def setupUi(self, MrMeshMainWindow):
        MrMeshMainWindow.setObjectName("MrMeshMainWindow")
        MrMeshMainWindow.resize(708, 550)
        self.centralwidget = QtWidgets.QWidget(MrMeshMainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setMinimumSize(QtCore.QSize(662, 0))
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setAutoFillBackground(False)
        self.tabWidget.setTabsClosable(True)
        self.tabWidget.setMovable(True)
        self.tabWidget.setObjectName("tabWidget")
        self.horizontalLayout.addWidget(self.tabWidget)
        MrMeshMainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MrMeshMainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 708, 19))
        self.menubar.setObjectName("menubar")
        self.menuMenu = QtWidgets.QMenu(self.menubar)
        self.menuMenu.setObjectName("menuMenu")
        self.menuComing = QtWidgets.QMenu(self.menubar)
        self.menuComing.setObjectName("menuComing")
        self.menuSoon = QtWidgets.QMenu(self.menubar)
        self.menuSoon.setObjectName("menuSoon")
        self.menuROIs = QtWidgets.QMenu(self.menubar)
        self.menuROIs.setObjectName("menuROIs")
        self.menuTesting = QtWidgets.QMenu(self.menubar)
        self.menuTesting.setObjectName("menuTesting")
        MrMeshMainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MrMeshMainWindow)
        self.statusbar.setObjectName("statusbar")
        MrMeshMainWindow.setStatusBar(self.statusbar)
        self.actionSoon = QtWidgets.QAction(MrMeshMainWindow)
        self.actionSoon.setObjectName("actionSoon")
        self.actionEnableDraw = QtWidgets.QAction(MrMeshMainWindow)
        self.actionEnableDraw.setObjectName("actionEnableDraw")
        self.actionDisableDraw = QtWidgets.QAction(MrMeshMainWindow)
        self.actionDisableDraw.setObjectName("actionDisableDraw")
        self.actionCloseAndFill = QtWidgets.QAction(MrMeshMainWindow)
        self.actionCloseAndFill.setObjectName("actionCloseAndFill")
        self.actionSend_10_bytes_TCP = QtWidgets.QAction(MrMeshMainWindow)
        self.actionSend_10_bytes_TCP.setObjectName("actionSend_10_bytes_TCP")
        self.actionStart_New_ROI = QtWidgets.QAction(MrMeshMainWindow)
        self.actionStart_New_ROI.setObjectName("actionStart_New_ROI")
        self.menuComing.addAction(self.actionSoon)
        self.menuROIs.addAction(self.actionEnableDraw)
        self.menuROIs.addAction(self.actionDisableDraw)
        self.menuROIs.addAction(self.actionCloseAndFill)
        self.menuROIs.addSeparator()
        self.menuROIs.addSeparator()
        self.menuROIs.addAction(self.actionStart_New_ROI)
        self.menuTesting.addAction(self.actionSend_10_bytes_TCP)
        self.menubar.addAction(self.menuMenu.menuAction())
        self.menubar.addAction(self.menuComing.menuAction())
        self.menubar.addAction(self.menuSoon.menuAction())
        self.menubar.addAction(self.menuROIs.menuAction())
        self.menubar.addAction(self.menuTesting.menuAction())

        self.retranslateUi(MrMeshMainWindow)
        self.tabWidget.setCurrentIndex(-1)
        QtCore.QMetaObject.connectSlotsByName(MrMeshMainWindow)

    def retranslateUi(self, MrMeshMainWindow):
        _translate = QtCore.QCoreApplication.translate
        MrMeshMainWindow.setWindowTitle(_translate("MrMeshMainWindow", "mrMeshPy v0.1"))
        self.menuMenu.setTitle(_translate("MrMeshMainWindow", "Menu"))
        self.menuComing.setTitle(_translate("MrMeshMainWindow", "Coming"))
        self.menuSoon.setTitle(_translate("MrMeshMainWindow", "Soon"))
        self.menuROIs.setTitle(_translate("MrMeshMainWindow", "ROIs"))
        self.menuTesting.setTitle(_translate("MrMeshMainWindow", "Testing"))
        self.actionSoon.setText(_translate("MrMeshMainWindow", "Soon"))
        self.actionEnableDraw.setText(_translate("MrMeshMainWindow", "Enable drawing"))
        self.actionDisableDraw.setText(_translate("MrMeshMainWindow", "Disable drawing"))
        self.actionCloseAndFill.setText(_translate("MrMeshMainWindow", "Close and Fill"))
        self.actionSend_10_bytes_TCP.setText(_translate("MrMeshMainWindow", "Send 10 bytes TCP"))
        self.actionStart_New_ROI.setText(_translate("MrMeshMainWindow", "Start New ROI"))

