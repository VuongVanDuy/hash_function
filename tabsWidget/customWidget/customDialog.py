from time import sleep

from PySide6.QtWidgets import QDialog, QVBoxLayout, QLabel, QScrollArea, QPushButton
from PySide6.QtCore import QSize, Qt
from PySide6.QtGui import QIcon
from common.common import hex_to_str, str_to_hex

class QCustomDialog(QDialog):
    def __init__(self, content, title="Detailed content", type=None, parent=None):
        super().__init__(parent)
        self.setWindowTitle(title)
        icon = QIcon()
        icon.addFile(u":/icons/iconsDark/detail_content.png", QSize(100, 100), QIcon.Mode.Normal, QIcon.State.Off)
        self.setWindowIcon(icon)

        layout = QVBoxLayout(self)

        # Tạo một QLabel để hiển thị nội dung và đặt cho phép xuống dòng
        self.label = QLabel(content, self)
        self.label.setWordWrap(True)

        if type == "Plaintext":
            content_list = content.split(" ")
            if all(len(i) == 2 and all(c in "0123456789ABCDEF" for c in i) for i in content_list):
                # nội dung là dạng hex string
                self.button = QPushButton("Text format", self)
                self.button.clicked.connect(self.clicked_button)
            else:
                # nội dung là dạng text string
                self.button = QPushButton("Hex format", self)
                self.button.clicked.connect(self.clicked_button)

        if hasattr(self, 'button') and isinstance(self.button, QPushButton):
            layout.addWidget(self.button)
        # Tạo QScrollArea và gán QLabel vào bên trong nó
        scroll_area = QScrollArea(self)
        scroll_area.setWidgetResizable(True)
        scroll_area.setWidget(self.label)
        self.label.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignTop)

        # Thêm QScrollArea vào layout của dialog
        layout.addWidget(scroll_area)
        # set size for dialog
        self.setMinimumSize(400, 500)

    def clicked_button(self):
        # kiểm tra nội dung dạng text string hay hex string (ví dụ: A5 BD 4D 2A 3F)
        # lấy name của button
        content = self.label.text()
        name_button = self.button.text()
        if name_button == "Hex format":
            content_hex = str_to_hex(content)
            self.label.setText(content_hex)
            self.button.setText("Text format")
        elif name_button == "Text format":
            content_str = hex_to_str(content)
            self.label.setText(content_str)
            self.button.setText("Hex format")

    # tạo một phương thức xóa dialog khi nó được đóng
    def closeEvent(self, event):
        self.deleteLater()
        event.accept()
