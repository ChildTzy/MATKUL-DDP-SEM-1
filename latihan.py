
nama = "  Ragil setiawan  "
umur = "umur saya 19"
alamat = "saya tinggal dijakarta"
bool = "true"
list = " HAIII"
tinggi_badan = "tinggi saya 174.5"


#MODIFIKASI TIPE DATA STRING
print(nama.upper()) #mengubah string menjadi huruf besar
print(nama.lower()) #mengubah string menjadi huruf kecil
print(nama.capitalize()) #mengubah string menjadi huruf besar diawal kalimat
print(nama.split())#memisahkan string
print(" ".join(['Ragil','setiawan']))#menggabungkan string
print(nama.replace('Ragil','setiawan')) #mengganti string
print(nama.rstrip()) # hapus spasi kanan
print(nama.lstrip()) #hapus spasi kiri
print(f"nama {nama.strip()} dan umur saya {umur}" )
print(nama.strip()) # hapus spasi
print(nama.title())#mengubah string menjadi huruf besar diawal kata

#menulis teks ke file 
with open ("biodata.txt", "w") as file :
    file.write("hello world!\n")
    file.write("ini adalah baris kedua\n")

nama = input("nama: ")
# buka file untuk ditulis
nama= open("bioadata.txt", "w")
#tulis teks ke file
nama.write(nama)
#tutup file
nama.close()

#tentukan daftar string yang akan ditulis
text = ["ini baris pertama\n", "ini baris kedua\n", "baris ketiga\n"]
with open ('contoh_writelines.txt', 'w') as f :
    f.writelines(text)
print("Data berhasil ditulis ke dalam file contoh_writeline")

segitiga = 5

for i in range(1, segitiga + 1):
    print('*' * i) 


#PERTEMUAN KE 5 PENGONDISIAN 

a = 99
b = 89
c = 58

if b > a and b> c:
    print('b lebih besar dari a dan lebih dari c')

elif a > b and a > c:
    print ('a lebih besar dari b dan lebih dari c')

elif a == b and a == c:
    print('a sama dengan b dan sama dengan c') 

elif c > a and c > b:
    print('c lebih dari b dan lebih dari a') 

else :
    print('nilai tidak diketahui') 

# tanda penghubung hanya 2 yaitu ( or dan and )
#pengondisian bisa berapa saja asal terpenuhi


# FUNCTION

# def func_name(parameter):
#function (argument)

def hitung_luas_balok(alas, tinggi):
        luas= alas * tinggi + 50 / 2
        print (luas)

hitung_luas_balok(4, 5)
hitung_luas_balok(5, 6)
hitung_luas_balok(6, 7)


alas = 50
tinggi = 10 #Variabel global
def hitung_luas_balok():
        luas= alas * tinggi 
        print (luas)

hitung_luas_balok()
hitung_luas_balok()
hitung_luas_balok()


def hitung_luas_balok():
        alas = 50
        tinggi = 10 #Variabel lokal
        luas= alas * tinggi 
        print (luas)

hitung_luas_balok()
hitung_luas_balok()
hitung_luas_balok()


 # Fungsi rekursif untuk menghitung jumlah elemen list
def hitung_jumlah(data):
    # Basis: jika list kosong, jumlahnya 0
    if data == []:
        return 0
    else:
        # Rekurens: 1 + hitung sisanya
        return 1 + hitung_jumlah(data[1:])


# Input list dari pengguna
data = input("Masukkan elemen-elemen list (pisahkan dengan spasi): ").split()

# Hitung jumlah dengan rekursif
jumlah = hitung_jumlah(data)

print("Jumlah data dalam list:", jumlah)

#Latihan soal 
nama_user = input("Masukkan nama Anda: ")

def menu_utama():
    while True:
        print(f"\nHalo, {nama_user}! Selamat datang di program BIODATA MAHASISWA.") 
        print("Pilih Opsi:")
        print("1. Input data")
        print("2. Cek data")
        print("3. Keluar")

        pilihan = input("Masukkan pilihan Anda (1-3): ")

        # =======================
        # OPSI 1 : INPUT DATA
        # =======================
        if pilihan == "1":
            Nama = input("Nama Mahasiswa : ")
            NIM = input("NIM : ")
            ALAMAT = input("Alamat : ")
            TEMPAT_LAHIR = input("Tempat Lahir : ")
            TANGGAL_LAHIR = input("Tanggal Lahir : ")
            HOBBY = input("Hobby : ")
            CITA_CITA = input("Cita-cita : ")

            with open("biodata.txt", "w") as file:
                file.write("=========================\n")
                file.write(f"{Nama}\n")
                file.write(f"{NIM}\n")
                file.write(f"{ALAMAT}\n")
                file.write(f"{TEMPAT_LAHIR}\n")
                file.write(f"{TANGGAL_LAHIR}\n")
                file.write(f"{HOBBY}\n")
                file.write(f"{CITA_CITA}\n")

            print("\nData berhasil disimpan ke file biodata.txt!\n")

        # =======================
        # OPSI 2 : CEK DATA
        # =======================
        elif pilihan == "2":
            try:
                with open("biodata.txt", "r") as file:
                    data = file.readlines()

                print("\n=== DATA BIODATA MAHASISWA ===")
                print("Nama            :", data[1].strip())
                print("NIM             :", data[2].strip())
                print("Alamat          :", data[3].strip())
                print("Tempat Lahir    :", data[4].strip())
                print("Tanggal Lahir   :", data[5].strip())
                print("Hobby           :", data[6].strip())
                print("Cita-cita       :", data[7].strip())
                print()

            except FileNotFoundError:
                print("\nFile biodata.txt belum ada. Silakan input data dulu.\n")

        # =======================
        # OPSI 3 : KELUAR
        # =======================
        elif pilihan == "3":
            print("Program selesai. Terima kasih!")
            break

        else:
            print("Pilihan tidak valid, coba lagi.")

menu_utama()
      

def hitung_jumlah_data (data) :
    if data == [] :
        return 0
    else :
        return 1 + hitung_jumlah_data (data[1:])

data = input("MASUKAN DATA : ").split()
jumlah = hitung_jumlah_data(data)

print("JUMLAH DATA ADALAH : ", jumlah)




