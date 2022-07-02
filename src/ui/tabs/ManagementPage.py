from PyQt6.QtWidgets import (
    QVBoxLayout,
)

from ui.Console import Console
from ui.components.BasePage import BasePage
from ui.components.ManagementButtons import ManagementButtons

class ManagementPage(BasePage):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.bottom_layout = QVBoxLayout()

        self.console = Console()
        self.management_buttons = ManagementButtons()

        self.horizontal_layout.addWidget(self.console)
        self.bottom_layout.addWidget(self.management_buttons)

        self.pagelayout.addLayout(self.horizontal_layout)
        self.pagelayout.addLayout(self.bottom_layout)

        self.setLayout(self.pagelayout)