import math

# Fungsi untuk mencari luas persegi panjang
def luas_persegi_panjang(panjang, lebar):
    return panjang*lebar
    
# Fungsi untuk mencari luas persegi
def luas_persegi(sisi):
    return sisi*sisi

# Fungsi untuk mencari luas segitiga
def luas_segitiga(alas, tinggi):
    return 0.5*alas*tinggi

# Fungsi untuk mencari luas trapesium
def luas_trapesium(sisi_atas, sisi_bawah, tinggi):
    return 0.5 * (sisi_atas + sisi_bawah)*tinggi

nama_user = input("Masukkan nama Anda: ")

def menu_utama():
    print(f"\nHalo, {nama_user}! Selamat datang di program perhitungan bangun ruang.")
    print("Pilih bangun ruang yang ingin Anda hitung:")
    print("1. persegi panjang")
    print("2. persegi")
    print("3. segitiga")
    print("4. trapesium")
    print("5. Keluar")

    pilihan = input("Masukkan pilihan Anda (1-5): ")

    if pilihan == '1':
        panjang = float(input("Masukkan panjang persegi panjang: "))
        lebar = float(input("Masukkan lebar persegi panjang: "))
        luas = luas_persegi_panjang(panjang, lebar)
        print(f"Luas persegi panjang adalah: {luas:.2f}")

    elif pilihan == '2':
        sisi = float(input("Masukkan panjang sisi persegi: "))
        luas = luas_persegi(sisi)
        print(f"Luas persegi adalah: {luas:.2f}")

    elif pilihan == '3':
        alas = float(input("Masukkan alas segitiga: "))
        tinggi = float(input("Masukkan tinggi segitiga: "))
        luas = luas_segitiga(alas, tinggi)
        print(f"Luas segitiga adalah: {luas:.2f}")

    elif pilihan == '4':
        sisi_atas = float(input("Masukkan panjang sisi atas trapesium: "))
        sisi_bawah = float(input("Masukkan panjang sisi bawah trapesium: "))
        tinggi = float(input("Masukkan tinggi trapesium: "))
        luas = luas_trapesium(sisi_atas, sisi_bawah, tinggi)
        print(f"Luas trapesium adalah: {luas:.2f}")

    elif pilihan == '7':
        print("Program selesai. Sampai jumpa!")
        return False
    else:
        print (f"pilihan tidak valid")


while True:
    if not menu_utama():  # kalau user pilih 5 (Keluar), fungsi return False
        break
    
    lanjut = input("\nApakah ingin menghitung lagi? (y/n): ")
    if lanjut.lower() != 'y':
        print("Program selesai. Sampai jumpa!")
        break



