from PyQt6.QtWidgets import *

class Console(QTextEdit):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.logs = []
        
        self.setReadOnly(True)
    
    def print(self, text: str):
        self.logs.append(text)
        print(text)
        self.append(text)

    def info(self, text: str):
        self.print("[INFO] " + text)
    
    def error(self, text: str):
        self.print("[ERROR] " + text)
    
    def warn(self, text: str):
        self.print("[WARNING] " + text)