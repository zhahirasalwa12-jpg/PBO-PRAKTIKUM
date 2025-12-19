# models/transaksi.py

class Transaksi:
    def __init__(self, pelanggan):
        self.pelanggan = pelanggan
        self.total = 0

    def proses_pembelian(self):
        print(f"\nMemproses transaksi untuk {self.pelanggan.nama}...")
        for produk, jumlah in self.pelanggan.keranjang:
            produk.kurangi_stok(jumlah)
            subtotal = produk.get_harga() * jumlah
            self.total += subtotal
            print(f"{produk.get_nama()} x{jumlah} = Rp{subtotal}")
        print(f"Total Pembayaran: Rp{self.total}")
        self.pelanggan.keranjang.clear()
