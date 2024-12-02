import tkinter as tk

# Fungsi untuk menambahkan angka atau operasi ke layar kalkulator
def button_click(value):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current + str(value))

# Fungsi untuk menghitung hasil
def calculate():
    try:
        result = eval(entry.get())  # Mengevaluasi ekspresi matematika
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

# Fungsi untuk menghapus layar
def clear():
    entry.delete(0, tk.END)

# Setup GUI
root = tk.Tk()
root.title("Kalkulator Sederhana")
root.geometry("400x500")

# Entry untuk menampilkan input dan hasil
entry = tk.Entry(root, width=20, font=('Arial', 24), bd=10, relief="sunken", justify="right")
entry.grid(row=0, column=0, columnspan=4)

# Tombol angka dan operasi
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3)
]

# Menambahkan tombol ke GUI
for (text, row, col) in buttons:
    if text == "=":
        tk.Button(root, text=text, width=10, height=3, font=('Arial', 18), command=calculate).grid(row=row, column=col, padx=5, pady=5)
    else:
        tk.Button(root, text=text, width=10, height=3, font=('Arial', 18), command=lambda value=text: button_click(value)).grid(row=row, column=col, padx=5, pady=5)

# Tombol Clear
tk.Button(root, text="C", width=10, height=3, font=('Arial', 18), command=clear).grid(row=5, column=0, columnspan=4, padx=5, pady=5)

# Menjalankan aplikasi
root.mainloop()
