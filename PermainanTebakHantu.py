import random

class PermainanTebakHantu:
    def __init__(self):
        self.pemain_scores = []
    
    def bubble_sort(self):
        
        n = len(self.pemain_scores)
        for i in range(n):
            for j in range(0, n - i - 1):
                if self.pemain_scores[j][1] < self.pemain_scores[j + 1][1]:
                    self.pemain_scores[j], self.pemain_scores[j + 1] = self.pemain_scores[j + 1], self.pemain_scores[j]
    def introgame(self):
        print('''
        ====================================================================    
                     SELAMAT DATANG DI PERMAINAN TEBAK HANTU
        ====================================================================
        Apakah kamu suka dengan game tebak tebakan?
        ada sebuah ratu hantu yang sedang dikawal oleh 10 hantu merah.
        ratu hantu itu seorang gadis perempuan berwujud hantu putih.
        kemampuan dia adalah bisa mengubah dirinya menjadi hantu merah.
        dia bisa berpindah posisi sesuai dengan keinginan dia.
        tugas kamu adalah menebak posisi hantu putih.
        ====================================================================
        ''')
    def petunjukpermainan(self):
        print('''
        ====================================================================
                                 PETUNJUK PERMAINAN
        ====================================================================
        1. Masukan nama kamu sebagai nama pemain.
        2. Posisi hantu putih itu acak.
        3. Pilih angka 1 - 10 untuk menebak posisi hantu putih.
        4. Kamu akan diberikan 10 kesempatan menebak posisi hantu putih.
        5. Setiap tebakan yang salah, skor kamu akan berkurang 10 poin.
        6. Jika tebakan pertama benar, kamu akan mendapatkan skor 100 poin.
        7. Jika semua tebakan salah skor kamu akan menjadi 0 poin.
        8. Bisa bermain dengan temanmu secara bergantian.
              
        Lihat siapa yang mendapatkan skor tertinggi dan Selamat bermain!
        ====================================================================
        ''')
    def mulai(self):
        
        self.introgame()
        self.petunjukpermainan()
        while True:
            pilihan_main = input("❓❓Apakah anda ingin bermain?❓❓ (iya/tidak): ").strip().lower()
            print()
            
            if pilihan_main == "tidak":
                print("Terima kasih sudah bermain! \n")
                if self.pemain_scores:
                    print("🏆 URutan rangking dari masing masing pemain 🏆\n")
                    self.bubble_sort()
                    for i, (nama, score) in enumerate(self.pemain_scores):
                        print(f"{i+1}. {nama} mendapatkan {score} point")
                else:
                    print("Belum ada skor yang tercatat.\n")
                input("\nTekan Enter untuk kembali ke menu utama...")
                return
            elif pilihan_main == "iya":
                nama_pemain = input("Masukkan nama pemain: ").strip()
                print()
                hantumerah = "👹"
                hantuputih = "👻"
                a = [hantumerah] * 10  
                skor = 100
                percobaan = 0
                print(f"🥰 Selamat datang, kak {nama_pemain}! 🥰\n")
                print(" ".join(a))
                print()
                b = random.randint(0, 9)  
                a[b] = hantuputih  
                print("Ada 10 hantu merah yang diantaranya ada Hantu PUtih sedang sembunyi")
                print("Tebak posisi hantu putih 👻 dengan memilih angka 1 - 10")
                print()

                while percobaan < 10:
                    tebakan = input(f"[Percobaan ke-{percobaan+1}] Masukkan angka 1 sampai 10: ")
                    print()
                    
                    if tebakan.isdigit():
                        tebakan = int(tebakan) - 1  
                        
                        if 0 <= tebakan <= 9:
                            if tebakan == b:
                                if skor != 100:
                                    print(f"🎉🎉🎉  Selamat, tebakan kak {nama_pemain} benar! 🎉🎉🎉")
                                else:
                                    print(f"🎉🎉🎉 WOW tebakan pertama kak {nama_pemain} langsung benar, keren 🎉🎉🎉")
                                
                                print(f"Skor kak {nama_pemain}: {skor}")
                                print("Posisi hantu putih 👻 ada di urutan ke: ", b+1)
                                print(" ".join(a))
                                print()
                                break
                            else:
                                percobaan += 1
                                skor -= 10
                                if tebakan < b:
                                    print("💡 Tebakanmu terlalu kecil dari posisi hantu putih 👻")
                                elif tebakan > b:
                                    print("💡 Tebakanmu terlalu besar dari posisi hantu putih 👻")
                                print(f"❌ Maaf, kak {nama_pemain}, tebakannya salah 😞")
                                print(f"Skor kak {nama_pemain}: {skor}\n")

                                if percobaan == 10:
                                    print(f"😞 Maaf, kak {nama_pemain} kalah.")
                                    print(f"Skor akhir: {skor}\n")
                        else:
                            print("⚠️ Masukkan angka antara 1-10!\n")
                    else:
                        print("⚠️ Masukkan angka yang valid!\n")

                self.pemain_scores.append((nama_pemain, skor))  
        
        input("Game tebak hantu sudah berakhir tekan enter untuk keluar")


if __name__ == "__main__":
    game = PermainanTebakHantu()
    game.mulai()                                             