# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainUI.ui'
##
## Created by: Qt User Interface Compiler version 6.9.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QMainWindow, QMenu,
    QMenuBar, QSizePolicy, QStatusBar, QTabWidget,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(954, 728)
        self.actionMD5 = QAction(MainWindow)
        self.actionMD5.setObjectName(u"actionMD5")
        self.actionMD5.setMenuRole(QAction.MenuRole.NoRole)
        self.actionSHA_1 = QAction(MainWindow)
        self.actionSHA_1.setObjectName(u"actionSHA_1")
        self.actionSHA_1.setMenuRole(QAction.MenuRole.NoRole)
        self.actionSHA_256 = QAction(MainWindow)
        self.actionSHA_256.setObjectName(u"actionSHA_256")
        self.actionSHA_256.setMenuRole(QAction.MenuRole.NoRole)
        self.actionLanguages = QAction(MainWindow)
        self.actionLanguages.setObjectName(u"actionLanguages")
        self.actionLanguages.setMenuRole(QAction.MenuRole.NoRole)
        self.actionFuntions_of_keys = QAction(MainWindow)
        self.actionFuntions_of_keys.setObjectName(u"actionFuntions_of_keys")
        self.actionFuntions_of_keys.setMenuRole(QAction.MenuRole.NoRole)
        self.actionAbout_algorithms = QAction(MainWindow)
        self.actionAbout_algorithms.setObjectName(u"actionAbout_algorithms")
        self.actionAbout_algorithms.setMenuRole(QAction.MenuRole.NoRole)
        self.actionAbout_authors = QAction(MainWindow)
        self.actionAbout_authors.setObjectName(u"actionAbout_authors")
        self.actionAbout_authors.setMenuRole(QAction.MenuRole.NoRole)
        self.actionModes = QAction(MainWindow)
        self.actionModes.setObjectName(u"actionModes")
        self.actionModes.setMenuRole(QAction.MenuRole.NoRole)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setTabShape(QTabWidget.TabShape.Rounded)

        self.verticalLayout.addWidget(self.tabWidget)


        self.horizontalLayout.addLayout(self.verticalLayout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 954, 33))
        self.menuAlgorithms = QMenu(self.menubar)
        self.menuAlgorithms.setObjectName(u"menuAlgorithms")
        self.menuSettings = QMenu(self.menubar)
        self.menuSettings.setObjectName(u"menuSettings")
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName(u"menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuAlgorithms.menuAction())
        self.menubar.addAction(self.menuSettings.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menuAlgorithms.addAction(self.actionMD5)
        self.menuAlgorithms.addAction(self.actionSHA_1)
        self.menuAlgorithms.addAction(self.actionSHA_256)
        self.menuSettings.addAction(self.actionLanguages)
        self.menuSettings.addAction(self.actionModes)
        self.menuHelp.addAction(self.actionFuntions_of_keys)
        self.menuHelp.addAction(self.actionAbout_algorithms)
        self.menuHelp.addAction(self.actionAbout_authors)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(-1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionMD5.setText(QCoreApplication.translate("MainWindow", u"MD5", None))
        self.actionSHA_1.setText(QCoreApplication.translate("MainWindow", u"SHA-1", None))
        self.actionSHA_256.setText(QCoreApplication.translate("MainWindow", u"SHA-256", None))
        self.actionLanguages.setText(QCoreApplication.translate("MainWindow", u"Languages", None))
        self.actionFuntions_of_keys.setText(QCoreApplication.translate("MainWindow", u"Funtions of keys", None))
        self.actionAbout_algorithms.setText(QCoreApplication.translate("MainWindow", u"About algorithms", None))
        self.actionAbout_authors.setText(QCoreApplication.translate("MainWindow", u"About authors", None))
        self.actionModes.setText(QCoreApplication.translate("MainWindow", u"Modes", None))
        self.menuAlgorithms.setTitle(QCoreApplication.translate("MainWindow", u"Algorithms", None))
        self.menuSettings.setTitle(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.menuHelp.setTitle(QCoreApplication.translate("MainWindow", u"Help", None))
    # retranslateUi

