from util.keyboardUtils import pressKey
import time

class Arrow():
    def __init__(self, color, position, key, color_tolerance = (10, 10, 10)):
        self.color = color
        self.color_tolerance = color_tolerance
        self.position = position
        self.position_range = (
            position[0] - 1,
            position[1] - 1,
            position[0] + 1,
            position[1] + 1
        )
        self.key = key
    
    # Compares a pixel color with the arrow color in the tolerance range.
    # Returns True if the color is within the tolerance range.
    def _color_is_within_tolerance(self, pixel) -> bool:
        return (
            abs(pixel[0] - self.color[0]) <= self.color_tolerance[0] and
            abs(pixel[1] - self.color[1]) <= self.color_tolerance[1] and
            abs(pixel[2] - self.color[2]) <= self.color_tolerance[2]
        )

    # A function to compare the color of the pixel within the position range
    # on a screen with the color of the arrow we are looking for.
    # Returns True if the color of the pixel is within the tolerance of the arrow color.
    def compare_pixels(self, Screen) -> bool:
        pixel = Screen.getpixel(self.position)
        return self._color_is_within_tolerance(pixel)
    
    def _press_key(self):
        pressKey(self.key)

    def do_compare(self, Screen) -> bool:
        if (self.compare_pixels(Screen)):
            self._press_key()
            return True
        return False