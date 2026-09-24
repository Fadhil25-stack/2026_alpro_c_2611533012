#Buat file dengan nama if elif_else1_nim.py
# Buat program untuk kodisional if
# Nama variabel ditambah 4 digit terakhir dontoh: ipk_1234
# Program ini menggunakan fungsi input()

umur_3012 = int(input("Input Umur Anda = "))
sim_3012 = input("Apakah Anda Sudah Punya SIM (y/t): ")[0]

if umur_3012 >= 17 and sim_3012 == "y":
    print("Anda Sudah dewasa dan boleh bawa motor")
elif umur_3012 >= 17 and sim_3012 != "y":
    print ("Anda Sudah dewasa tetapi tidak boleh bawa motor")
elif umur_3012 < 17 and sim_3012 == "y":
    print("Anda Belum Cukup Umur punya SIM")
else:
    print ("Anda Belum Cukup Umur dan tidak boleh bawa motor")
print ("Program Selesai")