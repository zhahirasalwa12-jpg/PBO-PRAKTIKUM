# models/produk.py

# Parent Class
class Produk:
    def __init__(self, nama, harga, stok):
        self.__nama = nama
        self.__harga = harga
        self.__stok = stok

    # Getter dan Setter (enkapsulasi)
    def get_nama(self):
        return self.__nama

    def get_harga(self):
        return self.__harga

    def get_stok(self):
        return self.__stok

    def set_harga(self, harga_baru):
        if harga_baru > 0:
            self.__harga = harga_baru
        else:
            print("Harga tidak valid!")

    def kurangi_stok(self, jumlah):
        if jumlah <= self.__stok:
            self.__stok -= jumlah
        else:
            print(f"Stok {self.__nama} tidak mencukupi.")

    def tambah_stok(self, jumlah):
        self.__stok += jumlah

    def tampilkan_info(self):
        return f"Produk: {self.__nama}, Harga: Rp{self.__harga}, Stok: {self.__stok}"


# Child Class (Inheritance & Polymorphism)
class ProdukElektronik(Produk):
    def __init__(self, nama, harga, stok, garansi):
        super().__init__(nama, harga, stok)
        self.garansi = garansi

    def tampilkan_info(self):  # Polymorphism
        return f"{super().tampilkan_info()}, Garansi: {self.garansi} tahun"
