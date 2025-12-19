# models/pelanggan.py

class Pelanggan:
    def __init__(self, nama):
        self.nama = nama
        self.keranjang = []

    def tambah_ke_keranjang(self, produk, jumlah):
        if produk.get_stok() >= jumlah:
            self.keranjang.append((produk, jumlah))
            print(f"{self.nama} menambahkan {jumlah} {produk.get_nama()} ke keranjang.")
        else:
            print(f"Stok {produk.get_nama()} tidak mencukupi untuk dimasukkan ke keranjang.")

    def tampilkan_keranjang(self):
        print(f"\nKeranjang {self.nama}:")
        for produk, jumlah in self.keranjang:
            print(f"- {produk.get_nama()} x{jumlah}")
