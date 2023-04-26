import tkinter as tk
from tkinter import messagebox

def logn():
    if username_label.get() == "admin" and pasword_entry.get() == "password":
        messagebox.showinfo("Login successful", "Welcome!")
    else:
        messagebox.showerror("Login failed", "Incorrect username or password.")

def cler():
    username_label.delete(0, tk.END)
    pasword_entry.delete(0, tk.END)

prog = tk.Tk()
prog.title("Login")
prog.geometry("350x150")

name_label = tk.Label(prog, text="Username:")
username_label = tk.Entry(prog)
password_label = tk.Label(prog, text="Password:")
pasword_entry = tk.Entry(prog, show="*")

login_button = tk.Button(prog, text="Login", command=logn)
clear_button = tk.Button(prog, text="Clear", command=cler)

name_label.grid(row=0, column=0, padx=5, pady=5)
username_label.grid(row=0, column=1, padx=5, pady=5)
password_label.grid(row=1, column=0, padx=5, pady=5)
pasword_entry.grid(row=1, column=1, padx=5, pady=5)
login_button.grid(row=2, column=0, padx=5, pady=5)
clear_button.grid(row=2, column=1, padx=5, pady=5)

prog.mainloop()
