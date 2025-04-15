from PySide6.QtWidgets import QApplication, QFileDialog, QPushButton, QWidget, QGroupBox
from PySide6.QtCore import QTimer, QSize, QEventLoop
from PySide6.QtGui import QIcon
from .view import Ui_Form
from tabsWidget.config import StateWidget, get_instruction_algorithm, SHA1_INSTRUCTION
from tabsWidget.customWidget.customDialog import QCustomDialog
from hash.sha1 import SHA1

class QTabWidgetSHA1(Ui_Form, QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Main Window")
        self.md5Control = None
        self.btnChooseFile.setEnabled(self.File.isChecked())
        self.timer = None
        self.instruction.setText(get_instruction_algorithm(file_name=SHA1_INSTRUCTION))

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    main_app = QTabWidgetSHA1()
    main_app.show()
    sys.exit(app.exec())