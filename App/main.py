import ast

from window import Window
import sys
from PyQt6.QtWidgets import QApplication

from Chord import Chord, Tuner, Metronome



app = QApplication(sys.argv)

window = Window()

akord_list = []

with open("akord_base.txt") as f:
    data = f.read()

akord_dict = ast.literal_eval(data)

for akord in akord_dict:
    akord = Chord(variant=akord_dict[akord]["variant"], x_cor=akord_dict[akord]["x_cor"], y_cor=akord_dict[akord]["y_cor"], wg=akord_dict[akord]["wg"], hg=akord_dict[akord]["hg"],
                  image_7=akord_dict[akord]["image_7"], image_dur=akord_dict[akord]["image_dur"], image_mol=akord_dict[akord]["image_mol"],
                  sound_7=akord_dict[akord]["sound_7"], sound_dur=akord_dict[akord]["sound_dur"], sound_mol=akord_dict[akord]["sound_mol"])
    akord_list.append(akord)


for akord in akord_list:
    akord.create_new_window()
    akord.create_button(window)

tuner = Tuner(variant="Tuner", x_cor=600, y_cor=100, wg=150, hg=150,
                image_e6="border-image:url(C-7.png)", image_a="border-image:url(C-dur.png)", image_d="border-image:url(C-mol.png)",
                image_g="border-image:url(C-mol.png)", image_b="border-image:url(C-mol.png)", image_e1="border-image:url(C-mol.png)",
                sound_e6="Sounds/E6.wav", sound_a="Sounds/A.wav", sound_d="Sounds/D.wav", sound_g="Sounds/G.wav",
                sound_b="Sounds/B.wav", sound_e1="Sounds/E1.wav")

metronome = Metronome(variant="Metronome", x_cor=60, y_cor=100, wg=150, hg=150, image_7="border-image:url(C-7.png)", sound_7="Sounds/metron_tick.wav", BPM=0.5)


tuner.create_button(window)
tuner.create_new_window()
metronome.create_button(window)
metronome.create_new_window()

#metronome.create_slider(window)

window.create_logo()



#if __name__ = "__main__":
window.show()

sys.exit(app.exec())
