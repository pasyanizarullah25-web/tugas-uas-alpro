# ================================
# SISTEM CAFE SEDERHANA
# ================================

# =====================================
# VARIABEL GLOBAL
# =====================================
pesanan = []
wishlist = []
total_harga = 0
nama_pelanggan = ""
tipe_pesanan = ""

# =====================================
# INPUT PELANGGAN
# =====================================
def input_pelanggan():
    global nama_pelanggan, tipe_pesanan

    print("\n" + "=" * 45)
    print("        SELAMAT DATANG DI CAFE")
    print("=" * 45)

    nama_pelanggan = input("Masukkan Nama Pelanggan : ")

    print("\nPilih Tipe Pesanan")
    print("1. Takeaway")
    print("2. Dine In")

    pilihan = input("Masukkan pilihan : ")

    if pilihan == "1":
        tipe_pesanan = "Takeaway"
    elif pilihan == "2":
        tipe_pesanan = "Dine In"
    else:
        tipe_pesanan = "Dine In"


# =====================================
# FUNGSI TAMBAH PESANAN
# =====================================
def tambah_ke_pesanan(nama_item, harga, qty):
    global total_harga

    subtotal = harga * qty

    pesanan.append({
        "nama": nama_item,
        "harga": harga,
        "qty": qty,
        "subtotal": subtotal
    })

    total_harga += subtotal

    print(f"\n✅ {nama_item} berhasil ditambahkan ke pesanan!")


# =====================================
# FUNGSI TAMBAH WISHLIST
# =====================================
def tambah_ke_wishlist(nama_item, harga, qty):
    wishlist.append({
        "nama": nama_item,
        "harga": harga,
        "qty": qty
    })

    print(f"💖 {nama_item} berhasil ditambahkan ke wishlist!")


# =====================================
# LIHAT WISHLIST
# =====================================
def lihat_wishlist():
    if not wishlist:
        print("\nWishlist kosong.")
        return

    print("\n" + "=" * 45)
    print("              WISHLIST")
    print("=" * 45)

    for idx, item in enumerate(wishlist, start=1):
        print(f"{idx:<3} {item['nama']:<30} {item['qty']} pcs   Rp{item['harga']:>8,}")


# =====================================
# PINDAH DARI WISHLIST
# =====================================
def pindah_dari_wishlist():
    if not wishlist:
        print("\nWishlist kosong.")
        return

    lihat_wishlist()

    try:
        pilihan = int(input("\nPilih nomor wishlist : ")) - 1

        if 0 <= pilihan < len(wishlist):
            item = wishlist.pop(pilihan)

            tambah_ke_pesanan(
                item['nama'],
                item['harga'],
                item['qty']
            )
        else:
            print("❌ Nomor tidak valid.")

    except ValueError:
        print("❌ Masukkan angka yang benar.")


# =====================================
# DATABASE MENU MAKANAN
# =====================================
makanan_db = {
    "1": ("Nasi Goreng", 15000),
    "2": ("Mie Goreng", 14000),
    "3": ("Beef Aussie Rice Bowl", 45000),
    "4": ("Chicken Steak Crispy", 38500),
    "5": ("Salmon Mentai Rice", 63000),
    "6": ("Salted Egg Chicken Rice Bowl", 29000),
    "7": ("Nasi Telur Dadar", 10000),
    "8": ("Ramen Enoboruki", 37000),
    "9": ("Sushi Salmon Mix Beef Spicy", 64800),
    "10": ("Rice Bowl Ayam Bakar Madu", 29000),
    "11": ("Caribbean Chicken Steak", 89000),
    "12": ("Mentai Fish Baked Rice With Mushroom", 50000),
    "13": ("Chicken Cordon Blue", 61450),
    "14": ("Fish And Chips", 46000),
    "15": ("Wagyu Steak", 189000)
}


# =====================================
# MENU MAKANAN
# =====================================
def menu_makanan():
    print("\n" + "=" * 45)
    print("             MENU MAKANAN")
    print("=" * 45)

    for kode, item in makanan_db.items():
        print(f"{kode:<3} {item[0]:<38} Rp{item[1]:>8,}")

    pilihan = input("\nPilih makanan : ")

    if pilihan in makanan_db:
        nama, harga = makanan_db[pilihan]

        qty = int(input(f"Jumlah {nama} : "))

        print("\n1. Pesan Sekarang")
        print("2. Tambahkan ke Wishlist")

        aksi = input("Pilih aksi : ")

        if aksi == "1":
            tambah_ke_pesanan(nama, harga, qty)

        elif aksi == "2":
            tambah_ke_wishlist(nama, harga, qty)

        else:
            print("❌ Pilihan tidak valid.")

    else:
        print("❌ Menu tidak tersedia.")


# =====================================
# MENU DESSERT
# =====================================
def menu_dessert():
    dessert_db = {
        "1": ("Ice Cream", 10000),
        "2": ("Pudding", 8000)
    }

    print("\n===== MENU DESSERT =====")

    for kode, item in dessert_db.items():
        print(f"{kode:<3} {item[0]:<25} Rp{item[1]:>8,}")

    pilihan = input("Pilih dessert : ")

    if pilihan in dessert_db:
        nama, harga = dessert_db[pilihan]

        qty = int(input(f"Jumlah {nama} : "))

        print("\n1. Pesan Sekarang")
        print("2. Tambahkan ke Wishlist")

        aksi = input("Pilih aksi : ")

        if aksi == "1":
            tambah_ke_pesanan(nama, harga, qty)

        elif aksi == "2":
            tambah_ke_wishlist(nama, harga, qty)

        else:
            print("❌ Aksi tidak valid.")

    else:
        print("❌ Pilihan tidak valid.")


# =====================================
# MENU CEMILAN
# =====================================
def menu_cemilan():
    cemilan_db = {
        "1": ("Kentang Goreng", 12000),
        "2": ("Nugget", 13000)
    }

    print("\n===== MENU CEMILAN =====")

    for kode, item in cemilan_db.items():
        print(f"{kode:<3} {item[0]:<25} Rp{item[1]:>8,}")

    pilihan = input("Pilih cemilan : ")

    if pilihan in cemilan_db:
        nama, harga = cemilan_db[pilihan]

        qty = int(input(f"Jumlah {nama} : "))

        print("\n1. Pesan Sekarang")
        print("2. Tambahkan ke Wishlist")

        aksi = input("Pilih aksi : ")

        if aksi == "1":
            tambah_ke_pesanan(nama, harga, qty)

        elif aksi == "2":
            tambah_ke_wishlist(nama, harga, qty)

        else:
            print("❌ Aksi tidak valid.")

    else:
        print("❌ Pilihan tidak valid.")


# =====================================
# DATABASE MENU MINUMAN
# =====================================
MENU_LENGKAP = {
    "ICE": {
        "Lemon Tea": 5000,
        "Lychee Tea": 7000,
        "Peach Tea": 15000,
        "Jasmine Tea": 12000,
        "Green Tea": 10000,
        "Yakult Drink": 15000,
        "Soda Gembira": 15000,
        "Blue Ocean": 15000,
        "Mojito": 15000,
        "Thai Tea": 15000,
        "Taro Drink": 15000
    },

    "HOT": {
        "Tea Original": 8000,
        "Green Tea": 12000,
        "Ginger Tea": 10000,
        "Lemon Tea": 12000
    },

    "MILK": {
        "Fresh Milk Original": 12000,
        "Strawberry Milk": 15000,
        "Chocolate Milk": 15000,
        "Matcha Milk": 15000,
        "Taro Milk": 15000,
        "Vanilla Milk": 15000,
        "Banana Milk": 15000,
        "Caramel Milk": 15000,
        "Oreo Milk": 15000
    },

    "COFFEE": {
        "Expresso": 15000,
        "Americano": 17000,
        "Cappuccino": 20000,
        "Cafe Latte": 18000,
        "Vanilla Latte": 18000,
        "Caramel Latte": 18000,
        "Hazelnut Latte": 20000,
        "Mochaccino": 20000,
        "Affogato": 19000
    }
}


# =====================================
# MENU MINUMAN
# =====================================
def menu_minuman():
    kategori_list = list(MENU_LENGKAP.keys())

    print("\n===== MENU MINUMAN =====")

    for i, kategori in enumerate(kategori_list, 1):
        print(f"{i}. {kategori}")

    try:
        pilih_kategori = int(input("\nPilih kategori : ")) - 1

        nama_kategori = kategori_list[pilih_kategori]
        submenu = MENU_LENGKAP[nama_kategori]

        print(f"\n--- {nama_kategori} ---")

        item_list = list(submenu.keys())

        for j, item in enumerate(item_list, 1):
            print(f"{j:<3} {item:<30} Rp{submenu[item]:>8,}")

        pilih_item = int(input("\nPilih menu : ")) - 1

        nama_produk = item_list[pilih_item]
        harga_produk = submenu[nama_produk]

        qty = int(input(f"Jumlah {nama_produk} : "))

        print("\n1. Pesan Sekarang")
        print("2. Tambahkan ke Wishlist")

        aksi = input("Pilih aksi : ")

        if aksi == "1":
            tambah_ke_pesanan(nama_produk, harga_produk, qty)

        elif aksi == "2":
            tambah_ke_wishlist(nama_produk, harga_produk, qty)

        else:
            print("❌ Pilihan tidak valid.")

    except:
        print("❌ Input salah.")


# =====================================
# PAYMENT
# =====================================
def payment():
    global total_harga

    if not pesanan:
        print("\nBelum ada pesanan.")
        return

    print("\n" + "=" * 55)
    print("                STRUK PEMBELIAN")
    print("=" * 55)

    print(f"Nama Pelanggan : {nama_pelanggan}")
    print(f"Tipe Pesanan   : {tipe_pesanan}")

    print("-" * 55)
    print(f"{'Menu':<30}{'Qty':<8}{'Subtotal'}")
    print("-" * 55)

    for item in pesanan:
        print(f"{item['nama']:<30}{item['qty']:<8}Rp{item['subtotal']:>10,}")

    print("-" * 55)
    print(f"TOTAL BAYAR : Rp{total_harga:,}")

    uang = int(input("\nMasukkan uang pembayaran : Rp"))

    if uang >= total_harga:
        kembalian = uang - total_harga

        print(f"Kembalian : Rp{kembalian:,}")
        print("\n✨ Terima kasih telah berkunjung ✨")

    else:
        print("❌ Uang tidak cukup.")


# =====================================
# MENU UTAMA
# =====================================
def menu_utama():
    while True:
        print("\n" + "=" * 45)
        print("              MENU UTAMA")
        print("=" * 45)

        print("1. Daftar Makanan")
        print("2. Daftar Minuman")
        print("3. Dessert")
        print("4. Cemilan")
        print("5. Lihat Wishlist")
        print("6. Pesan dari Wishlist")
        print("7. Payment")

        pilihan = input("\nPilih menu : ")

        if pilihan == "1":
            menu_makanan()

        elif pilihan == "2":
            menu_minuman()

        elif pilihan == "3":
            menu_dessert()

        elif pilihan == "4":
            menu_cemilan()

        elif pilihan == "5":
            lihat_wishlist()

        elif pilihan == "6":
            pindah_dari_wishlist()

        elif pilihan == "7":
            payment()
            break

        else:
            print("❌ Pilihan tidak valid.")


# =====================================
# PROGRAM UTAMA
# =====================================
def main():
    input_pelanggan()
    menu_utama()


main()