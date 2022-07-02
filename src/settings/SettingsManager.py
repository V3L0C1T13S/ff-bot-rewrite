class SettingsManager():
    def __init__(self):
        self.settings = {
            "bot_settings": {
                "arrow_count": 0,
            },
        }
        self.settings_file = "settings.json"
