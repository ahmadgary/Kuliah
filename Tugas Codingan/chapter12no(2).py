# Nama Anggota = Ahmad Gary, Romario, Muhammad Nabil, Adythia, Kevin Dhiyo,Muhammad Hisyam
import tkinter as tk

root = tk.Tk()
root.title("Menampilkan Angka 1-20")

def display_numbers():
    for i in range(1, 21):
        print(f'Kamu menampilkan angka {i}')

# Membuat satu tombol yang akan menampilkan angka 1-20
button = tk.Button(root, text="Tampilkan Angka 1-20", command=display_numbers)
button.pack(pady=20)

root.mainloop()
