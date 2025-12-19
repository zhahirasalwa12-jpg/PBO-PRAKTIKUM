from models.produk import Produk, ProdukElektronik
from models.pelanggan import Pelanggan
from models.transaksi import Transaksi

if __name__ == "__main__":
    # Membuat produk
    laptop = ProdukElektronik("Laptop Asus", 9000000, 5, 2)
    hp = ProdukElektronik("HP Samsung", 4000000, 10, 1)
    buku = Produk("Buku Python", 150000, 20)

    # Menampilkan info produk
    print(laptop.tampilkan_info())
    print(hp.tampilkan_info())
    print(buku.tampilkan_info())

    # Membuat pelanggan
    pelanggan1 = Pelanggan("Icha")

    # Pelanggan menambahkan produk ke keranjang
    pelanggan1.tambah_ke_keranjang(laptop, 1)
    pelanggan1.tambah_ke_keranjang(buku, 2)
    pelanggan1.tampilkan_keranjang()

    # Proses transaksi
    transaksi1 = Transaksi(pelanggan1)
    transaksi1.proses_pembelian()

    # Cek stok setelah transaksi
    print("\nStok setelah pembelian:")
    print(laptop.tampilkan_info())
    print(buku.tampilkan_info())
