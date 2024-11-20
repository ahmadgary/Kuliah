# Nama Anggota = Ahmad Gary, Romario, Muhammad Nabil, Adythia, Kevin Dhiyo,Muhammad Hisyam
datakaryawan = ["budi", "bunga", "alex", "mawar", "dani", "sultan"]
nama = input("Masukkan nama: ").lower()
print(f"{nama.capitalize()} adalah {'karyawan' if nama in datakaryawan else 'bukan karyawan'}.")
