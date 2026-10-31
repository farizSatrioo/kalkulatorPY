def tambah(a, b):
    print("Hasil:", a + b)


def kurang(a, b):
    print("Hasil:", a - b)


def kali(a, b):
    print("Hasil:", a * b)


def bagi(a, b):
    if b != 0:
        print("Hasil:", a / b)
    else:
        print("Tidak bisa dibagi nol!")


while True:
    print("\n=== KALKULATOR ===")
    print("1. Tambah (+)")
    print("2. Kurang (-)")
    print("3. Kali (*)")
    print("4. Bagi (/)")
    print("5. Keluar")

    pilihan = input("Pilih menu (1-5): ")

    if pilihan == "5":
        print("Terima kasih telah menggunakan")
        break

    elif pilihan == "1" or pilihan == "2" or pilihan == "3" or pilihan == "4":
        angka1 = int(input("masukan angka 1: "))
        angka2 = int(input("masukan angka 2: "))

        if pilihan == "1":
            tambah(angka1, angka2)
        elif pilihan == "2":
            kurang(angka1, angka2)
        elif pilihan == "3":
            kali(angka1, angka2)
        elif pilihan == "4":
            bagi(angka1, angka2)

    else:
        print("Pilihan tidak tersedia!")
