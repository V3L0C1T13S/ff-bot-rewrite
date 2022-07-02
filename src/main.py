from PyQt6.QtWidgets import (
    QApplication,
)

from ui.MainWindow import MainWindow

app = QApplication([])
window = MainWindow()
window.show()
app.exec()
