# list multidimensi(soal 3)
# baris = int(input("Masukkan jumlah baris: "))
# kolom = int(input("Masukkan jumlah kolom: "))

# data = []

# for i in range(baris):
#     isi_baris = []
#     for j in range(kolom):
#         nilai = int(input(f"Masukkan nilai baris {i} kolom {j}: "))
#         isi_baris.append(nilai)
#     data.append(isi_baris)

# print("List Multidimensi:")
# for baris in data:
#     print(baris)

# //////////////////////////////////////////
#kuis 3
# data = [[2, 4], [6, 8], [10, 12]]
# flatten = [j for i in data for j in i]

# print(flatten)

# Soal 1 
# kuadrat = []
# for x in range(5):
#     kuadrat.append(x**2)
#     print(kuadrat)

# kuis 1
# List comprehension: 
# [ekspresi for item in iterable if kondisi]
# hasil = [n * 3 for n in range(1, 11) if n % 2 == 0]

# print(hasil)

# Soal 2
# array_2d = [
#     [10, 20, 30],
#     [40, 50, 60],
#     [70, 80, 90]
# ]

# # Menampilkan isi array
# print("Isi Array 2 Dimensi:")
# for baris in array_2d:
#     for kolom in baris:
#         print(kolom, end=" ")
#     print()

# Kuis 2
# Membuat array 2 dimensi 3x3
# array_2d = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]

# # Menampilkan seluruh isi array
# for baris in array_2d:
#     for elemen in baris:
#         print(elemen, end=" ")
#     print()  # pindah ke baris baru   

# Soal 4
# 4.  # Fungsi menghitung diskon belanja
# def hitung_diskon(total_belanja, member=False, kupon=None):
#     diskon = 0
    
#     # Diskon member 10%
#     if member:
#         diskon += 10
#         print("✅ Diskon Member 10% diterapkan")
    
#     # Diskon kupon
#     if kupon == "HEMAT20":
#         diskon += 20
#         print("✅ Kupon HEMAT20: diskon 20% diterapkan")
#     elif kupon == "HEMAT10":
#         diskon += 10
#         print("✅ Kupon HEMAT10: diskon 10% diterapkan")
    
#     # Diskon tambahan untuk belanja > 500000
#     if total_belanja > 500000:
#         diskon += 5
#         print("✅ Bonus belanja > Rp500.000: diskon 5% diterapkan")
    
#     total_diskon = total_belanja * diskon / 100
#     total_bayar = total_belanja - total_diskon
    
#     return total_bayar, diskon

# # Demo pemanggilan fungsi
# print("=== TRANSAKSI 1 ===")
# bayar1, diskon1 = hitung_diskon(350000, member=True)
# print(f"Total belanja: Rp350.000")
# print(f"Total diskon: {diskon1}%")
# print(f"Total bayar: Rp{bayar1:,.0f}")

# print("\n=== TRANSAKSI 2 ===")
# bayar2, diskon2 = hitung_diskon(750000, kupon="HEMAT20", member=False)
# print(f"Total belanja: Rp750.000")
# print(f"Total diskon: {diskon2}%")
# print(f"Total bayar: Rp{bayar2:,.0f}")

# print("\n=== TRANSAKSI 3 ===")
# bayar3, diskon3 = hitung_diskon(600000, member=True, kupon="HEMAT10")
# print(f"Total belanja: Rp600.000")
# print(f"Total diskon: {diskon3}%")
# print(f"Total bayar: Rp{bayar3:,.0f}")

# kuis 4
# Program: Fungsi menghitung luas persegi panjang
def hitung_luas_persegi_panjang(panjang, lebar):
    luas = panjang * lebar
    return luas

# Memanggil fungsi dengan panjang=8, lebar=5
p = 8
l = 5
hasil = hitung_luas_persegi_panjang(p, l)

print(f"Panjang = {p}")
print(f"Lebar   = {l}")
print(f"Luas persegi panjang = {p} x {l} = {hasil}")

# Alternatif dengan keyword argument
print("\nPemanggilan dengan keyword argument:")
luas2 = hitung_luas_persegi_panjang(panjang=8, lebar=5)
print(f"Luas = {luas2}")