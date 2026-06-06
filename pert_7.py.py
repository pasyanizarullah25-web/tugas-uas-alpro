#langkah 3
# anggota = []

# jumlah_anggota = int(input("Masukkan jumlah anggota: "))

# for i in range(jumlah_anggota):
#     nama = input("Masukan Nama: ")
#     anggota.append(nama)

# print(anggota)

# anggota = ["jeruk", "apel", "mangga", "pisang", "anggur", "semangka"]
# del anggota[1:3]
# print(anggota)

# anggota = ["jeruk", "apel", "mangga", "pisang", "anggur", "semangka"]
# print(anggota[0:5])

# buah = ["jeruk", "apel", "mangga", "pisang", "anggur", "semangka"]
# print(buah[-4:-2])

# buah = ["jeruk", "apel", "mangga", "pisang", "anggur", "semangka"]
# buah.insert(4, "nanas")
# buah.append("kiwi")
# buah.append("melon")
# print(buah)

#list in act 2
# list = [10, 1, 8, 3, 5]

# list[0], list[4] = list[4], list[0]
# list[1], list[3] = list[3], list[1]
# print(list)


# soal 1
# angka = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# angka[2:4] = angka[5:7]
# print(angka)


# soal 2
# angka = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(angka[0:8:3])


# angka = [1, 2, 4, 5, 6, 7, 8, 9, 10]
# for i in range(len(angka)):
#     print(angka[i])

# list = [1, 2, 3, 4, 5]
# list[len(list) // 2]
# del list[-1]
# print(len(list))
# print(list)

# my_list = []
# for i in range(10):
#     my_list.append(i + 20)
# print(my_list)

# my_list = []
# for i in range(10):
#     my_list.insert(0, i + 20)
# print(my_list)


# soal 3 - fungsi len
# angka = [1, "aufa"]
# print(len(angka))

# soal 4 - menghapus element list
# buah = ["jeruk", "apel", "mangga", "pisang", "anggur", "semangka"]
# del buah[1:3]
# print(buah)

# soal 5 - negative index
# buah = ["jeruk", "apel", "mangga", "pisang", "anggur", "semangka"]
# print(buah[-5:-1])

# soal 6
# topi_list = [1, 2, 3, 4, 5]
# topi_list[len(topi_list)//2] = int(input("Masukkan angka: "))
# del topi_list[-1]

# print(len(topi_list))
# print(topi_list)

# soal 7 - append dan insert
# buah = ["jeruk", "apel", "mangga", "pisang", "anggur", "semangka"]
# buah.insert(4, "nanas")

# buah.append("kiwi")
# buah.append("melon")
# print(buah)

# soal 8 
# list_1 = []
# for i in range(10):
#     list_1.append(i + 1)
# print(list_1)

# list_2 = []
# for i in range(10):
#     list_2.insert(0, i + 1)
# print(list_2)

# soal 10
# my_list = [10, 1, 8, 3, 5]
# total = 0

# for i in range(len(my_list)):
#     total += my_list[i]
# print(total)

# soal 11
# my_list = [10, 1, 8, 3, 5]
# total = 0

# for i in my_list:
#     total += i
# print(total)

# soal 12 - list in act 2
# list = [10, 1, 8, 3, 5]

# for i in range(len(list) // 2):
#     list[i], list[len(list) - 1 - i] = list[len(list) - 1 - i], list[i]
# print(list)

# soal 13
# exo = []

# exo.append("Suho")
# exo.append("Kai")
# exo.append("Chanyeol")
# exo.append("Sehun")

# anggota_tambahan = ["DO", "Baekhyun", "Kris", "Lay", "Luhan", "Tao", "Chen"]
# for nama in anggota_tambahan:
#     exo.append(nama)

# del exo[6:9]

# exo.insert(-2, "Xiumin") 

# print("Daftar anggota EXO akhir:")
# print(exo)
# print(f"Jumlah anggota: {len(exo)}")

# Langkah 1
exo = []
print("langkah 1: ", exo)

# Langkah 2
exo.append("Suho")
exo.append("Kai")
exo.append("Chanyeol")
exo.append("Sehun")

print("Langkah 2: ", exo)

# Langkah 3
anggota_tambahan = ["DO", "Baekhyun", "Kris", "Lay", "Luhan", "Tao", "Chen"]
for nama in anggota_tambahan:
    exo.append(nama)

print("Langkah 3: ", exo)
print(f"Jumlah anggota: {len(exo)}")

# Langkah 4
del exo[6]
del exo[7:9]
print("Langkah 4: ", exo)
print(f"Jumlah anggota: {len(exo)}")

# Langkah 5
exo.insert(-2, "Xiumin")
print("Langkah 5: ", exo)
print(f"Jumlah anggota: {len(exo)}")
