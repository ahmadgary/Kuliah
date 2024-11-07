import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

# Variabel global untuk menyimpan nilai awal
initial_values = {
    "kode": "",
    "nama": "",
    "jenis": ""
}

def validate_inputs():
    kode = entry_kode.get()
    nama = entry_nama.get()
    jenis = combo_jenis.get()
    
    if not kode or not nama or not jenis:
        messagebox.showerror("Input Error", "Semua kolom harus diisi!")
        return False
    if not kode.isalnum():
        messagebox.showerror("Input Error", "Kode kategori harus alfanumerik!")
        return False
    return True

def save_data():
    if validate_inputs():
        kode = entry_kode.get()
        nama = entry_nama.get()
        jenis = combo_jenis.get()
        text_area.insert(tk.END, f"Save: Kode: {kode}, Nama: {nama}, Jenis: {jenis}\n")
        # Simpan nilai awal
        initial_values["kode"] = kode
        initial_values["nama"] = nama
        initial_values["jenis"] = jenis

def update_data():
    if validate_inputs():
        kode = entry_kode.get()
        nama = entry_nama.get()
        jenis = combo_jenis.get()
        
        # Periksa apakah ada perubahan pada data
        if kode == initial_values["kode"] and nama == initial_values["nama"] and jenis == initial_values["jenis"]:
            messagebox.showerror("Update Error", "Tidak ada perubahan pada data!")
            return
        
        text_area.insert(tk.END, f"Update: Kode: {kode}, Nama: {nama}, Jenis: {jenis}\n")
        # Perbarui nilai awal
        initial_values["kode"] = kode
        initial_values["nama"] = nama
        initial_values["jenis"] = jenis

def delete_data():
    if validate_inputs():
        kode = entry_kode.get()
        nama = entry_nama.get()
        jenis = combo_jenis.get()
        text_area_content = text_area.get("1.0", tk.END)
        lines = text_area_content.splitlines()
        updated_lines = [line for line in lines if not (f"Kode: {kode}" in line and f"Nama: {nama}" in line and f"Jenis: {jenis}" in line)]
        text_area.delete("1.0", tk.END)
        for line in updated_lines:
            text_area.insert(tk.END, line + "\n")
        messagebox.showinfo("Success", f"Data Kode: {kode}, Nama: {nama}, Jenis: {jenis} berhasil dihapus")

root = tk.Tk()
root.title("Form Kategori")
root.geometry("450x350")
root.configure(bg="#f5f5f5")

frame = tk.Frame(root, padx=10, pady=10, bg="#f5f5f5")
frame.pack(pady=20)

label_kode = tk.Label(frame, text="KODE KATEGORI", font=("Helvetica", 12), bg="#f5f5f5")
label_kode.grid(row=0, column=0, sticky="w")
entry_kode = tk.Entry(frame, width=30, font=("Helvetica", 12))
entry_kode.grid(row=0, column=1, padx=10, pady=5)

label_nama = tk.Label(frame, text="NAMA", font=("Helvetica", 12), bg="#f5f5f5")
label_nama.grid(row=1, column=0, sticky="w")
entry_nama = tk.Entry(frame, width=30, font=("Helvetica", 12))
entry_nama.grid(row=1, column=1, padx=10, pady=5)

label_jenis = tk.Label(frame, text="JENIS", font=("Helvetica", 12), bg="#f5f5f5")
label_jenis.grid(row=2, column=0, sticky="w")
combo_jenis = ttk.Combobox(frame, width=28, font=("Helvetica", 12))
combo_jenis['values'] = ("Jenis A", "Jenis B", "Jenis C") 
combo_jenis.grid(row=2, column=1, padx=10, pady=5)

frame_buttons = tk.Frame(root, padx=10, pady=10, bg="#f5f5f5")
frame_buttons.pack(pady=10)

btn_save = tk.Button(frame_buttons, text="SAVE", width=10, font=("Helvetica", 12), bg="#4CAF50", fg="white", command=save_data)
btn_save.grid(row=0, column=0, padx=5, pady=5)

btn_update = tk.Button(frame_buttons, text="UPDATE", width=10, font=("Helvetica", 12), bg="#2196F3", fg="white", command=update_data)
btn_update.grid(row=0, column=1, padx=5, pady=5)

btn_delete = tk.Button(frame_buttons, text="DELETE", width=10, font=("Helvetica", 12), bg="#f44336", fg="white", command=delete_data)
btn_delete.grid(row=0, column=2, padx=5, pady=5)

text_area = tk.Text(root, height=8, width=40, font=("Helvetica", 12))
text_area.pack(pady=10)

root.mainloop()