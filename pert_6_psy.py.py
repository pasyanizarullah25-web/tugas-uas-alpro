#soal 1: Perulangan While  
# i = 1
# while i < 100:
#     print(i)
#     i = i + 2

#soal 2: Perulangan For
# for i in range(100):
#     print("Pria Sawit")

#Soal 3: Contoh kasus menghitung angka ganjil dan genap dengan perulangan while
# i = 1
# while i <= 100:
#     if i % 2 == 0:
#         print(f"{i} adalah angka genap")
#     else:
#         print(f"{i} adalah angka ganjil")
#     i += 1

# Soal 4: Kuis 15
# secret_number = 777
# guess = int(input("Tebak angka rahasia antara 1 dan 1000: "))

# while guess != secret_number:
#     print("hahaha! kamu nyangkut di loop saya")
#     guess = int(input("Terai Again: "))
# print("Selamat, Muggle! Kamu bebas sekarang!")


#Soal 5: Perulangan dengan for, contoh 1: bandingkan nilai a,b,c,d,e
# a = 10
# b = 20
# c = 30
# d = 40
# e = 50
# for i in range(1, 6):
#     if i == 1:
#         print(f"Nilai a: {a}")
#     elif i == 2:
#         print(f"Nilai b: {b}")
#     elif i == 3:
#         print(f"Nilai c: {c}")
#     elif i == 4:
#         print(f"Nilai d: {d}")
#     elif i == 5:
#         print(f"Nilai e: {e}")

# Soal 6: Perulangan dengan for, contoh 2: menghitung eksponensial 2
# for i in range(10):
#     print(f"2 pangkat {i} adalah {2 ** i}")

# Soal 7: Contoh break dan continue.
# for i in range(1, 11):
#     if i == 5:
#         print("ditemukan angka 5, keluar dari loop.")
#         break
#     elif i % 2 == 0:
#         continue
#         # print(f"{i} adalah angka genap, kodingan dilanjutkan.")
#     print(f"{i} adalah angka ganjil.")

# soal 8: Kuis 16: implementasi break
# print(f"Saya adalah pesulap dan anda harus menebak nomor rahasianya!")
# print(f"Jika anda menebak dengan benar, anda akan bebas!")
# print(f"pilih angka 1 - 10")

# secret_number = 7
# while True:
#     guess = int(input("Tebak nomor rahasia: "))
#     if guess == secret_number:
#         print("Selamat, kamu menebak dengan benar! Kamu bebas sekarang!")
#         break
#     else:
#         print("hahaha! kamu nyangkut di loop saya")

# soal 9: Kuis 17: implementasi continue | tidak mengikuti soal
# print(f"Saya adalah pesulap dan anda harus menebak nomor rahasianya!")
# print(f"Jika anda menebak dengan benar, anda akan bebas!")
# print(f"pilih angka 1 - 10")

# secret_number = 7
# while True:
#     guess = int(input("Tebak nomor rahasia: "))
#     if guess == secret_number:
#         print("Selamat, kamu menebak dengan benar! Kamu bebas sekarang!")
#         break
#     elif guess < secret_number:
#         print("Tebakan terlalu rendah, coba lagi!")
#         continue
#     else:
#         print("Tebakan terlalu tinggi, coba lagi!")
#         continue

# soal 9: Kuis 17: implementasi continue
# word = input("Masukkan sebuah kata: ")
# word = word.upper()

# for char in word:
#     if char == "A" or char == "i" or char == "U" or char == "E" or char == "O":
#         continue
#     else:
#         print(char)

# Soal 10: Perulangan while dengan else
# i = 1
# while i <= 5:
#     print(f"Perulangan ke-{i}")
#     i += 1
# else:
#     print("Perulangan selesai.")

# Soal 11: Perulangan for dengan else
# for i in range(1, 6):
#     print(f"Perulangan ke-{i}")
# else:
#     print("Perulangan selesai.")

# Soal 12: Contoh ekspresi logika pada python
# a = 10
# b = 20

# print(a < b and a > 5)  
# print(a < b or a > 15)
# print(not (a < b))

# Soal 13: Operasi logical vs. Bit pada python
# a = True
# b = False

# print("Operasi Logical:")
# print(f"a AND b: {a and b}")
# print(f"a OR b: {a or b}")
# print(f"NOT a: {not a}")

# x = 7
# y = 5
# print("\nOperasi Bit:")
# print(f"x AND y: {x & y}")
# print(f"x OR y: {x | y}")
# print(f"x XOR y: {x ^ y}")
# print(f"NOT x: {~x}")

# Soal 14: Binary Shifting
# x = 8
# print(f"Nilai awal x adalah: {x}")
# print(f"x << 1: {x << 1}")
# print(f"x >> 1: {x >> 1}")

# Soal 15: Latihan bitwise operator dan binary shifting
# x = 4
# y = 1

# a = x & y
# b = x | y
# c = ~x
# d = x ^ 5
# e = x >> 2
# f = x << 2

# print(a, b, c, d, e, f)

# percobaan
# secret_number = 777
# guess = int(input("Tebak angka rahasia antara 1 dan 1000: "))
# limit = 5

# while guess != secret_number:
#     limit -= 1
#     print("hahaha! tebakanmu salah, coba lagi!")
#     print(f"Kamu memiliki {limit} kesempatan tersisa.")
#     guess = int(input("Tebak lagi: "))
#     if limit == 1:
#         print("Maaf, kamu kehabisan kesempatan! Game over.")
#         break
# else:
#     print("Selamat, Muggle! Kamu bebas sekarang!")

# no 5
# for i in range(1, 6):
#     print(input(f"Masukkan nama ke-{i}: "))
    
