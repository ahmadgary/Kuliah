# Meminta input total belanja dari pengguna
total_belanja = float(input("Masukkan total belanja Budi: "))

# Inisialisasi variabel diskon dan total bayar
diskon_persen = 0
total_bayar = total_belanja

# Menghitung diskon jika total belanja lebih dari 300
while total_belanja > 300:
    diskon_persen = 15
    diskon = (diskon_persen / 100) * total_belanja
    total_bayar = total_belanja - diskon
    break

# Menampilkan hasil
print(f"Total belanja: Rp{total_belanja}")
print(f"Diskon: {diskon_persen}%")
print(f"Total yang harus dibayar: Rp{total_bayar}")