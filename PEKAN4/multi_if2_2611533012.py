# Buat file dengan nama multi_1f2_nim.py
# Buat program untuk kondisional if
# Nama variabel ditambah 4 digit nim terakhir contoh: total_belanja_1234
# Progran ini menggunakan fungsi Input()
# Program Menghitung Diskon Belanja

# Input dari user
total_belanja_3012 = float(input("Masukkan total belanja (Rp): "))

# Input status member (mengecek apakah user mengetik 'y' atau 'ya')
input_member_3012 = input("Apakah Anda member? (y/t): ").strip().lower()
is_member_3012 = input_member_3012 in ('y', 'ya')

# Input status kode promo (mengecek apakah user mengetik 'y' atau 'ya')
input_promo_3012 = input("Apakah kode promo valid) (y/t): ").strip(). lower()
kode_promo_valid_3012 = input_promo_3012 in ('y', 'ya')

total_diskon_persen_3012 = 0

# Multi-IF terpisah: Setiap kondisi diperiksa secara independen
# Diskon bisa ditumpuk (akumulasi) Jika memenuhi beberapa syarat sekaligus

if total_belanja_3012 > 1000000:
    total_diskon_persen_3012 += 10 # Diskon Belanja Besar
if is_member_3012 :
    total_diskon_persen_3012 += 5 # Diskon Member
if kode_promo_valid_3012:
    total_diskon_persen_3012 += 10 # Diskon Voucher

# Menghitung total nominal belanja dan diskon
nominal_diskon_3012 = total_belanja_3012 + (total_diskon_persen_3012/100)
total_bayar_3012 = total_belanja_3012 - nominal_diskon_3012

# Output hasil
print("---Rincian Pembayaran---")
print(f"Total diskon: {total_diskon_persen_3012}% (Rp. {nominal_diskon_3012:,.0f})")
print(f"Total bayar: Rp {total_bayar_3012:,.0f}")

print(f"Total diskon yang anda dapatkan  {+total_diskon_persen_3012}%")
print("program selesai")
# Output : Total diskon yang anda dapatkan 0,0% jika belanja > 1juta, member, dan kode promo valid