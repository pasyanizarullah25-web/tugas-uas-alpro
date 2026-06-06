#soal1 Return tanpa ekspresi: memanggil fungsi tanpa argumen
# def fungsi_tanpa_ekspresi():
#     print("Fungsi ini tidak mengembalikan nilai apa pun.")
#     return

# fungsi_tanpa_ekspresi()

#soal2 Return tanpa ekspresi: memanggil fungsi dengan argumen False
# def fungsi_dengan_argumen(arg):
#     if arg:
#         print("Argumen bernilai True.")
#     else:
#         print("Argumen bernilai False.")
#     return

# fungsi_dengan_argumen(False)

#soal3 Return dengan ekspresi: menyimpan nilai yang di return ke dalam variabel
# def fungsi_dengan_return():
#     return "Fungsi ini mengembalikan sebuah string." 
# hasil = fungsi_dengan_return()
# print(hasil)

#soal4 Return dengan ekspresi: mengabaikan nilai yang di return dari fungsi
# def fungsi_dengan_return():
#     return "Fungsi ini mengembalikan sebuah string."
# fungsi_dengan_return()  

#soal5 Keyword None
# def fungsi_dengan_none():
#     return None
# print(fungsi_dengan_none())

#soal6 List sebagai argument dari fungsi
# def fungsi_dengan_list(argumen_list):
#     print("Isi list yang diterima:")
#     for item in argumen_list:
#         print(item)
# contoh_list = [1, 2, 3, 4, 5]
# fungsi_dengan_list(contoh_list)

#soal7 Coba ganti argument pada saat pemanggilan sesuai dengan modul
# def fungsi_dengan_argumen(arg):
#     print(f"Argumen yang diterima: {arg}")
# fungsi_dengan_argumen("Hello, World!")

#soal8 List sebagai hasil dari fungsi
# def fungsi_kembalikan_list():
#     return [1, 2, 3, 4, 5]
# hasil_list = fungsi_kembalikan_list()
# print(hasil_list)

#soal9 kuis23
# def tahun_kabisat(tahun):
#     # Tahun kabisat jika:
#     # habis dibagi 400
#     # atau habis dibagi 4 tetapi tidak habis dibagi 100
    
#     if (tahun % 400 == 0) or (tahun % 4 == 0 and tahun % 100 != 0):
#         return True
#     else:
#         return False
# # Data uji
# data_uji = [1900, 2000, 2016, 1987]
# # Hasil yang diharapkan
# data_hasil = [False, True, True, False]
# # Pengujian
# for i in range(len(data_uji)):
#     th = data_uji[i]
#     print(th, "->", end=" ")
#     hasil = tahun_kabisat(th)
#     if hasil == data_hasil[i]:
#         print("OK")
#     else:
#         print("Gagal")

#soal10 kuis24
# def tahun_kabisat(tahun):
#     if (tahun % 400 == 0) or (tahun % 4 == 0 and tahun % 100 != 0):
#         return True
#     else:
#         return False

# def hari_didalam_bulan(tahun, bulan):
#     # Februari
#     if bulan == 2:
#         if tahun_kabisat(tahun):
#             return 29
#         else:
#             return 28
#     # Bulan dengan 31 hari
#     elif bulan in [1, 3, 5, 7, 8, 10, 12]:
#         return 31
#     # Bulan dengan 30 hari
#     else:
#         return 30

# data_uji = [1900, 2000, 2016, 1987]
# data_bulan = [2, 2, 1, 11]
# data_hasil = [28, 29, 31, 30]

# for i in range(len(data_uji)):
#     thn = data_uji[i]
#     bln = data_bulan[i]
#     print(thn, bln, "->", end=" ")
#     hasil = hari_didalam_bulan(thn, bln)
#     if hasil == data_hasil[i]:
#         print("OK")
#     else:
#         print("Gagal")

#soal11 kuis25
# def tahun_kabisat(tahun):
#     if (tahun % 400 == 0) or (tahun % 4 == 0 and tahun % 100 != 0):
#         return True
#     else:
#         return False

# def hari_didalam_bulan(tahun, bulan):
#     if bulan == 2:
#         if tahun_kabisat(tahun):
#             return 29
#         else:
#             return 28
#     elif bulan in [1, 3, 5, 7, 8, 10, 12]:
#         return 31
#     elif bulan in [4, 6, 9, 11]:
#         return 30
#     else:
#         return None

# def hari_pada_tahun(tahun, bulan, hari):
#     # cek validasi bulan
#     jumlah_hari = hari_didalam_bulan(tahun, bulan)
#     if jumlah_hari is None:
#         return None
#     # cek validasi hari
#     if hari < 1 or hari > jumlah_hari:
#         return None
#     total_hari = hari
#     # menjumlahkan hari dari bulan sebelumnya
#     for b in range(1, bulan):
#         total_hari += hari_didalam_bulan(tahun, b)
#     return total_hari
# # Test
# print(hari_pada_tahun(2000, 12, 31))

# Soal 12 kuis26
# def cek_prima(bilangan):
#     # Bilangan prima harus lebih dari 1
#     if bilangan <= 1:
#         return False
#     # Mengecek pembagi selain 1 dan dirinya sendiri
#     for i in range(2, bilangan):
#         if bilangan % i == 0:
#             return False
#     return True

# for i in range(1, 20):
#     if cek_prima(i + 1):
#         print(i + 1, end=" ")
# print()

# Soal 13 kuis27
# def cek_prima(bilangan):
#     # Bilangan prima harus lebih dari 1
#     if bilangan <= 1:
#         return False
#     # Mengecek apakah ada pembagi selain 1 dan dirinya sendiri
#     for i in range(2, bilangan):
#         if bilangan % i == 0:
#             return False
#     return True

# for i in range(1, 20):
#     if cek_prima(i + 1):
#         print(i + 1, end=" ")
# print()

#soal14 kuis28
def Liter100km_ke_mpg(liter):
    km_ke_mil = 100 / 1.609344
    galon = liter / 3.785411784    
    mil_per_galon = km_ke_mil / galon
    return mil_per_galon

def mpg_ke_Liter100km(mil):
    km_per_galon = mil * 1.609344    
    galon_per_100km = 100 / km_per_galon
    liter_per_100km = galon_per_100km * 3.785411784
    return liter_per_100km

print(Liter100km_ke_mpg(3.9))
print(Liter100km_ke_mpg(7.5))
print(Liter100km_ke_mpg(10.))
print(mpg_ke_Liter100km(60.3))
print(mpg_ke_Liter100km(31.4))
print(mpg_ke_Liter100km(23.5))