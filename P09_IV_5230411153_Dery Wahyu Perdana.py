from abc import ABC, abstractmethod

class Makanan(ABC):
    @abstractmethod
    def pesan(self, nama_pelanggan, menu):
        pass

    @abstractmethod
    def biaya(self, jumlah):
        pass

class NasiGoreng(Makanan):
    harga_per_porsi = 20000

    def pesan(self, nama_pelanggan, menu):
        print(f"{nama_pelanggan} telah memesan {menu}")

    def biaya(self, jumlah):
        if jumlah < 1:
            raise ValueError("Pesanan gagal: jumlah porsi minimal 1")
        return self.harga_per_porsi * jumlah

class MieGoreng(Makanan):
    harga_per_porsi = 15000

    def pesan(self, nama_pelanggan, menu):
        print(f"{nama_pelanggan} telah memesan {menu}")

    def biaya(self, jumlah):
        if jumlah < 1:
            raise ValueError("Pesanan gagal: jumlah porsi minimal 1")
        return self.harga_per_porsi * jumlah

def main():
    try:
        nasi_goreng = NasiGoreng()
        mie_goreng = MieGoreng()

        while True:
            nama_pelanggan = input("Masukkan nama pelanggan: ")
            menu = input("Masukkan menu (Nasi Goreng/Mie Goreng): ")
            jumlah = float(input("Masukkan jumlah porsi: "))

            try:
                if jumlah < 1:
                    raise ValueError("Pesanan gagal: jumlah porsi minimal 1")

                if menu.lower() == "nasi goreng":
                    nasi_goreng.pesan(nama_pelanggan, menu)
                    print(f"Biaya: Rp{nasi_goreng.biaya(jumlah)}")
                elif menu.lower() == "mie goreng":
                    mie_goreng.pesan(nama_pelanggan, menu)
                    print(f"Biaya: Rp{mie_goreng.biaya(jumlah)}")
                else:
                    print("Menu tidak tersedia")
                    continue

                uang_dibayar = int(input("Masukkan jumlah uang yang dibayarkan: Rp "))
                if menu.lower() == "nasi goreng":
                    total_biaya = nasi_goreng.biaya(jumlah)
                elif menu.lower() == "mie goreng":
                    total_biaya = mie_goreng.biaya(jumlah)

                if uang_dibayar < total_biaya:
                    print("Uang yang dibayarkan tidak cukup")
                else:
                    kembalian = uang_dibayar - total_biaya
                    print(f"Pembayaran berhasil. Kembalian: Rp{kembalian}")

            except ValueError as e:
                print(e)

            lanjut = input("Apakah Anda ingin memesan lagi? (ya/tidak): ")
            if lanjut.lower() != "ya":
                print("Terima kasih telah memesan!")
                break

    except ValueError as e:
        print(e)

    def cetak_struk(nama_pelanggan, menu, jumlah, total_biaya, uang_dibayar, kembalian):
        print("\n===== STRUK PEMESANAN =====")
        print(f"Nama Pelanggan : {nama_pelanggan}")
        print(f"Menu           : {menu}")
        print(f"Jumlah Porsi   : {jumlah}")
        print(f"Total Biaya    : Rp{total_biaya}")
        print(f"Uang Dibayar   : Rp{uang_dibayar}")
        print(f"Kembalian      : Rp{kembalian}")
        print("==========================\n")

    # Call cetak_struk function after successful payment
    cetak_struk(nama_pelanggan, menu, jumlah, total_biaya, uang_dibayar, kembalian)

if __name__ == "__main__":
    main()