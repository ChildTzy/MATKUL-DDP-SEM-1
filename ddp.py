
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



"""alas = 50
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
hitung_luas_balok()"""
