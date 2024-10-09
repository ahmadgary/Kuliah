import tkinter as tk
from tkinter import messagebox

def check_grade():
    try:
        nilai = int(entry.get())
        if nilai >= 85:
            grade = "Predikat A / Memuaskan"
        elif nilai >= 75:
            grade = "Predikat B / Bagus"
        elif nilai >= 65:
            grade = "Predikat C / Cukup"
        elif nilai >= 55:
            grade = "Predikat D / Kurang"
        else:
            grade = "Predikat E / Sangat Kurang"
        messagebox.showinfo("Hasil", grade)
    except ValueError:
        messagebox.showerror("Error", "Masukkan nilai yang valid")

# Create the main window
root = tk.Tk()
root.title("Penilaian Siswa")

# Create and place the widgets
label = tk.Label(root, text="Masukkan Nilai Siswa:")
label.pack(pady=10)

entry = tk.Entry(root)
entry.pack(pady=5)

button = tk.Button(root, text="Cek Predikat", command=check_grade)
button.pack(pady=20)

# Run the application
root.mainloop()

