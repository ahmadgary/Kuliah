#Tugas Kelompok Chapter 14 Ahmad Gary Shahroom Putra,Adythia Pradiptha Koesnaedi,Kevin Dhiyo Faziliki,Muhammad Hisyam Fata,Muhammad Nabil Ihsan,Romario Galiano
def hitung_tarif_parkir():
    while True:
        jenis_kendaraan = input("Masukkan jenis kendaraan (motor/mobil/bus): ").lower()
        if jenis_kendaraan not in ["motor", "mobil", "bus"]:
            print("Jenis kendaraan tidak valid. Harap masukkan 'motor', 'mobil', atau 'bus'.")
            continue
        
        try:
            durasi_parkir = float(input("Masukkan durasi parkir (jam): "))
            if durasi_parkir < 0:
                print("Durasi parkir harus berupa angka positif.")
                continue
            elif durasi_parkir * 60 < 10:
                print("Parkir gratis (kurang dari 10 menit).")
                return
            
            if jenis_kendaraan == "motor":
                tarif = 2000
            elif jenis_kendaraan == "mobil":
                tarif = 5000
            elif jenis_kendaraan == "bus":
                tarif = 10000

            total_tarif = tarif * durasi_parkir
            print(f"Total tarif parkir: Rp{int(total_tarif):,}")
            break
        except ValueError:
            print("Durasi parkir harus berupa angka.")

# Menjalankan aplikasi parkir
hitung_tarif_parkir()
