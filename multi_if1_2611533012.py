# Buat file dengan nama multi_if1_nim.py
# Buat progran untuk kondisional if
# Nama variable ditambah 4 digit nim terakhir contoh: ipk_1234
# Program ini nenggunakan fungsi Input()

umur_3012 = int(input("Input umur anda: "))
sim_3012 = input("Apakah Anda Sudah Punya Sim C (y/t): ")[0]

if umur_3012 >= 17 and sim_3012 == 'y':
    print("Anda Sudah dewasa dan boleh bawa motor")
    
if umur_3012 >= 17 and sim_3012 != 'y':
    print("Anda Sudah dewasa tetapi tidak boleh bawa motor")

if umur_3012 < 17 and sim_3012 == 'y':
    print("Anda Belum Cukup Umur Punya SIM")

if umur_3012 < 17 and sim_3012 != 'y' :
    print("Anda Belum Cukup Umur bawa motor")
print("Program selesai")