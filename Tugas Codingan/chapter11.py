#Tugas Kelompok Chapter 11 Ahmad Gary Shahroom Putra,Adythia Pradiptha Koesnaedi,Kevin Dhiyo Faziliki,Muhammad Hisyam Fata,Muhammad Nabil Ihsan,Romario Galiano
import tkinter as tk
from tkinter import messagebox

def calculate_discount():
    try:
        total_belanja = float(entry_total.get())
        if total_belanja > 500000:
            discount = total_belanja * 0.07
            bonus = "Bonus Coca Cola dan diskon 7%"
        elif 100000 <= total_belanja <= 499000:
            discount = total_belanja * 0.05
            bonus = "Bonus Coca Cola dan diskon 5%"
        else:
            discount = 0
            bonus = "Tidak mendapatkan diskon dan kupon belanja"
        
        total_bayar = total_belanja - discount
        result_text = (f"Total belanja : Rp{total_belanja:.2f}\n"
                       f"{bonus}\n"
                       f"Diskon : Rp{discount:.2f}\n"
                       f"Total Bayar : Rp{total_bayar:.2f}\n"
                       f"Barang yang sudah dibeli tidak dapat ditukar\n"
                       f"Terimakasih Sudah Belanja di Toko ABC")
        messagebox.showinfo("Hasil", result_text)
    except ValueError:
        messagebox.showerror("Error", "Masukkan nilai total belanja yang valid")

root = tk.Tk()
root.title("Hitung Diskon dan Bonus")

label_total = tk.Label(root, text="Masukkan Total Belanja:")
label_total.pack(pady=10)
entry_total = tk.Entry(root)
entry_total.pack(pady=5)

btn_calculate = tk.Button(root, text="Hitung Diskon & Bonus", command=calculate_discount)
btn_calculate.pack(pady=20)

root.mainloop()