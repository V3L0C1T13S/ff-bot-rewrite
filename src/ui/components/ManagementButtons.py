from PyQt6.QtWidgets import *

class ManagementButtons(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.layout = QHBoxLayout()

        self.start_button = QPushButton("Start")

        self.layout.addWidget(self.start_button)

        self.setLayout(self.layout)