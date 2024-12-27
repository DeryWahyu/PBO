import sys

import my_library.capitallize
sys.path.append('D:/TUGAS KULIAH INFORMATIKA/SEMESTER 3/PBO/pertemuan-13/my_library')
print("Path yang digunakan: ", sys.path)  

#sekarang python dapat menemukan my_library yang berada didalam append
import my_library

#mengecek apakah "fungsi 'tambah' ada
print ("Apakah 'tambah' ada di my_library?", "tambah" in dir(my_library))

print(my_library.tambah(3, 4))
print(my_library.capitallize_first_letter("hello"))

print("Luas persegi adalah:", my_library.luas_persegi(5))
print("Keliling persegi adalah:", my_library.keliling_persegi(5))   