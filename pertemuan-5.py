# class Mahasiswa:
#     def __init__(self, nama, nim, jurusan):
#         self.__nama = nama
#         self.__nim = nim
#         self.__jurusan = jurusan

#     def tampilan(self):
#         print("Nama : ", self.__nama)
#         print("NIM : ", self.__nim)
#         print("Jurusan : ", self.__jurusan)

# # def getNama(self):
# #     return self.nama

# # def setNama(self, nama):
# #     self.nama = nama

# # def getNim(self):
# #     return self.nim

# # def setNim(self, nim):
# #     self.nim = nim

# # def getJurusan(self):
# #     return self.jurusan

# # def setJurusan(self, jurusan):
# #     self.jurusan = jurusan

# mhs = Mahasiswa("Budi", "123456", "Teknik Informatika")
# mhs.tampilan()

# class Pasien:
#     def __init__(self, nama, idPasien, penyakit):
#         self.__nama = nama
#         self.__idPasien = idPasien
#         self.__penyakit = penyakit

#     def getNama(self):
#         return self.__nama
     
#     def setNama(self, nama):
#         self.__nama = nama
    
#     def getIdPasien(self):
#         return self.__idPasien
    
#     def setIdPasien(self, idPasien):
#         self.__idPasien = idPasien

#     def getPenyakit(self):
#         return self.__penyakit
    
#     def setPenyakit(self, penyakit):
#         self.__penyakit = penyakit

#     def tampilan(self):
#         print("Nama : ", self.__nama)
#         print("ID Pasien : ", self.__idPasien)
#         print("Penyakit : ", self.__penyakit)

# pasien = Pasien("Budi", "123456", "Demam")
# pasien.tampilan()
# pasien.setNama("Andi")
# pasien.setIdPasien("654321")
# pasien.setPenyakit("Flu")
# pasien.tampilan()

class Dosen:
    def __init__(self, nama, nidn, mata_kuliah):
        self.__nama = nama
        self.__nidn = nidn
        self.__mata_kuliah = mata_kuliah

    def getNama(self):
        return self.__nama

    def setNama(self, nama):
        self.__nama = nama

    def getNidn(self):
        return self.__nidn

    def setNidn(self, nidn):
        self.__nidn = nidn

    def getMataKuliah(self):
        return self.__mata_kuliah

    def setMataKuliah(self, mata_kuliah):
        self.__mata_kuliah = mata_kuliah

    def tampilan(self):
        print("Nama : ", self.__nama)
        print("NIDN : ", self.__nidn)
        print("Mata Kuliah : ", self.__mata_kuliah)

dosen = Dosen("Dr. Ahmad Siti", "987654", "Pemrograman Dasar")
dosen.tampilan()
dosen.setNama("Dr. Ahmad")
dosen.setNidn("123789")
dosen.setMataKuliah("Pemrograman Berorientasi Objek")
dosen.tampilan()

