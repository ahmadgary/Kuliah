# Nama Anggota = Ahmad Gary, Romario, Muhammad Nabil, Adythia, Kevin Dhiyo,Muhammad Hisyam
import tkinter as tk
from tkinter import messagebox

def tampilkan_hari():
    try:
        nomor_hari = int(entry.get())

        hari = ["Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu", "Minggu"]

        if 1 <= nomor_hari <= 7:
            label_hasil.config(text=hari[nomor_hari - 1])
        else:
            messagebox.showerror("Error", "Masukkan angka antara 1 hingga 7!")
    except ValueError:
        messagebox.showerror("Error", "Input harus berupa angka!")

root = tk.Tk()
root.title("NOMOR 3 KEL.1")

root.geometry("900x500")

root.config(bg="black")

label_instruksi = tk.Label(root, text="Masukkan angka (1-7):", bg="black", fg="white")
label_instruksi.pack(pady=10)

entry = tk.Entry(root, bg="black", fg="white", insertbackground="white")
entry.pack(pady=5)

tombol = tk.Button(root, text="Tampilkan Hari", command=tampilkan_hari ,bg="black", fg="white", relief="solid")
tombol.pack(pady=10)

label_hasil = tk.Label(root, text="", font=("Arial", 200), bg="black", fg="white")
label_hasil.pack(pady=20)

root.mainloop()