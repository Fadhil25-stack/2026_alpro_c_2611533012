# Buat file dengan nama aritmatika_NIM.py
# Buat program untuk operator aritmatika dalam Python
# Nama variabel ditambah 4 digit nim terakhir contoh: angka1_1234
# Program ini menggunakan fungsi input()
# Nilai yang dimasukkan akan dikonversi menjadi tipe data integer

angka1_3012 = int(input("Input angka-1: "))
angka2_3012 = int(input("Input angka-2: "))

# Penjumlahan
hasil_3012 = angka1_3012 + angka2_3012
print("\nOperator Penjumlahan")
print("Hasil =", hasil_3012)

# Pengurangan
hasil_3012 = angka1_3012 - angka2_3012
print("\nOperator Pengurangan")
print("Hasil =", hasil_3012)

# Perkalian
hasil_3012 = angka1_3012 * angka2_3012
print("\nOperator Perkalian")
print("Hasil =", hasil_3012)

# Pembagian, pembagian bulat, dan sisa bagi
if angka2_3012 != 0:
    hasil_3012 = angka1_3012 / angka2_3012
    print("\nOperator Pembagian")
    print("Hasil =", hasil_3012)

    hasil_3012 = angka1_3012 // angka2_3012
    print("\nOperator Pembagian Bulat")
    print("Hasil =", hasil_3012)

    hasil_3012 = angka1_3012 % angka2_3012
    print("\nOperator Sisa Bagi")
    print("Hasil =", hasil_3012)
else:
    print("Angka kedua tidak boleh bernilai 0.")

# Pangkat
hasil_3012 = angka1_3012 ** angka2_3012
print("\nOperator Pangkat")
print("Hasil =", hasil_3012)