from settings.SettingsManager import SettingsManager
from ui.components.BasePage import BasePage

class Settings(BasePage):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.settingsManager = SettingsManager()