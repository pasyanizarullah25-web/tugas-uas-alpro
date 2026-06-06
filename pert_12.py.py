#soal1 Variable local: variable yang berada di dalam fungsi
# def fungsi_local():
#     local_var = "Saya adalah variable lokal."
#     print(local_var)
# fungsi_local()

#soal2 Variable di luar fungsi -1
# global_var = "Saya adalah variable global."
# def fungsi_global():
#     print(global_var)
# fungsi_global()

#soal3 Variable di luar fungsi -2
# global_var = "Saya adalah variable global."
# def fungsi_global():
#     global global_var
#     global_var = "Saya telah diubah di dalam fungsi."
# fungsi_global()  
# print(global_var)

#soal4 Variable global dengan keyword ‘global’
# global_var = "Saya adalah variable global."
# def fungsi_ubah_global():
#     global global_var
#     global_var = "Saya telah diubah di dalam fungsi."
# print("Sebelum pemanggilan fungsi:", global_var)
# fungsi_ubah_global()
# print("Setelah pemanggilan fungsi:", global_var)

#soal5 kuis MIT
# def hitung_imt(berat, tinggi):
#     # Menghitung IMT = berat (kg) / (tinggi (m) ^ 2)
#     imt = berat / (tinggi ** 2)
#     return imt

# berat = float(input("Masukkan berat badan (kg): "))
# tinggi = float(input("Masukkan tinggi badan (meter): "))

# index_massa_tubuh = hitung_imt(berat, tinggi)
# kategori = ["Normal", "Gemuk", "Obesitas"]
# if index_massa_tubuh < 18.5:
#     print("Index massa tubuh anda adalah", round(index_massa_tubuh, 2), "termasuk kategori Kurus")
# elif index_massa_tubuh < 25:
#     print("Index massa tubuh anda adalah", round(index_massa_tubuh, 2), "termasuk kategori", kategori[0])
# elif index_massa_tubuh < 30:
#     print("Index massa tubuh anda adalah", round(index_massa_tubuh, 2), "termasuk kategori", kategori[1])
# else:
#     print("Index massa tubuh anda adalah", round(index_massa_tubuh, 2), "termasuk kategori", kategori[2], ". Anda harus diet!")

#soal6 Fungsi segitiga -1
# def hitung_luas_segitiga(alas, tinggi):
#     luas = 0.5 * alas * tinggi
#     return luas
# alas = 10
# tinggi = 5
# luas_segitiga = hitung_luas_segitiga(alas, tinggi)
# print(f"Alas = {alas}")
# print(f"Tinggi = {tinggi}")
# print(f"Luas segitiga = 0.5 x {alas} x {tinggi} = {luas_segitiga}")

#soal7 Fungsi segitiga -2
# def hitung_luas_segitiga(alas, tinggi):
#     luas = 0.5 * alas * tinggi
#     return luas
# alas = 10
# tinggi = 5
# luas_segitiga = hitung_luas_segitiga(alas=alas, tinggi=tinggi)
# print(f"Alas = {alas}")
# print(f"Tinggi = {tinggi}")
# print(f"Luas segitiga = 0.5 x {alas} x {tinggi} = {luas_segitiga}")

#soal8 Fungsi segitiga -3
# def hitung_luas_segitiga(alas, tinggi):
#     luas = 0.5 * alas * tinggi
#     return luas
# luas_segitiga = hitung_luas_segitiga(tinggi=5, alas=10)
# print(f"Alas = 10")
# print(f"Tinggi = 5")
# print(f"Luas segitiga = 0.5 x 10 x 5 = {luas_segitiga}")

#soal9 KUIS FAKTORIAL
# faktorialnya: n! = 1 × 2 × 3 × ... × (n-1) × n
# 0! = 1
# def faktorial(n):
#     if n < 0:
#         return None
#     if n < 2:
#         return 1
#     hasil = 1
#     for i in range(2, n + 1):  # dari 2 sampai n
#         hasil = hasil * i
#     return hasil

# n = int(input("Masukkan nilai yang ingin di faktorial: "))
# if n < 0:
#     print("Faktorial tidak terdefinisi untuk bilangan negatif!")
# else:
    # print(n, "! = ", faktorial(n))

#soal10 KUIS FIBONACCI
# def fibonacci(n):
#     if n < 1:
#         return None
#     if n < 3:
#         return 1

#     elem_1 = elem_2 = 1
#     hasil_jumlah = 0
#     for i in range(3, n + 1):
#         hasil_jumlah = elem_1 + elem_2 
#         elem_1, elem_2 = elem_2, hasil_jumlah  
#     return hasil_jumlah

# for i in range(1, 10):
#     print(i, "->", fibonacci(i))

#soal1 Rekursif faktorial
# def faktorial(n):
#     if n < 0:
#         return None
#     if n < 2:
#         return 1
#     return n * faktorial(n - 1)
# n = int(input("Masukkan nilai yang ingin di faktorial: "))
# if n < 0:
#     print("Faktorial tidak terdefinisi untuk bilangan negatif!")
# else:
#     print(n, "! = ", faktorial(n))

#soal2 Rekursif Fibonacci
def fibonacci(n):
    if n < 1:
        return None
    if n < 3:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)
for i in range(1, 10):
    print(i, "->", fibonacci(i))
