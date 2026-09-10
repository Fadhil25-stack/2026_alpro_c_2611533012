# Buat file dengan nama Boolean_NIM.py
# Nama variable ditamnbah 4 digit nim terkahir contoh : nilai_1234
# Deklarasi variable dengan tipe data boolean 
is_lulus = True
is_cumlaude = True

# Menggunakan Boolean 
nilai_3012 = 85
batas_lulus_3012 = 75

# Menentukan nilai Boolean dari kondisi
status_kelulusan_3012 = nilai_3012 >= batas_lulus_3012 #Hasilnya akan True

print("--- Check kelulusan ---")
print("Nilai:", nilai_3012)
print("Apakah Lulus?:", status_kelulusan_3012)
if is_lulus and is_cumlaude:
    print("selamat, Anda lulus dengan predikat Cum laude!")