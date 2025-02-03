from abc import ABC, abstractmethod

class Deskripsi(ABC):
    @abstractmethod
    def tampilkan_deskripsi(self):
        pass

class Kendaraan(Deskripsi):
    def __init__(self, nama, tahun, nomor_registrasi, deskripsi):
        self.__nama = nama
        self.__tahun = tahun
        self.__nomor_registrasi = nomor_registrasi
        self.__deskripsi = deskripsi

    @abstractmethod
    def tampilkan_info(self):
        pass

    def tampilkan_deskripsi(self):
        print(f"{self.__deskripsi}")

    # Getter methods for private attributes
    def get_nama(self):
        return self.__nama

    def get_tahun(self):
        return self.__tahun

    def get_nomor_registrasi(self):
        return self.__nomor_registrasi

class Mobil(Kendaraan):
    def tampilkan_info(self):
        print(f"{self.get_nama()} ({self.get_tahun()})")
        print(f"Nomor Registrasi: {self.get_nomor_registrasi()}")
        self.tampilkan_deskripsi()
        print("-" * 40)

class Motor(Kendaraan):
    def tampilkan_info(self):
        print(f"{self.get_nama()} ({self.get_tahun()})")
        print(f"Nomor Registrasi: {self.get_nomor_registrasi()}")
        self.tampilkan_deskripsi()
        print("-" * 40)

class Truk(Kendaraan):
    def tampilkan_info(self):
        print(f"{self.get_nama()} ({self.get_tahun()})")
        print(f"Nomor Registrasi: {self.get_nomor_registrasi()}")
        self.tampilkan_deskripsi()
        print("-" * 40)

# Daftar kendaraan
daftar_kendaraan = [
    Mobil("Toyota Avanza", 2021, "B1234XYZ", "Mobil dengan kapasitas 7 penumpang."),
    Motor("Honda Supra", 2019, "B5678ABC", "Motor tipe bebek."),
    Truk("Hino Ranger", 2018, "B9876DEF", "Truk dengan kapasitas muatan 15 ton.")
]

# Menampilkan daftar kendaraan
print("Daftar Kendaraan Perusahaan LogistiCo:")
print("=" * 40)
for kendaraan in daftar_kendaraan:
    kendaraan.tampilkan_info()