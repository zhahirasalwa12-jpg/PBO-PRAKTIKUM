<<<<<<< HEAD
# diskon_service.py (VERSI FINAL - BUG PPN SUDAH DIPERBAIKI)

import pdb


class DiskonCalculator:
    """Menghitung harga akhir setelah diskon."""

    def hitung_diskon(self, harga_awal: float, persentase_diskon: int) -> float:
        # Perhitungan Diskon
        jumlah_diskon = harga_awal * persentase_diskon / 100
        harga_akhir = harga_awal - jumlah_diskon

        # !!! BUG PPN 10% SUDAH DIHAPUS DARI SINI !!!

        return harga_akhir  # Sekarang mengembalikan harga akhir yang benar
=======
# diskon_service.py (VERSI FINAL - BUG PPN SUDAH DIPERBAIKI)

import pdb


class DiskonCalculator:
    """Menghitung harga akhir setelah diskon."""

    def hitung_diskon(self, harga_awal: float, persentase_diskon: int) -> float:
        # Perhitungan Diskon
        jumlah_diskon = harga_awal * persentase_diskon / 100
        harga_akhir = harga_awal - jumlah_diskon

        # !!! BUG PPN 10% SUDAH DIHAPUS DARI SINI !!!

        return harga_akhir  # Sekarang mengembalikan harga akhir yang benar
>>>>>>> 62723ba572f986321ceb1f39bc4fb779b6dc725a
