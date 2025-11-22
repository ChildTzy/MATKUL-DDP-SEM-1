#PENJUMLAHAN
def tambah (*angka):
    hasil = angka [0]
    for i in angka [1:]:
        hasil += i
    print(f"Hasinya {hasil}") 

#PENGURANGAN
def kurang (*angka) :
    hasil = angka [0]
    for i in angka [1:] :
        hasil -= i
    print(f"Hasinya {hasil}") 

#PEMBAGIAN
def bagi (*angka):
    hasil = angka [0]
    for i in angka [1:] :
        hasil //= i
    print(f"Hasinya {hasil}") 

#PERKALIAN
def kali (*angka):
    hasil = angka[0]
    for i in angka [1:]:
        hasil *= i
    print(f"Hasinya {hasil}") 


#PANGKAT
def pangkat (*angka):
    hasil = angka [0]
    for i in angka [1:] :
        hasil = hasil ** i
    print(f"Hasinya {hasil}") 

tambah(2, 5, 3)
kurang(20,5, 10)
bagi(20, 2, 5)
kali(2, 5, 10)
pangkat(5, 2, 3)


# [] = mengeluarkan suatu data dalam suatu variable list dimulai dai 0: