from window import ChordsWindow
from PyQt6.QtWidgets import QPushButton
from PyQt6.QtGui import QFont


class Chord:

    def __init__(self, variant, x_cor, y_cor, wg, hg, image_7, image_dur, image_mol, sound_7, sound_dur, sound_mol):
        self.variant = variant
        self.x_cor = x_cor
        self.y_cor = y_cor
        self.wg = wg
        self.hg = hg
        self.new_window = ChordsWindow()
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
