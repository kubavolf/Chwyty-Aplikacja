import sys

from PyQt6.QtWidgets import QPushButton, QLabel, QMainWindow, QWidget, QApplication
from PyQt6.QtGui import QIcon, QPixmap, QFont, QGuiApplication
from PyQt6.QtMultimedia import QMediaPlayer, QAudioOutput, QSoundEffect
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
        self.new_window_c = NewWindow()
        self.new_window_d = NewWindow()
        self.new_window_e = NewWindow()
        self.new_window_f = NewWindow()
        self.new_window_g = NewWindow()
        self.new_window_a = NewWindow()
        self.new_window_b = NewWindow()
        self.new_window_cis = NewWindow()
        self.new_window_dis = NewWindow()
        self.new_window_fis = NewWindow()
        self.new_window_gis = NewWindow()
        self.new_window_h = NewWindow()


    def create_main_button(self, name, x_cor, y_cor, wg, hg):
        button = QPushButton(name, self)
        button.setFont(QFont("Times", 15))
        button.setGeometry(x_cor, y_cor, wg, hg)
        button.setStyleSheet("color: rgb(255, 255, 255)")  #"border-image:url(c_chord_image.png)")
        if name == "C_chords":
            button.clicked.connect(self.c_button_click)
        elif name == "D_chords":
            button.clicked.connect(self.d_button_click)
        elif name == "E_chords":
            button.clicked.connect(self.e_button_click)
        elif name == "F_chords":
            button.clicked.connect(self.f_button_click)
        elif name == "G_chords":
            button.clicked.connect(self.g_button_click)
        elif name == "A_chords":
            button.clicked.connect(self.a_button_click)
        elif name == "B_chords":
            button.clicked.connect(self.b_button_click)
        elif name == "Cis_chords":
            button.clicked.connect(self.cis_button_click)
        elif name == "Dis_chords":
            button.clicked.connect(self.dis_button_click)
        elif name == "Fis_chords":
            button.clicked.connect(self.fis_button_click)
        elif name == "Gis_chords":
            button.clicked.connect(self.gis_button_click)
        elif name == "H_chords":
            button.clicked.connect(self.h_button_click)

    def c_button_click(self):
        self.new_window_c.show()

    def d_button_click(self):
        self.new_window_d.show()

    def e_button_click(self):
        self.new_window_e.show()

    def f_button_click(self):
        self.new_window_f.show()

    def g_button_click(self):
        self.new_window_g.show()

    def a_button_click(self):
        self.new_window_a.show()

    def b_button_click(self):
        self.new_window_b.show()

    def cis_button_click(self):
        self.new_window_cis.show()

    def dis_button_click(self):
        self.new_window_dis.show()

    def fis_button_click(self):
        self.new_window_fis.show()

    def gis_button_click(self):
        self.new_window_gis.show()

    def h_button_click(self):
        self.new_window_h.show()



    def create_logo(self):
        logo = QLabel(self)
        logo.setPixmap(self.pixmap_logo)
        logo.resize(250, 130)
        logo.setScaledContents(True)
        logo.move(280, 25)


def sound_button_click():
    filename = "rocket.wav"
    effect = QSoundEffect()
    effect.setSource(QUrl.fromLocalFile(filename))
    effect.setVolume(0.5)
    # possible bug: QSoundEffect::Infinite cannot be used in setLoopCount
    effect.setLoopCount(1)
    effect.play()
    print("clicked")


class NewWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Chords")
        self.setWindowIcon(QIcon("icon.png"))
        self.setFixedHeight(600)
        self.setFixedWidth(800)
        self.setStyleSheet("background-image:url(new_background2.png); background-attachment: fixed")

    def create_sound_button(self, image, x_cor, y_cor, wg, hg):

        button = QPushButton(self)
        button.setStyleSheet(image)
        button.setGeometry(x_cor, y_cor, wg, hg)
        button.clicked.connect(sound_button_click)
