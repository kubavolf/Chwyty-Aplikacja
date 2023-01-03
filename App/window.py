import sys
import time
from PyQt6.QtWidgets import QPushButton, QLabel, QMainWindow, QSlider
from PyQt6.QtGui import QIcon, QPixmap
from PyQt6.QtMultimedia import QSoundEffect
from PyQt6.QtCore import QUrl, Qt

import signal
import threading

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Chords App")
        self.setWindowIcon(QIcon("icon.png"))
        self.setFixedHeight(600)
        self.setFixedWidth(800)
        self.setStyleSheet("background-image:url(background.png); background-attachment: fixed")
        self.pixmap_logo = QPixmap("logo.png")


    def create_logo(self):
        logo = QLabel(self)
        logo.setPixmap(self.pixmap_logo)
        logo.resize(250, 130)
        logo.setScaledContents(True)
        logo.move(280, 25)


def sound_button_click(sound):
    filename = sound
    global effect
    effect = QSoundEffect()
    effect.setSource(QUrl.fromLocalFile(filename))
    effect.setVolume(0.5)
    # possible bug: QSoundEffect::Infinite cannot be used in setLoopCount
    effect.setLoopCount(1)
    effect.play()
    print("clicked")

def metronome_button_click(sound):

    filename = sound
    global effect
    effect = QSoundEffect()
    effect.setSource(QUrl.fromLocalFile(filename))
    effect.setVolume(0.5)
        # possible bug: QSoundEffect::Infinite cannot be used in setLoopCount
    effect.setLoopCount(1)
    effect.play()
    print("clicked")

exit_event = threading.Event()



def metro_loop(sound, BPM):
    exit_event.clear()
    while True:
        time.sleep(BPM)
        metronome_button_click(sound)

        if exit_event.is_set():
            break


def signal_handler(signum, frame):
    exit_event.set()


signal.signal(signal.SIGINT, signal_handler)




class ChordsWindow(QMainWindow):
    def __init__(self, variant):
        super().__init__()
        self.setWindowTitle(variant)
        self.setWindowIcon(QIcon("icon.png"))
        self.setFixedHeight(600)
        self.setFixedWidth(800)
        self.setStyleSheet("background-image:url(new_background2.png); background-attachment: fixed")

    def create_sound_button(self, image, x_cor, y_cor, wg, hg, sound):

        button = QPushButton(self)
        button.setStyleSheet(image)
        button.setGeometry(x_cor, y_cor, wg, hg)
        button.clicked.connect(lambda: sound_button_click(sound))


    def create_metronome_button(self, image, x_cor, y_cor, wg, hg, sound, BPM):

        button = QPushButton(self)
        button.setStyleSheet(image)
        button.setGeometry(x_cor, y_cor, wg, hg)
        th = threading.Thread(target=metro_loop, args=[sound, BPM])
        button.clicked.connect(lambda: th.start())

    def create_metronome_stop_button(self, image, x_cor, y_cor, wg, hg, sound, BPM):

        button = QPushButton(self)
        button.setStyleSheet(image)
        button.setGeometry(x_cor, y_cor, wg, hg)
        button.clicked.connect(lambda: signal_handler())

    def create_slider(self):
        slider = QSlider(self)
        #slider.setOrientation()
        slider.setMinimum(10)
        slider.setMaximum(50)
        slider.setGeometry(430, 200, 200, 50)
