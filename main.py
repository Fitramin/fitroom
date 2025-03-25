from PermainanTebakHantu import PermainanTebakHantu
from Kalkulator import kalkulator

def judul():
    print('''
        ====================================================================    
                                SELAMAT DATANG
        ====================================================================
        Di aplikasi ini terdapat beberapa menu pilihan yang bisa kamu coba :
        1. Game Tebak Hantu
        2. Kalkulator
        3. Keluar Program
        ====================================================================
        ''')

def menu(data):
        if data == 1:
            game = PermainanTebakHantu()
            game.mulai()
        elif data == 2:
            calc = kalkulator()
            calc.start()
        elif data == 3:
            print("akan menutup aplikasi")
            input("selamat tinggal program")
            exit()

def main():
    while True:
        judul()

        pilihan = input("Pilih program dengan pilihan ( 1 / 2 / 3 ) ")
        if pilihan.isdigit():
            pilihan = int(pilihan)
        else:
            print("tolong masukan angka1")

        menu(pilihan)

if __name__ == "__main__":
    main()


        
