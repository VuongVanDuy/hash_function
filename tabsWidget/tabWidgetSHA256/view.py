from PySide6.QtWidgets import QApplication, QWidget, QGraphicsView, QGraphicsScene, QVBoxLayout
from PySide6.QtCore import Qt
from .controller import ContainerControl

class QTabWidgetSHA256(QWidget):
    def __init__(self):
        super().__init__()

        # Tạo form và scene
        self.form = ContainerControl()
        self.scene = QGraphicsScene(self)
        self.proxy = self.scene.addWidget(self.form)

        # Tạo view để show scene
        self.view = QGraphicsView(self.scene, self)
        self.view.setAlignment(Qt.AlignCenter)

        # Layout: chỉ chứa mỗi view
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(self.view)

    def showEvent(self, event):
        super().showEvent(event)
        # Lúc view đã có size thật, gọi fitInView 1 lần
        rect = self.proxy.boundingRect()
        self.view.setSceneRect(rect)
        self.view.fitInView(rect, Qt.IgnoreAspectRatio)

    def resizeEvent(self, event):
        super().resizeEvent(event)
        # Cứ resize lại là scale tiếp
        if not self.isActiveWindow():
            return

        rect = self.proxy.boundingRect()
        self.view.fitInView(rect, Qt.IgnoreAspectRatio)


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    w = QTabWidgetSHA256()
    # Đặt kích thước khởi tạo (theo đúng bản design)
    w.resize(1488, 748)
    w.show()
    sys.exit(app.exec())