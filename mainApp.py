from PySide6.QtWidgets import QApplication, QTabWidget, QMainWindow
from PySide6.QtCore import QSize
from PySide6.QtGui import QIcon
from tabsWidget.tabWidgetMD5 import QTabWidgetMD5
from tabsWidget.tabWidgetSHA1 import QTabWidgetSHA1
from mainUI import Ui_MainWindow

class MainApp(Ui_MainWindow, QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("App cryptool")
        icon = QIcon()
        icon.addFile(u":/icons/iconsDark/iconApp.png", QSize(100, 100), QIcon.Mode.Normal, QIcon.State.Off)
        self.setWindowIcon(icon)
        self.resize(1182, 780)
        self.actionMD5.triggered.connect(lambda: self.add_tabs_algorithms("MD5"))
        self.actionSHA_1.triggered.connect(lambda: self.add_tabs_algorithms("SHA1"))

    def add_tabs_algorithms(self, name_tab):
        self.tabWidget.setTabPosition(QTabWidget.TabPosition.North)
        self.tabWidget.setTabsClosable(True)
        self.tabWidget.setMovable(True)
        self.tabWidget.setTabShape(QTabWidget.TabShape.Triangular)

        # Create a new tab for MD5
        if name_tab == "MD5":
            self.tabWidget.addTab(QTabWidgetMD5(), name_tab)
            self.tabWidget.setTabText(self.tabWidget.indexOf(QTabWidgetMD5()), name_tab)
        elif name_tab == "SHA1":
            self.tabWidget.addTab(QTabWidgetSHA1(), name_tab)
            self.tabWidget.setTabText(self.tabWidget.indexOf(QTabWidgetSHA1()), name_tab)

        # Connect the tab close event to a method
        self.tabWidget.tabCloseRequested.connect(self.close_tab)

    def close_tab(self, index):
        if index >= 0:
            self.tabWidget.removeTab(index)
            self.tabWidget.setCurrentIndex(index - 1 if index > 0 else 0)



if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    main_app = MainApp()
    main_app.show()
    sys.exit(app.exec())
