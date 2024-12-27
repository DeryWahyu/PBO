import psycopg2 
# koneksi ke database PostgreSQL
try:
    connection = psycopg2.connect(
        dbname = "uty1",
        user = "postgres",
        password = "admin",
        host = "localhost",
        port = "5432"
    )
    cursor = connection.cursor()
    print("Koneksi database ke PostgreSQL berhasil")
    
    # eksekusi query : menampilkan data dari tabel mahasiswa
    query = "SELECT * FROM mahasiswa"
    cursor.execute(query)
    rows = cursor.fetchall()
    for row in rows:
        print("=====================================")
        print("NIM: ", row[0])
        print("Nama: ", row[1])
        print("Jurusan: ", row[2])
        print("Alamat: ", row[3])
        print("=====================================")
        
except Exception as e:
    print(f"Terjadi kesalahan: {e}")
    
finally:
    if connection:
        cursor.close()
        connection.close()
        print("Koneksi postgreSQL ditutup")

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
import psycopg2

class DatabaseApp(App):
    def build(self):
        self.layout = BoxLayout(orientation = "vertical", spacing=10)
        
        # input
        self.nama_input = TextInput(hint_text="Nama Mahasiswa")
        self.jurusan_input = TextInput(hint_text="Jurusan")
        self.angkatan_input = TextInput(hint_text="Angkatan", input_filter="int")
        
        # button
        self.add_button = Button(text="Tambah Data", on_press=self.add_data)
        self.show_button = Button(text="Tampilkan Data", on_press=self.show_data)
        
        # output
        self.output_label = Label(size_hint_y=None, height=200)
        
        self.layout.add_widget(self.nama_input)
        self.layout.add_widget(self.jurusan_input)
        self.layout.add_widget(self.angkatan_input)
        self.layout.add_widget(self.add_button)
        self.layout.add_widget(self.show_button)
        self.layout.add_widget(self.output_label)
        
        return self.layout
    
    def connect_db(self):
        try:
            connection = psycopg2.connect(
                host = "localhost",
                dbname = "uty1",
                user = "postgres",
                password = "admin"
            )

            return connection
        except Exception as e:
            self.output_label.text = f"Terjadi kesalahan: {e}"

    def add_data(self, instance):
        conn = self.connect_db()
        if conn:
            cursor = conn.cursor()
            try :
                cursor.execute("INSERT INTO mahasiswa(nama, jurusan, angkatan) VALUES(%s, %s, %s)", 
                               (self.nama_input.text, self.jurusan_input.text, self.angkatan_input.text))
                conn.commit()
                self.output_label.text = "Data berhasil ditambahkan" 
            except Exception as e:
                self.output_label.text = f"Terjadi kesalahan: {e}"
            finally:
                cursor.close()
                conn.close()


    def show_data(self, instance):
        conn = self.connect_db()
        if conn:
            cursor = conn.cursor()
            try:
                cursor.execute("SELECT * FROM mahasiswa")
                rows = cursor.fetchall()
                result = "\n".join([f"{row[0]} {row[1]} {row[2]} {row[3]}" for row in rows])
                self.output_label.text = result
            except Exception as e:
                self.output_label.text = f"Terjadi kesalahan: {e}"
            finally:
                cursor.close()
                conn.close()

DatabaseApp().run()