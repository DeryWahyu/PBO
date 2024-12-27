from abc import ABC, abstractmethod

# class Hewan(ABC):
#     @abstractmethod
#     def suara(self):
#         pass

# class Anjing(Hewan):
#     def suara(self):
#         return "Guk Guk"

# class Kucing(Hewan):
#     def suara(self):
#         return "Meong Meong"

# # Abstract class Hewan cannot be instantiated directly
# # so we remove the instantiation part

# anjing = Anjing()
# print(anjing.suara())

# kucing = Kucing()
# print(kucing.suara())

# class Kendaraan(ABC):
#     @abstractmethod
#     def bergerak(self):
#         pass

# class Mobil(Kendaraan):
#     def bergerak(self):
#         return "Mobil bergerak dengan roda empat"

# class Sepeda(Kendaraan):
#     def bergerak(self):
#         return "Sepeda bergerak dengan roda dua"

# mobil = Mobil()
# print(mobil.bergerak())

# sepeda = Sepeda()
# print(sepeda.bergerak())

# class Pegawai(ABC):
#     @abstractmethod
#     def tampilkan_deskripsi(self):
#         pass

# class Dosen(Pegawai):
#     def __init__(self, nama, np):
#         self.nama = nama
#         self.np = np

#     def tampilkan_deskripsi(self):
#         return f"Dosen : {self.nama}, NP : {self.np}"

# class StafAdministrasi(Pegawai):
#     def __init__(self, nama, id_staf):
#         self.nama = nama
#         self.id_staf = id_staf

#     def tampilkan_deskripsi(self):
#         return f"Staf Administrasi : {self.nama}, ID Staf : {self.id_staf}"

# dosen = Dosen("Dr. Budi", "123456")
# print(dosen.tampilkan_deskripsi())  

# staf = StafAdministrasi("Andi", "78910")
# print(staf.tampilkan_deskripsi())

# Sistem Penyewaan Kendaraan
class SewaKendaraan(ABC):
    @abstractmethod
    def biaya_sewa(self, durasi):
        pass

class Motor(SewaKendaraan):
    def biaya_sewa(self, durasi):
        return 100000 * durasi

class Bus(SewaKendaraan):
    def biaya_sewa(self, durasi):
        return 500000 * durasi

motor = Motor()
print("===================[ SEWA KENDARAAN ]===================")
print(f"=        Biaya sewa motor untuk 3 hari : Rp {motor.biaya_sewa(3)}     =")

bus = Bus()
print(f"=        Biaya sewa bus untuk 2 hari   : Rp {bus.biaya_sewa(2)}    =")
print("========================================================")

# Sistem Restorasi
class Menu(ABC):
    @abstractmethod
    def nama_menu(self):
        pass

    @abstractmethod
    def harga_menu(self):
        pass

class Minuman(Menu):
    def __init__(self, nama, harga):
        self.nama = nama
        self.harga = harga

    def nama_menu(self):
        return self.nama

    def harga_menu(self):
        return self.harga

class Makanan(Menu):
    def __init__(self, nama, harga):
        self.nama = nama
        self.harga = harga

    def nama_menu(self):
        return self.nama

    def harga_menu(self):
        return self.harga

minuman = Minuman("Es Teh", 5000)
print("\n===================[ SISTEM RESTORAN ]==================")
print(f"=        Menu: {minuman.nama_menu()}       -> Harga : Rp {minuman.harga_menu()}         =")

makanan = Makanan("Nasi Goreng", 15000)
print(f"=        Menu: {makanan.nama_menu()}  -> Harga : Rp {makanan.harga_menu()}        =")
print("========================================================")

# Sistem Reservasi Hotel
class Reservasi(ABC):
    @abstractmethod
    def buat_reservasi(self, nama, durasi):
        pass

class ReservasiKamar(Reservasi):
    def buat_reservasi(self, nama, durasi):
        print("\n==============[ SISTEM RESERVASI HOTEL ]================")
        return f"=   Reservasi kamar untuk {nama} selama {durasi} malam.         ="

class ReservasiRuangMeeting(Reservasi):
    def buat_reservasi(self, nama, durasi):
        return f"=   Reservasi ruang meeting untuk {nama} selama {durasi} jam.   ="

reservasi_kamar = ReservasiKamar()
print(reservasi_kamar.buat_reservasi("Dery", 3))

reservasi_ruang_meeting = ReservasiRuangMeeting()
print(reservasi_ruang_meeting.buat_reservasi("Dery", 5))
print("========================================================")