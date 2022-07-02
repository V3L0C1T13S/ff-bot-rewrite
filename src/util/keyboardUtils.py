import pyautogui
import keyboard
import os

def pressKey(key: str):
    if os.name == "nt":
        # for some reason, pyautogui.press doesn't work on Windows
        # (it works on Mac, Linux, and the BSDs though)
        keyboard.press_and_release(key)
    else:
        pyautogui.press(key)