from settings.structs.Setting import Setting

class ArrowSettings(Setting):
    def __init__(self) -> None:
        super().__init__()

        self.json = {
            "color": (0, 0, 0),
            "color_tolerance": (10, 10, 10),
            "position": (0, 0),
            "position_range": (0, 0, 0, 0),
            "key": "",
        }

        self.settings_name = "ArrowSettings"
    
    @property
    def color(self) -> tuple:
        return self.json["color"]

    @color.setter
    def color(self, value: tuple) -> None:
        self.json["color"] = value
    
    @property
    def color_tolerance(self) -> tuple:
        return self.json["color_tolerance"]
    
    @color_tolerance.setter
    def color_tolerance(self, value: tuple) -> None:
        self.json["color_tolerance"] = value
    
    @property
    def position(self) -> tuple:
        return self.json["position"]
    
    @position.setter
    def position(self, value: tuple) -> None:
        self.json["position"] = value
    
    @property
    def position_range(self) -> tuple:
        return self.json["position_range"]
    
    @position_range.setter
    def position_range(self, value: tuple) -> None:
        self.json["position_range"] = value

    @property
    def key(self) -> str:
        return self.json["key"]
    
    @key.setter
    def key(self, value: str) -> None:
        self.json["key"] = value