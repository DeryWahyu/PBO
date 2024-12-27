# class Hewan:
#     def __init__(self, nama):
#         self.nama = nama
    
#     def Bergerak(self):
#         print(f"{self.nama} Bergerak")

# class Burung(Hewan):
#     def Terbang(self):
#         print(f"{self.nama} Terbang")


# hewan = Hewan("Kucing")
# hewan.Bergerak()

# burung = Burung("Elang")
# burung.Bergerak()
# burung.Terbang()

# class A:
#     def methodA(self):
#         print("\nMetode A")

# class B:
#     def methodB(self):
#         print("Metode B")

# class C(A, B):
#     pass

# objek = C()
# objek.methodA()
# objek.methodB()

# class Hewan:
#     def Suara(self):
#         print("\nHewan membuat suara")

# class Kucing(Hewan):
#     def Suara(self):
#         print("Meong")

# class Kucing(Hewan):
#     def Suara(self):
#         super().Suara()
#         print("Kucing mengeong")

# kucing = Kucing()
# kucing.Suara()

# class Kendaraan:
#     def __init__(self, merk):
#         self.merk = merk

#     def Bergerak(self):
#         print(f"{self.merk} Bergerak dijalan")

# class Mobil(Kendaraan):
#     def Bergerak(self):
#         print(f"\n{self.merk} Bergerak dengan kecepatan tinggi")

# mobil = Mobil("Toyota")
# mobil.Bergerak()


# class Kendaraan:
#     def __init__(self, merk, model):
#         self.merk = merk
#         self.model = model

#     def infoKendaraan(self):
#         print(f"\n{self.merk} {self.model}")

# class Mobil(Kendaraan):
#     def __init__(self, merk, model, jumlahPintu):
#         super().__init__(merk, model)
#         self.jumlahPintu = jumlahPintu

#     def infoMobil(self):
#         print(f"{self.merk} {self.model} dengan {self.jumlahPintu} Pintu")

# mobil = Mobil("Toyota", "Avanza", 4)
# mobil.infoKendaraan()
# mobil.infoMobil()

# class Elektronik:
#     def nyalakan(self):
#         print("Perangkat dinyalakan")

# class Televisi(Elektronik):
#     def nyalakan(self):
#         super().nyalakan()

# tv = Televisi()
# tv.nyalakan()

# class Pelajar:
#     def belajar(self):
#         print("Pelajar sedang belajar")

# class Atlet:
#     def latihan(self):
#         print("Atlet sedang latihan")

# class PelajarAtlet(Pelajar, Atlet):
#     pass

# pelajar_atlet = PelajarAtlet()
# pelajar_atlet.belajar()
# pelajar_atlet.latihan()


class Guest:
    def __init__(self, name):
        self.name = name

    def browse_system(self):
        print(f"{self.name} sedang menjelajahi sistem")

    def access(self):
        print(f"{self.name} sedang mengakses sistem sebagai tamu")

class User(Guest):
    def __init__(self, name):
        super().__init__(name)

    def use_system(self):
        print(f"{self.name} sedang menggunakan sistem")

class Admin(Guest):
    def __init__(self, name):
        super().__init__(name)

    def manage_system(self):
        print(f"{self.name} sedang mengelola sistem")

    def access(self):
        print(f"{self.name} sedang mengakses sistem sebagai admin")

class SuperUser(Admin, User):
    def __init__(self, name):
        Admin.__init__(self, name)
        User.__init__(self, name)

    def super_use(self):
        print(f"{self.name} memiliki hak istimewa super user")

super_user = SuperUser("Wahyu")
super_user.access()