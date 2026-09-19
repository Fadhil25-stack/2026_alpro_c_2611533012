# Buat file dengan nama lainnya_NIM.py
# Nama variabel ditambah 4 digit nim terakhir contoh: angka1_1234
# Program ini menggunakan fungsi input()
# Program operator keanggotaan dan  identitas

print("========================================")
print("1. OPERATOR KEANGGOTAAN")
print("========================================")

# Input beberapa data yang dipisahkan dengan koma
input_data_3012 = input("Masukkan beberapa angka, pisahkan dengan koma: ")

# Mengubah input menjadi list integer
data_3012 = [int(angka.strip()) for angka in input_data_3012.split(",")]

nilai_dicari_3012 = int(input("Masukkan angka yang ingin dicari: "))

# Operator in
hasil_3012 = nilai_dicari_3012 in data_3012
print("\nOperator keanggotaan IN")
print(nilai_dicari_3012, "in", data_3012, "=", hasil_3012)

# Operator not in
hasil = nilai_dicari_3012 not in data_3012
print("\nOperator keanggotaan NOT IN")
print(nilai_dicari_3012, "not in", data_3012, "=", hasil_3012)

print("\n========================================")
print("2. OPERATOR IDENTITAS")
print("========================================")

# objek1 menggunakan list dari input pengguna
objek1_3012 = data_3012

# objek2 merujuk pada objek yang sama dengan objek1
objek2_3012 = objek1_3012

# objek3 memiliki isi sama, tetapi merupakan objek baru
objek3_3012 = data_3012.copy()

print("objek1 =", objek1_3012)
print("objek2 =", objek2_3012)
print("objek3 =", objek3_3012)

# Operator is
hasil_3012 = objek1_3012 is objek2_3012
print("\nOperator identitas IS")
print("objek1 is objek2 =", hasil_3012)

# Operator is not
hasil_3012 = objek1_3012 is not objek3_3012
print("\nOperator identitas IS NOT")
print("objek1 is not objek3 =", hasil_3012)

# Membandingkan identitas dan nilai
print("\nPerbandingan identitas dan nilai")
print("objek1 is objek3 =", objek1_3012 is objek3_3012)
print("objek1 == objek3 =", objek1_3012 == objek3_3012)
