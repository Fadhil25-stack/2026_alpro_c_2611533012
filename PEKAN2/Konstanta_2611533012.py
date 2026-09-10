# Buat file dengan nama Konstanta_NIM.py
# Program ini menggunakan konstanta untuk menghitung luas lingkaran
# nama variable ditambah 4 digit nim terakhir contoh : jari_3012

from typing import Final
PI: Final = 3.14
print("pi : %f" % (PI))
jari_3012 = float(input("masukkan nilai jari jari:"))
luas_3012 = PI * jari_3012 * jari_3012
print( "luas lingkaran dengan jari-jari %.2f adalah %.2f" % (jari_3012, luas_3012))