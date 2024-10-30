def proses_pesanan(nama, barang, harga, diskon=0):
    # Menghitung total harga barang sebelum diskon dan pajak
    total_harga = sum(harga)

    # Mengaplikasikan diskon jika ada
    if diskon > 0:
        total_diskon = (diskon / 100) * total_harga
    else:
        total_diskon = 0

    total_harga_setelah_diskon = total_harga - total_diskon

    # Menambahkan pajak 10%
    pajak = 0.10 * total_harga_setelah_diskon
    total_harga_setelah_pajak = total_harga_setelah_diskon + pajak

    # Menampilkan ringkasan pesanan
    print(f"\nPesanan untuk : {nama}")
    print("Daftar Barang yang dibeli:")
    for i in range(len(barang)):
        print(f"- {barang[i]}: Rp {harga[i]}")
    print(f"Total Harga: Rp {total_harga}")
    print(f"Total setelah diskon dan pajak: Rp {total_harga_setelah_pajak:.2f}\n")

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
