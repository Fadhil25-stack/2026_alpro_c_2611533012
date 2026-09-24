#Buat file dengan nama 1f2_nim.py
#  #Buat program untuk kondisional if
#Nama vardabel ditambah 4 digit nim terakhir contoh: ipk_1234
#Program in1 menggunakan fungsi input()

ipk_3012 = float(input("Input IPK Anda =  "))
if ipk_3012 > 2.75:
    print("Anda Lulus Sangat Memuaskan dengan IPK" + str(ipk_3012))
else:
    print("Anda Tidak Lulus")
print("Program Selesai")