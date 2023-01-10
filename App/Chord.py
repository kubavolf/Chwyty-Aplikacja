from PyQt6.QtGui import QFont, QIcon
from PyQt6.QtCore import QTimer
from PyQt6.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QSlider, QPushButton, QLabel
import winsound
from window import ChordsWindow


class Chord:

    def __init__(self, variant, x_cor, y_cor, wg, hg, image_7, image_dur, image_mol, sound_7, sound_dur, sound_mol):
        self.variant = variant
        self.x_cor = x_cor
        self.y_cor = y_cor
        self.wg = wg
        self.hg = hg
        self.new_window = ChordsWindow(self.variant)
        self.image_7 = image_7
        self.image_dur = image_dur
        self.image_mol = image_mol
        self.sound_7 = sound_7
        self.sound_dur = sound_dur
        self.sound_mol = sound_mol

    def create_button(self, window):
        button = QPushButton(self.variant, window)
        button.setFont(QFont("Times", 15))
        button.setGeometry(self.x_cor, self.y_cor, self.wg, self.hg)
        button.setStyleSheet("color: rgb(255, 255, 255)")
        button.clicked.connect(self.on_click)

    def create_new_window(self):
        self.new_window.create_sound_button(self.image_7, x_cor=60, y_cor=100, wg=285, hg=197, sound=self.sound_7)
        self.new_window.create_sound_button(self.image_dur, x_cor=440, y_cor=100, wg=285, hg=197, sound=self.sound_dur)
        self.new_window.create_sound_button(self.image_mol, x_cor=250, y_cor=350, wg=285, hg=197, sound=self.sound_mol)

    def on_click(self):
        self.new_window.show()


class Tuner:
    def __init__(self, variant, x_cor, y_cor, wg, hg, image_e6, image_a, image_d, image_g, image_b, image_e1, sound_e6, sound_a, sound_d, sound_g, sound_b, sound_e1):
        self.variant = variant
        self.x_cor = x_cor
        self.y_cor = y_cor
        self.wg = wg
        self.hg = hg
        self.new_window = ChordsWindow(self.variant)
        self.image_e6 = image_e6
        self.image_a = image_a
        self.image_d = image_d
        self.image_g = image_g
        self.image_b = image_b
        self.image_e1 = image_e1
        self.sound_e6 = sound_e6
        self.sound_a = sound_a
        self.sound_d = sound_d
        self.sound_g = sound_g
        self.sound_b = sound_b
        self.sound_e1 = sound_e1

    def create_button(self, window):
        button = QPushButton(self.variant, window)
        button.setFont(QFont("Times", 15))
        button.setGeometry(self.x_cor, self.y_cor, self.wg, self.hg)
        button.setStyleSheet("color: rgb(255, 255, 255)")
        button.clicked.connect(self.on_click)

    def create_new_window(self):
        self.new_window.create_sound_button(self.image_e6, x_cor=40, y_cor=150, wg=150, hg=100, sound=self.sound_e6)
        self.new_window.create_sound_button(self.image_a, x_cor=230, y_cor=150, wg=150, hg=100, sound=self.sound_a)
        self.new_window.create_sound_button(self.image_d, x_cor=420, y_cor=150, wg=150, hg=100, sound=self.sound_d)
        self.new_window.create_sound_button(self.image_g, x_cor=610, y_cor=150, wg=150, hg=100, sound=self.sound_g)
        self.new_window.create_sound_button(self.image_b, x_cor=230, y_cor=350, wg=150, hg=100, sound=self.sound_b)
        self.new_window.create_sound_button(self.image_e1, x_cor=420, y_cor=350, wg=150, hg=100, sound=self.sound_e1)

    def on_click(self):
        self.new_window.show()


class Metronome(QWidget):
    def __init__(self, variant, x_cor, y_cor, wg, hg, image_7, sound_7):
        super().__init__()
        self.variant = variant
        self.x_cor = x_cor
        self.y_cor = y_cor
        self.wg = wg
        self.hg = hg
        self.image_7 = image_7
        self.sound_7 = sound_7
        self.tempo = 120
        self.is_running = False
        self.setWindowIcon(QIcon("metro_icon2.png"))
        # timer i ustawienie sygnału timeout na funkcje tick()
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.tick)

        # widgets
        self.tempo_slider = QSlider()  # Qt.Horizontal
        self.tempo_slider.setMinimum(40)
        self.tempo_slider.setMaximum(220)
        self.tempo_slider.setValue(self.tempo)
        self.tempo_slider.valueChanged.connect(self.set_tempo)

        self.start_stop_button = QPushButton("Start")
        self.start_stop_button.setFixedWidth(160)
        self.start_stop_button.setFixedHeight(40)
        self.start_stop_button.clicked.connect(self.start_stop)

        self.tempo_label = QLabel(str(self.tempo))
        self.tempo_label.setFont(QFont('Arial', 15))
        self.tempo_label.setStyleSheet("background-color: rgba(0, 255, 255, 90)")

        # layouts
        hbox = QHBoxLayout()
        hbox.addWidget(self.start_stop_button)
        hbox.addWidget(self.tempo_slider)

        vbox = QVBoxLayout()
        vbox.addLayout(hbox)
        vbox.addWidget(self.tempo_label)

        self.setGeometry(820, 300, 300, 150)
        self.setLayout(vbox)
        self.setWindowTitle("Metronome")

    def start_stop(self):
        if self.is_running:
            self.timer.stop()
            self.is_running = False
            self.start_stop_button.setText("Start")
        else:
            self.timer.start(round(60000 / self.tempo))
            self.is_running = True
            self.start_stop_button.setText("Stop")

    def set_tempo(self, tempo):
        self.tempo = tempo
        self.tempo_label.setText(str(tempo))
        if self.is_running:
            self.start_stop()
            self.start_stop()

    def tick(self):
        winsound.Beep(1000, 200)

    def create_button(self, window):
        button = QPushButton(self.variant, window)
        button.setFont(QFont("Times", 15))
        button.setGeometry(self.x_cor, self.y_cor, self.wg, self.hg)
        button.setStyleSheet("color: rgb(255, 255, 255)")
        button.clicked.connect(self.on_click)

    def on_click(self):
        self.show()
