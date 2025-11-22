
nama_user = input("Masukkan nama Anda: ") #memasukan username seuai nama user

def menu_utama(): #membuat function 
    nama_peserta = ('RAGIL', 'FERDI', 'EGA', 'CHESTA', 'AGUS', 'NAUFAL') # tipe data set
    while True :
        print(f"\nHalo, {nama_user}! Selamat datang di program NAMA PESERTA LOMBA.") 
        print("Pilih Opsi yang ingin ditambahkan:")
        print("1. tambah data")
        print("2. Hapus data")
        print("3. Tampilan data")
        print("4. Cek Data")
        print("5. Jumlah Data")
        print("6. Keluar")

        pilihan = input("Masukkan pilihan Anda (1-6): ")

        if pilihan == '1':
            data = input("masukan data yang ingin ditambahkan : ")
            nama_peserta.add(data)
            print("Data berhasil ditambahkan")

        elif pilihan == '2':
            data = input("masukan data yang ingin dihapus : ")
            nama_peserta.remove(data)
            print("Data berhasil dihapus")
    
        elif pilihan == '3':
            if nama_peserta:
                print (nama_peserta)
            else :
                print("data tidak ditemukan")
    
    
        elif pilihan == '4':
            data = input("masukan data yang ingin dicek : ")
            if data in nama_peserta:
                print("data ditemukan didalam set")
        
            else :
                print("Data tidak dapat di temukan")

        elif pilihan == '5' :
            print("jumlah data peserta ", len(nama_peserta))
    
        elif pilihan == '6':
            print("Keluar dari program...")
            break

        else:
            print("pilihan tidak valid, silahkan coba lagi")=



menu_utama()
