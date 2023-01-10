from PyQt6.QtWidgets import QPushButton, QLabel, QMainWindow
from PyQt6.QtGui import QIcon, QPixmap
from PyQt6.QtMultimedia import QSoundEffect
from PyQt6.QtCore import QUrl


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



