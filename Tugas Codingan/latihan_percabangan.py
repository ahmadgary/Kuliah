import tkinter as tk
from tkinter import messagebox

def check_npm():
    try:
        npm = int(entry.get())
        if npm >= 130102:
            result = "Rino"
        elif npm >= 130029:
            result = "Dinda"
        else:
            result = "Tidak Terdaftar"
        messagebox.showinfo("Hasil", result)
    except ValueError:
        messagebox.showerror("Error", "Masukkan NPM yang valid")

# Create the main window
root = tk.Tk()
root.title("Pengecekan NPM")

# Create and place the widgets
label = tk.Label(root, text="Masukkan NPM:")
label.pack(pady=10)

entry = tk.Entry(root)
entry.pack(pady=5)

button = tk.Button(root, text="Cek NPM", command=check_npm)
button.pack(pady=20)

# Run the application
root.mainloop()
