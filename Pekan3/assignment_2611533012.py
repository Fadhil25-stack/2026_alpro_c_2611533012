# Buat file dengan nama assignment_NIM.py
# Nama variabel ditambah 4 digit nim terakhir contoh: angka1_1234
# Program ini menggunakan fungsi input()
# Nilai yang dimasukkan akan dikonversi menjadi tipe data integer
# Program operator assignment dalam Python

angka1_3012 = int(input("Input angka-1: "))
angka2_3012 = int(input("Input angka-2: "))

print("\nNilai awal angka1 =", angka1_3012)
print("Nilai angka2 =", angka2_3012)

# Assignment biasa
hasil_3012 = angka1_3012
print("\nAssignment biasa (=)")
print("Hasil =", hasil_3012)

# Assignment penambahan
hasil_3012 = angka1_3012
hasil_3012 += angka2_3012
print("\nAssignment penambahan (+=)")
print("Hasil =", hasil_3012)

# Assignment pengurangan
hasil_3012 = angka1_3012
hasil_3012 -= angka2_3012
print("\nAssignment pengurangan (-=)")
print("Hasil =", hasil_3012)

# Assignment perkalian
hasil_3012 = angka1_3012
hasil_3012 *= angka2_3012
print("\nAssignment perkalian (*=)")
print("Hasil =", hasil_3012)

# Assignment pembagian, pembagian bulat, dan sisa bagi
if angka2_3012 != 0:
    hasil_3012 = angka1_3012
    hasil_3012 /= angka2_3012
    print("\nAssignment pembagian (/=)")
    print("Hasil =", hasil_3012)
    # Operator tambahan
    hasil_3012 = angka1_3012
    hasil_3012 //= angka2_3012
    print("\nAssignment pembagian bulat (//=)")
    print("Hasil =", hasil_3012)
    hasil_3012 = angka1_3012
    hasil_3012 %= angka2_3012
    print("\nAssignment sisa bagi (%=)")
    print("Hasil =", hasil_3012)
else:
    print("\nPembagian tidak dapat dilakukan.")
    print("Angka kedua tidak boleh bernilai 0.")

# Operator tambahan: assignment perpangkatan
hasil_3012 = angka1_3012
hasil_3012 **= angka2_3012
print("\nAssignment perpangkatan (**=)")
print("Hasil =", hasil_3012)