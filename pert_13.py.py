#soal1 Membuat tuple dan tampilkan
# data_tuple = (1, 2, 3, 4, 5)
# print(data_tuple)

#soal2 Menggunakan tuple
# data_tuple = (10, 20, 30, 40, 50)
# print(data_tuple[0])

#soal3 Memodifikasi tuple
# data_tuple = (1, 2, 3, 4, 5)
# data_list = list(data_tuple)
# data_list[0] = 10
# data_tuple = tuple(data_list)
# print(data_tuple)

#soal4 Menggunakan tuple dengan len(), +,*, in dan not in
# data_tuple1 = (1, 2, 3)
# data_tuple2 = (4, 5, 6)
# print(len(data_tuple1))
# print(data_tuple1 + data_tuple2)
# print(data_tuple1 * 2)
# print(2 in data_tuple1)
# print(10 not in data_tuple1)

#soal5 Penugasan simultan pada tuple
# data_tuple = (1, 2, 3)
# a, b, c = data_tuple
# print(a)
# print(b)
# print(c)

#soal6 Membuat dictionary dan tampilkan
# data_dict = {"nama": "Aufa", "umur": 20, "kota": "Jakarta"}
# print(data_dict)

#soal7 Mengakses nilai dalam dictionary
# data_dict = {"nama": "Aufa", "umur": 20, "kota": "Jakarta"}
# print(data_dict["nama"])
# print(data_dict["umur"])
# print(data_dict["kota"])

#soal8 Method keys()
# data_dict = {"nama": "Aufa", "umur": 20, "kota": "Jakarta"}
# print(data_dict.keys())

#soal9 Method values()
# data_dict = {"nama": "Aufa", "umur": 20, "kota": "Jakarta"}
# print(data_dict.values())

#soal10 Method items()
# data_dict = {"nama": "Aufa", "umur": 20, "kota": "Jakarta"}
# print(data_dict.items())

#soal11 Methode update()
# data_dict = {"nama": "Aufa", "umur": 20, "kota": "Jakarta"}
# data_dict.update({"umur": 21, "kota": "Bandung"})
# print(data_dict)

# #soal12 Method popitem()
# data_dict = {"nama": "Aufa", "umur": 20, "kota": "Jakarta"}
# data_dict.popitem()
# print(data_dict)

#soal13 Modifikasi dictionary
# data_dict = {"nama": "Aufa", "umur": 20, "kota": "Jakarta"}
# data_dict["umur"] = 21
# data_dict["kota"] = "Bandung"
# print(data_dict)

#soal14 Menangani exception
# data_dict = {"nama": "Aufa", "umur": 20, "kota": "Jakarta"}
# try:
#     print(data_dict["pekerjaan"])
# except KeyError:
#     print("Key tidak ditemukan")

#soal15 Menangani multiple exception
data_dict = {"nama": "Aufa", "umur": 20, "kota": "Jakarta"}
try:
    print(data_dict["pekerjaan"])
except KeyError:
    print("Key tidak ditemukan")
except Exception as e:
    print(f"Terjadi kesalahan: {e}")