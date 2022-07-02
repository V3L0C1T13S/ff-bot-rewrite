from PyQt6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QHBoxLayout,

)

class BasePage(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.pagelayout = QVBoxLayout()
        self.horizontal_layout = QHBoxLayout()

        self.pagelayout.addLayout(self.horizontal_layout)

        self.setLayout(self.pagelayout)