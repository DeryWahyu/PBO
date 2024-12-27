#1
import openpyxl
workbook = openpyxl.Workbook()
sheet = workbook.active

sheet.title = "Mahasiswa"
sheet.append(["ID", "Nama", "Nilai"])
sheet.append(["1", "Yanto", 90])
sheet.append(["2", "Yanti", "75"])

workbook.save("Data Mahasiswa.xlsx")
print("Data Berhasil Disimpan")


#2
import psycopg2
import pandas as pd

def export_mhs():
    conn = psycopg2.connect(
        host = 'localhost',
        database = 'uty3',
        user = 'postgres',
        password = 'admin'
    )

    query = "SELECT * FROM mahasiswa"
    df = pd.read_sql_query(query, conn)
    df.to_excel('Mahasiswa.xlsx', index=False)
    conn.close()
    print("Data Berhasil Di ekspor ke dalam bentuk excel")

export_mhs()

#3
import psycopg2
import openpyxl
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput

class databaseManager:
    def __init__(self, host, database, user, password):
        try:
            self.conn = psycopg2.connect(
                host=host, database=database, user=user, password=password
            )
            self.cursor = self.conn.cursor()
            print("Koneksi Ke database berhasil")
        except Exception as e:
            print("Koneksi Ke database gagal")

    def getMahasiswa(self):
        try:
            self.cursor.execute("SELECT * FROM mahasiswa")
            data = self.cursor.fetchall()
            return data
        except Exception as e:
            print("Gagal mengambil data mahasiswa")
            return []

    def close(self):
        try:
            self.cursor.close()
            self.conn.close()
            print("Koneksi kedatabase berhasil di tutup")
        except Exception as e:
            print("Koneksi kedatabase gagal di tutup")

class excelReport:
    def __init__(self, filename):
        self.filename = filename

    def generateReport(self, data):
        try:
            workbook = openpyxl.Workbook()
            sheet = workbook.active
            sheet.title = "Laporan Mahasiswa"

            # Menambahkan Header
            sheet.append(["ID", "Nama", "Npm", "Jurusan"])
            for row in data:
                sheet.append(row)

            # Menyimpan file excel
            workbook.save(self.filename)
            print(f"Laporan berhasil di disimpan di {self.filename}")
        except Exception as e:
            print(f"Gagal membuat laporan {e}")


class reportApp(App):
    def build(self):
        self.db_manager = databaseManager('localhost', 'uty3', 'postgres', 'admin')
        data_mahasiswa = self.db_manager.getMahasiswa()
        self.db_manager.close()

        layout = BoxLayout(orientation='vertical')
        self.label = Label(text='Pembuatan Laporan Mahasiswa Berbasis Excel', size_hint_y = None, height=40)
        self.create_report_button = Button(text='Buat Laporan', size_hint_y =None, height =100)
        self.create_report_button.bind(on_press=self.createReport)

        layout.add_widget(self.label)
        layout.add_widget(self.create_report_button)
        return layout

    def createReport(self, instance):
        self.db_manager = databaseManager('localhost', 'uty3', 'postgres', 'admin')
        data_mahasiswa = self.db_manager.getMahasiswa()
        self.db_manager.close()

        excel_report = excelReport('Laporan Mahasiswa.xlsx')
        excel_report.generateReport(data_mahasiswa)
        self.label.text = "Laporan Excel Berhasil Di buat!"
if __name__ == '__main__':
    reportApp().run()