from PySide6.QtWidgets import QApplication, QTabWidget
from PySide6.QtCore import Qt
from tabsWidget.tabWidgetMD5 import QTabWidgetMD5

class MainApp(QTabWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("MD5 Hash Generator")
        # set size 1227 * 780
        self.resize(1227, 780)
        self.setTabsClosable(True)
        self.setMovable(True)
        # set tab nằm ngnag bên cạnh trái
        # self.setTabBarAutoHide(True)
        # self.setDocumentMode(True)
        # set tab position
        self.setTabPosition(QTabWidget.North)
        # set tab shape
        self.setTabShape(QTabWidget.Rounded)
        # self.setTabPosition(QTabWidget.West)
        # self.setTabShape(QTabWidget.Triangular)

        # Add the QTabWidgetMD5 instance
        self.tab_md5 = QTabWidgetMD5()
        self.addTab(self.tab_md5, "MD5 Hash")

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    main_app = MainApp()
    main_app.show()
    sys.exit(app.exec())
