class kalkulator:

    def __init__(self):
        pass
    def jumlah(self,x,y):
        return x + y
    def pengurangan(self,x,y):
        return x - y
    def perkalian(self,x,y):
        return x * y
    def pembagian(self,x,y):
        return x / y
    def judul(self):
        print('''
        ====================================================================    
                        SELAMAT DATANG DIKALKULATOR SEDERHANA
        ====================================================================
        Di kalkulator ini ada 4 pilihan operasi yaitu :
        1. Penjumlahan
        2. Pengurangan
        3. Perkalian
        4. Pembagian
        ====================================================================
        ''')
    def petunjuk(self):
        print('''
        ====================================================================    
                                PETUNJUK PENGOPRASIAN
        ====================================================================
        1. Masukan angka pertama
        2. Masukan angka kedua
        3. Pilih operasi
        4. System akan bertanya adakah angka yang ingin ditambahkan
        5. Bila tidak ada, system akan mencetak total penghitungan
        ====================================================================
        ''')
    def start(self):
        self.judul()
        self.petunjuk()

        tampung = (int(input("masukan angka pertama : ")))
        print()

        while True:
            pertanyaan = input("apakah ingin menambahkan angka?(iya/tidak) : ").strip().lower()
            print()
            if pertanyaan == "tidak":
                print(f"Totalnya adalah {round(tampung,2)}")
    
                print("kalkulator akan berhenti\n")
                input("Program kalkulator berhenti dan akan kembali ke menu utama\n")
                return
            elif pertanyaan =="iya": 
                angka = int(input("masukan angka ke 2 yang ingin di operasikan :"))
                print()
                while True:
                    operator = input("silahkan pilih operasi(+ , - , * , / ) : ")
                    print()
                    if operator == "+" :
                        hasil = self.jumlah(tampung,angka)

                    elif operator == "-" :
                        hasil = self.pengurangan(tampung,angka)
                    
                    elif operator == "*" :
                        hasil = self.perkalian(tampung,angka)
                        
                    elif operator == "/" :
                        hasil = self.pembagian(tampung,angka)
                    # else:
                    #     print(f"{operator} bukan operator")
                    print(f"Hasil dari {tampung} {operator} {angka} = ", end="")
                    tampung = hasil
                    hasila : int = tampung
                    print(round(hasil,2))
                    break
                    
if __name__ == "__main__":
    calc = kalkulator()
    calc.start()            

