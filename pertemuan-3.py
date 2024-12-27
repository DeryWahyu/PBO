# print("==================================================")
# suhu = float(input("Masukkan suhu dalam derajat Celsius : "))

# if suhu > 30:
#     print("Suhu tersebut panas.")
# elif 15 <= suhu <= 30:
#     print("Suhu tersebut sejuk.")
# else:
#     print("Suhu tersebut dingin.")
# print("==================================================")

# print("Soal 1")
# angka = float(input("Masukkan angka : "))

# if angka > 10:
#     print("Angka Besar")
# else:
#     print("Angka Kecil")

# print("\nSoal 2")
# angka = int(input("Masukkan angka : "))

# if angka % 2 == 0:
#     print("Angka Genap")
# else:
#     print("Angka Ganjil")

# print("\nSoal 3")
# angka = int(input("Masukkan angka : "))

# if angka > 0:
#     print("Bilangan Positif")
# elif angka < 0:
#     print("Bilangan Negatif")
# else:
#     print("Nol")

# print("\nSoal 4")
# nilai = float(input("Masukkan nilai akhir mahasiswa: "))

# if nilai >= 81:
#     print("Lulus dengan nilai A")
# elif nilai >= 61:
#     print("Lulus dengan nilai B")
# else:
#     print("Tidak lulus")

# print("\nSoal 5")
# angka1 = int(input("Masukkan angka pertama: "))
# angka2 = int(input("Masukkan angka kedua: "))

# if (angka1 > 50 and angka2 < 10) or (angka1 < 10 and angka2 > 50):
#     print("Salah satu angka lebih besar dari 50 dan yang lain lebih kecil dari 10")
# else:
#     print("Kondisi tidak terpenuhi")

# print("\nSoal 6")
# nama_pengguna = input("Masukkan nama pengguna: ")

# if nama_pengguna.lower() == "admin":
#     print("Selamat datang Admin")
# else:
#     print(f"Hallo pengguna {nama_pengguna}")

# print("\nSoal 7")
# while True:
#     karakter = input("Masukkan satu karakter: ").lower()

#     if len(karakter) == 1:
#         if karakter.isalpha():
#             if karakter in 'aeiou':
#                 print("Karakter tersebut adalah huruf vokal.")
#             else:
#                 print("Karakter tersebut adalah huruf konsonan.")
#             break
#         else:
#             print("Karakter yang dimasukkan bukan huruf. Coba lagi.")
#     else:
#         print("Masukkan hanya satu karakter. Coba lagi.")

# print("\nSoal 8")
# usia = int(input("Masukkan usia: "))

# if usia < 13:
#     print("Anak-anak")
# elif 13 <= usia <= 19:
#     print("Remaja")
# elif 20 <= usia <= 65:
#     print("Dewasa")
# else:
#     print("Lansia")

print("\nSoal 9")
jumlah_belanja = float(input("Masukkan jumlah belanja: "))

if jumlah_belanja > 1000000:
    diskon = 0.10
    strdiskon = "10%"
else:
    diskon = 0.05
    strdiskon = "5%"

jumlah_diskon = jumlah_belanja * diskon
total_bayar = jumlah_belanja - jumlah_diskon

print(f"Diskon: {strdiskon} : Rp {int(jumlah_diskon)}")
print(f"Total yang harus dibayar: Rp {int(total_bayar)}")

# print("\nSoal 10")
# angka1 = float(input("Masukkan angka pertama: "))
# angka2 = float(input("Masukkan angka kedua: "))
# angka3 = float(input("Masukkan angka ketiga: "))

# if angka1 >= angka2 and angka1 >= angka3:
#     terbesar = angka1
# elif angka2 >= angka1 and angka2 >= angka3:
#     terbesar = angka2
# else:
#     terbesar = angka3

# print(f"Angka terbesar adalah: {terbesar}")

print("\nSoal 11")



# angka = 1
# while angka <= 5:
#     print(f"angka ke {angka}")
#     angka += 1