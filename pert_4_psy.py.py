# Soal No 1
def sapa_pengguna():
    nama = input("Masukkan nama anda: ") 
    print(f"halo {nama}, selamat datang")
sapa_pengguna()

# Soal No 2
def sapa(nama):
    print(f"halo {nama}, selamat datang")
sapa("aufa")

# Soal No 3
nama = input("Masukkan nama anda: ")
umur = int(input("Masukkan umur anda: "))

# Soal No 4
tinggi_badan = float(input("Masukkan tinggi badan anda (dalam cm): "))

# Soal No 5
a = float(input("Masukkan panjang sisi alas (a): "))
b = float(input("Masukkan panjang sisi tinggi (b): "))
hypo = (a**2 + b**2)** 0.5

print(f"Panjang sisi miring adalah: {hypo}")

# Soal No 6
a = float(input("Masukkan panjang sisi alas (a): "))
b = float(input("Masukkan panjang sisi tinggi (b): "))
print(f"Panjang sisi miring adalah: {(a**2 + b**2)** 0.5}")

# Soal No 7(Operator Konkatenasi)
nama_depan = input("Masukkan nama depan anda: ")
nama_belakang = input("Masukkan nama belakang anda: ")
nama_lengkap = nama_depan + " " + nama_belakang

print(f"Nama lengkap anda adalah: {nama_lengkap}")

# Soal No 8(Operator Replikasi)
kata = input("Masukkan sebuah kata: ")
jumlah = int(input("Masukkan jumlah pengulangan: "))
hasil = kata * jumlah

print(f"Hasil pengulangan kata: {hasil}")

# Soal No 9
angka_bulat = 20
angka_desimal = 3.14
ini_boolean = True

str_angka_bulat = str(angka_bulat)
str_angka_desimal = str(angka_desimal)
str_ini_boolean = str(ini_boolean)

print(f"Nilai angka_bulat: {str_angka_bulat}, tipe data: {type(str_angka_bulat)}")
print(f"Nilai angka_desimal: {str_angka_desimal}, tipe data: {type(str_angka_desimal)}")
print(f"Nilai ini_boolean: {str_ini_boolean}, tipe data: {type(str_ini_boolean)}")

# Soal No 10
nama = "Aufa"
umur = 20
print(f"{nama} tipe datanya adalah {type(nama)}")
print(f"{umur} tipe datanya adalah {type(umur)}")

# # Soal No 11(kuis no 7)
a = int(input("Masukkan nilai int pertama: "))
b = int(input("Masukkan nilai int kedua: "))

print(f"Hasil penjumlahan: {a + b}")
print(f"Hasil pengurangan: {a - b}")
print(f"Hasil perkalian: {a * b}")
print(f"Hasil pembagian: {a / b}")
print("Selamat kamu sudah pintar matematika:))))")


# Soal No 13(kuis no 9)
jam = int(input("Waktu mulai (jam): "))
menit = int(input("Waktu mulai (menit): "))
durasi = int(input("Durasi Acara (menit): "))
total_menit = jam * 60 + menit + durasi

jam_selesai = total_menit // 60
menit_selesai = total_menit % 60
print("Acara selesai pukul", jam_selesai, ":", menit_selesai)