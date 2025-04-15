from PySide6.QtWidgets import QDialog, QVBoxLayout, QLabel, QScrollArea
from PySide6.QtCore import QSize, Qt
from PySide6.QtGui import QIcon

class QCustomDialog(QDialog):
    def __init__(self, content, title="Detailed content", parent=None):
        super().__init__(parent)
        self.setWindowTitle(title)
        icon = QIcon()
        icon.addFile(u":/icons/iconsDark/detail_content.png", QSize(100, 100), QIcon.Mode.Normal, QIcon.State.Off)
        self.setWindowIcon(icon)

        layout = QVBoxLayout(self)

        # Tạo một QLabel để hiển thị nội dung và đặt cho phép xuống dòng
        label = QLabel(content, self)
        label.setWordWrap(True)

        # Tạo QScrollArea và gán QLabel vào bên trong nó
        scroll_area = QScrollArea(self)
        scroll_area.setWidgetResizable(True)
        scroll_area.setWidget(label)
        label.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignTop)

        # Thêm QScrollArea vào layout của dialog
        layout.addWidget(scroll_area)
        # set size for dialog
        self.setMinimumSize(400, 500)

    # tạo một phương thức xóa dialog khi nó được đóng
    def closeEvent(self, event):
        self.deleteLater()
        event.accept()
