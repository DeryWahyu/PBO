# class Student:
#     def login(self, username, password=None):
#         if password:
#             return f";ogin dengan username dan password:{username}"
#         return f"Login dengan single sign on: {username}"

# student = Student()
# print(student.login("admin"))

# class Grade:
#     def addGrade(self, *args):
#         if len(args) == 1:
#             return f"menambahkan nilai : {args[0]}"
        
#         elif len(args) == 2:
#             return f"menambahkan nilai : {args[0]} dan {args[1]}"

# gradeManager = Grade()
# print(gradeManager.addGrade(85))

# class LibraryReservation:
#     def reservasiBook(self, *args):
#         if len(args) == 1:
#             return f"Reservasi buku dengan judul: {args[0]}"
#         elif len(args) == 2:
#             return f"Reservasi buku dengan judul: {args[0]} DI pinjam oleh {args[1]}"

# library = LibraryReservation()
# print(library.reservasiBook("Pemrograman Python"))
# print(library.reservasiBook("Pemrograman Python", "Dery"))

# class Store:
#     def purchaseItem(self, *args):
#         if len(args) == 1:
#             return f"Membeli produk dengan nama: {args[0]}"
#         elif len(args) == 2:
#             return f"Membeli produk dengan nama: {args[0]} dan jumlah: {args[1]}"

# store = Store()
# print(store.purchaseItem("Laptop"))
# print(store.purchaseItem("Laptop", 2))

