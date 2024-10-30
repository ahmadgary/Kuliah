# Variabel global
tax_rate = 0.10  # Pajak 10%
total_price = 0  # Total harga keseluruhan

def proses_pesanan(nama, barang, harga, diskon=0):
    global total_price  # Menggunakan variabel global

    # Menghitung total harga barang sebelum diskon dan pajak
    subtotal = sum(harga)  # Variabel lokal
    if diskon > 0:
        total_diskon = (diskon / 100) * subtotal  # Variabel lokal
    else:
        total_diskon = 0

    total_harga_setelah_diskon = subtotal - total_diskon  # Variabel lokal

    # Menambahkan pajak 10%
    pajak = total_harga_setelah_diskon * tax_rate  # Variabel lokal
    total_harga_setelah_pajak = total_harga_setelah_diskon + pajak  # Variabel lokal
    total_price += total_harga_setelah_pajak

    # Menampilkan ringkasan pesanan
    print(f"\nPesanan untuk : {nama}")
    print("Daftar Barang yang dibeli:")
    for i in range(len(barang)):
        print(f"- {barang[i]}: Rp {harga[i]}")
    print(f"Total Harga: Rp {subtotal}")
    print(f"Total setelah diskon dan pajak: Rp {total_harga_setelah_pajak:.2f}")

# Input nama pelanggan
nama = input("Masukkan nama pelanggan: ")

# Input jumlah barang
jumlah_barang = int(input("Masukkan jumlah barang: "))

# Input daftar barang dan harganya
barang = []
harga = []
for i in range(jumlah_barang):
    nama_barang = input(f"Masukkan nama barang ke-{i+1}: ")
    harga_barang = float(input(f"Masukkan harga {nama_barang}: "))
    barang.append(nama_barang)
    harga.append(harga_barang)

# Input diskon
diskon = float(input("Masukkan diskon (dalam persen, jika ada): "))

# Memproses pesanan
proses_pesanan(nama, barang, harga, diskon)

# Menampilkan total belanja keseluruhan
print(f"Total Harga Keseluruhan untuk {nama}: Rp {total_price:.2f}")