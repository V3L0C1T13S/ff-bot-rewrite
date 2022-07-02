import os


class SettingsManager():
    def __init__(self):
        self.settings = {
            "bot_settings": {
                "arrow_count": 0,
            },
        }
        # Create data dir if it doesn't exist
        if not os.path.exists("./data"):
            os.makedirs("./data")
