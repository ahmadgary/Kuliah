# Slide 11
import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Form Kategori")
root.geometry("400x300")

frame = tk.Frame(root, padx=10, pady=10)
frame.pack(pady=20)

label_kode = tk.Label(frame, text="KODE KATEGORI")
label_kode.grid(row=0, column=0, sticky="w")
entry_kode = tk.Entry(frame, width=30)
entry_kode.grid(row=0, column=1)

label_nama = tk.Label(frame, text="NAMA")
label_nama.grid(row=1, column=0, sticky="w")
entry_nama = tk.Entry(frame, width=30)
entry_nama.grid(row=1, column=1)

label_jenis = tk.Label(frame, text="JENIS")
label_jenis.grid(row=2, column=0, sticky="w")
combo_jenis = ttk.Combobox(frame, width=28)
combo_jenis['values'] = ("Jenis A", "Jenis B", "Jenis C") 
combo_jenis.grid(row=2, column=1)

frame_buttons = tk.Frame(root, padx=10, pady=10)
frame_buttons.pack()

btn_save = tk.Button(frame_buttons, text="SAVE", width=10)
btn_save.grid(row=0, column=0, padx=5)

btn_update = tk.Button(frame_buttons, text="UPDATE", width=10)
btn_update.grid(row=0, column=1, padx=5)

btn_delete = tk.Button(frame_buttons, text="DELETE", width=10)
btn_delete.grid(row=0, column=2, padx=5)

text_area = tk.Text(root, height=8, width=40)
text_area.pack(pady=10)

root.mainloop()