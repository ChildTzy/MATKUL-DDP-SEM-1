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
