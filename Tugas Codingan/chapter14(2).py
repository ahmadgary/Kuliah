#Tugas Kelompok Chapter 14 Ahmad Gary Shahroom Putra,Adythia Pradiptha Koesnaedi,Kevin Dhiyo Faziliki,Muhammad Hisyam Fata,Muhammad Nabil Ihsan,Romario Galiano
def generate_multiplication_table():
    while True:
        try:
            angka = int(input("Masukkan angka: "))
            if angka < 0:
                print("Angka tidak boleh negatif.")
            else:
                for i in range(1, 11):
                    print(f"{angka} x {i} = {angka * i}")
                break
        except ValueError:
            print("Input tidak valid. Harap masukkan angka.")

# Menjalankan aplikasi
generate_multiplication_table()
