# Nama Anggota = Ahmad Gary, Romario, Muhammad Nabil, Adythia, Kevin Dhiyo,Muhammad Hisyam
import tkinter as tk

root = tk.Tk()

def print_buy(fruit):
    print(f'Kamu Beli 1 {fruit}')

# Membuat tombol untuk setiap buah
for f in ['Apel', 'Pisang']:
    btn = tk.Button(
        root,
        text=f'Beli {f}',
        command=lambda f=f: print_buy(f)  # Menentukan argumen f secara eksplisit
    )
    btn.pack()

root.mainloop()