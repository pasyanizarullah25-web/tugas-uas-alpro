# soal 1: Comparison Operator
# a = 10
# b = 20
# print(a > b) 
# print(a < b)

# soal 2: kuil 11
# n = input("Masukkan sebuah angka: ")
# n = int(n)
# if n < 100:
#     print(False)
# else:
#     print(True)

# soal 3: Conditional statement: if tunggal
# a = 10

# if a > 5:
#     print("a lebih besar dari 5")

# soal 4: Conditional statement: irangkaian if
# a = 10
# if a > 5:
#     print("a lebih besar dari 5")
# if a % 2 == 0:
#     print("a adalah bilangan genap")

# soal 5: Conditional statement: if-else
# a = 10
# if a > 5:
#     print("a lebih besar dari 5")
# else:
#     print("a tidak lebih besar dari 5")

# soal 6: Conditional statement: if-elif-else
# a = 10
# if a > 10:
#     print("a lebih besar dari 10")
# elif a == 10:
#     print("a sama dengan 10")
# else:
#     print("a lebih kecil dari 10")
 
# soal 7: membandingkan dua angka input
# a = input("Masukkan angka pertama: ")
# b = input("Masukkan angka kedua: ")
# a = int(a)
# b = int(b)
# if a > b:
#     print("Angka pertama lebih besar dari angka kedua")
# elif a < b:
#     print("Angka pertama lebih kecil dari angka kedua")

# soal 8: kuis 12
# a = input("Masukkan sebuah angka: ")
# a = int(a)
# b = input("Masukkan sebuah angka: ")
# b = int(b)
# c = input("Masukkan sebuah angka: ")
# c = int(c)
# if a > b and a > c:
#     print("Angka pertama adalah yang terbesar")
# elif b > a and b > c:
#     print("Angka kedua adalah yang terbesar")
# else:
#     print("Angka ketiga adalah yang terbesar")

# soal 9: Fungsi max()
# a = input("Masukkan angka pertama: ")
# b = input("Masukkan angka kedua: ")
# c = input("Masukkan angka ketiga: ")
# d = input("Masukkan angka keempat: ")
# e = input("Masukkan angka kelima: ")
# a = int(a)
# b = int(b)
# c = int(c)
# d = int(d)
# e = int(e)
# max_value = max(a, b, c, d, e)
# print("Angka terbesar adalah:", max_value)

# soal 10: kuis 13
pendapatan = float(input("Masukkan pendapatan bulanan Anda: "))
pajak = 0.0

if pendapatan < 60000000:
    pajak = 0.05 * pendapatan
elif pendapatan >= 60000000 and pendapatan < 250000000:
    pajak = 0.15 * pendapatan
elif pendapatan >= 250000000 and pendapatan < 500000000:
    pajak = 0.25 * pendapatan
else:
    pajak = 0.30 * pendapatan

print("Pajak yang harus dibayar: Rp", pajak)
