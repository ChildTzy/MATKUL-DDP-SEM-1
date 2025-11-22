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
