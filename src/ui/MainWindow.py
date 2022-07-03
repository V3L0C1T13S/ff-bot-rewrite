from typing import List
from PIL import ImageGrab
import pyautogui
from PyQt6.QtWidgets import (
    QMainWindow,
    QTabWidget,
)
from PyQt6.QtCore import (
    QThreadPool,
    QRunnable,
    pyqtSlot,
)
import os
import threading
from Common.Arrow import Arrow
from ui.tabs.ManagementPage import ManagementPage
from ui.tabs.Settings import Settings

size = pyautogui.size()

x1 = size[0]/2+210; y1=size[1]/2-650
x2 = x1+790; y2=y1+240

class FrameCaptureWorker(QRunnable):
    def __init__(self):
        super().__init__()

        self.running = False

        self.arrows: List[Arrow] = []

        ArrowLeft = Arrow((194, 75, 153), (65, 120), "a")
        ArrowDown = Arrow((0, 255, 255), (283, 125), "s")
        ArrowUp = Arrow((18, 250, 5), (502, 140), "w")
        ArrowRight = Arrow((249, 57, 63), (723, 120), "d")

        self.arrows.append(ArrowLeft)
        self.arrows.append(ArrowDown)
        self.arrows.append(ArrowUp)
        self.arrows.append(ArrowRight)

    @pyqtSlot()
    def run(self):
        print("[INFO] Starting frame capture thread")
        while self.running:
            Screen = ImageGrab.grab(bbox = (x1, y1, x2, y2))

            for arrow in self.arrows:
                arrow.do_compare(Screen)
        
        print("[INFO] Stopping frame capture thread")

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.running = False
        self.frame_capture_worker = FrameCaptureWorker()
        self.threadpool = QThreadPool()

        self.setWindowTitle("FNF Bot")

        tabs = QTabWidget()
        tabs.setTabPosition(QTabWidget.TabPosition.North)
        tabs.setMovable(True)

        self.management_page = ManagementPage()
        self.startbtn = self.management_page.management_buttons.start_button
        self.startbtn.clicked.connect(self.button_clicked)

        self.settings_page = Settings()

        self.console = self.management_page.console

        tabs.addTab(self.management_page, "Management")
        tabs.addTab(self.settings_page, "Settings")

        self.setCentralWidget(tabs)

        self.console.info("running on host: " + os.name)
        self.console.info("multithreading with max %d threads" % self.threadpool.maxThreadCount())

    def start(self):
        self.console.info("starting bot")
        self.running = True
        self.startbtn.setText("Stop")
        self.frame_capture_worker.running = True
        self.threadpool.start(self.frame_capture_worker)

    def stop(self):
        self.console.info("stopping bot")
        self.frame_capture_worker.running = False
        self.threadpool.waitForDone()
        self.console.info("bot stopped")
        self.frame_capture_worker = FrameCaptureWorker()
        self.startbtn.setText("Start")
        self.running = False


    def button_clicked(self):
        if self.running:
            self.stop()
        else:
            self.start()