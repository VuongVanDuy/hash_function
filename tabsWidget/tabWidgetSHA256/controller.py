from PySide6.QtWidgets import QWidget
from PySide6.QtCore import Qt
from .form import Ui_Form
from tabsWidget.config import get_instruction_algorithm, SHA256_INSTRUCTION
from tabsWidget.customWidget.customDialog import QCustomDialog
from hash.sha256 import SHA256

# 1) Lớp container kế thừa QWidget + Ui_Form
class FormContainer(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("SHA256 Widget")
        self.btnChooseFile.setEnabled(self.File.isChecked())
        self.instruction.setText(
            get_instruction_algorithm(file_name=SHA256_INSTRUCTION)
        )
        self.timer = None
        self.md5Control = None

        self.zoom_3.clicked.connect(self.show_zoom_instruction)


    def show_zoom_instruction(self):
        content = self.instruction.toPlainText()
        customDialog = QCustomDialog(content=content, title="Instruction algorithm md5")
        customDialog.exec_()

