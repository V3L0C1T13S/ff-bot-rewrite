from PyQt6.QtCore import *
from PyQt6.QtWidgets import *

class ArrowStatus(QLabel):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setText("")
        self.setAlignment(Qt.AlignCenter)