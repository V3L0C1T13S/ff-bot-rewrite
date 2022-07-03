import json
import os


class Setting():
    def __init__(self) -> None:
        self.json = {}

        self.settings_name = ""

    def load(self) -> None:
        if os.path.exists(self.file_path):
            with open(self.file_path, "r") as f:
                self.json = json.load(f)
        else:
            self.save()
        
    def save(self) -> None:
        with open(self.file_path, "w") as f:
            json.dump(self.json, f, indent=4)