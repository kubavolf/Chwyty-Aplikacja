from window import Window
import sys
from PyQt6.QtWidgets import QApplication
from Chord import Chord

app = QApplication(sys.argv)

window = Window()


akord_c = Chord(variant="C_chords", x_cor=60, y_cor=100, wg=150, hg=50,
                image_7="border-image:url(C-7.png)", image_dur="border-image:url(C-dur.png)", image_mol="border-image:url(C-mol.png)",
                sound_7="rocket.wav", sound_dur="rocket.wav", sound_mol="rocket.wav")

akord_d = Chord(variant="D_chords", x_cor=240, y_cor=300, wg=150, hg=50,
                image_7="border-image:url(D-7.png)", image_dur="border-image:url(D-dur.png)", image_mol="border-image:url(D-mol.png)",
                sound_7="rocket.wav", sound_dur="rocket.wav", sound_mol="rocket.wav")

akord_e = Chord(variant="E_chords", x_cor=420, y_cor=300, wg=150, hg=50,
                image_7="border-image:url(C-7.png)", image_dur="border-image:url(C-dur.png)", image_mol="border-image:url(C-mol.png)",
                sound_7="rocket.wav", sound_dur="rocket.wav", sound_mol="rocket.wav")

akord_f = Chord(variant="F_chords", x_cor=600, y_cor=300, wg=150, hg=50,
                image_7="border-image:url(C-7.png)", image_dur="border-image:url(C-dur.png)", image_mol="border-image:url(C-mol.png)",
                sound_7="rocket.wav", sound_dur="rocket.wav", sound_mol="rocket.wav")

akord_g = Chord(variant="G_chords", x_cor=150, y_cor=400, wg=150, hg=50,
                image_7="border-image:url(C-7.png)", image_dur="border-image:url(C-dur.png)", image_mol="border-image:url(C-mol.png)",
                sound_7="rocket.wav", sound_dur="rocket.wav", sound_mol="rocket.wav")

akord_a = Chord(variant="A_chords", x_cor=330, y_cor=400, wg=150, hg=50,
                image_7="border-image:url(C-7.png)", image_dur="border-image:url(C-dur.png)", image_mol="border-image:url(C-mol.png)",
                sound_7="rocket.wav", sound_dur="rocket.wav", sound_mol="rocket.wav")

akord_b = Chord(variant="B_chords", x_cor=510, y_cor=400, wg=150, hg=50,
                image_7="border-image:url(C-7.png)", image_dur="border-image:url(C-dur.png)", image_mol="border-image:url(C-mol.png)",
                sound_7="rocket.wav", sound_dur="rocket.wav", sound_mol="rocket.wav")

akord_cis = Chord(variant="Cis_chords", x_cor=60, y_cor=500, wg=150, hg=50,
                  image_7="border-image:url(C-7.png)", image_dur="border-image:url(C-dur.png)", image_mol="border-image:url(C-mol.png)",
                sound_7="rocket.wav", sound_dur="rocket.wav", sound_mol="rocket.wav")

akord_dis = Chord(variant="Dis_chords", x_cor=240, y_cor=500, wg=150, hg=50,
                  image_7="border-image:url(C-7.png)", image_dur="border-image:url(C-dur.png)", image_mol="border-image:url(C-mol.png)",
                sound_7="rocket.wav", sound_dur="rocket.wav", sound_mol="rocket.wav")

akord_fis = Chord(variant="Fis_chords", x_cor=420, y_cor=500, wg=150, hg=50,
                  image_7="border-image:url(C-7.png)", image_dur="border-image:url(C-dur.png)", image_mol="border-image:url(C-mol.png)",
                sound_7="rocket.wav", sound_dur="rocket.wav", sound_mol="rocket.wav")

akord_gis = Chord(variant="Gis_chords", x_cor=600, y_cor=500, wg=150, hg=50,
                  image_7="border-image:url(C-7.png)", image_dur="border-image:url(C-dur.png)", image_mol="border-image:url(C-mol.png)",
                sound_7="rocket.wav", sound_dur="rocket.wav", sound_mol="rocket.wav")

akord_h = Chord(variant="H_chords", x_cor=330, y_cor=200, wg=150, hg=50,
                image_7="border-image:url(C-7.png)", image_dur="border-image:url(C-dur.png)", image_mol="border-image:url(C-mol.png)",
                sound_7="rocket.wav", sound_dur="rocket.wav", sound_mol="rocket.wav")

akord_list = [akord_c, akord_d, akord_e, akord_f, akord_g, akord_a, akord_b, akord_cis, akord_dis, akord_fis, akord_gis, akord_h]

for akord in akord_list:
    akord.create_button(window)
    akord.create_new_window()



window.create_logo()



#if __name__ = "__main__":
window.show()

sys.exit(app.exec())
