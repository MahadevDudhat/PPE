import tkinter as tk
import sqlite3
import random
import re
from tkinter import messagebox as ms
from PIL import Image, ImageTk

# Initialize window
root = tk.Tk()
root.configure(background='white')
w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry(f"{w}x{h}+0+0")

# Background Image
image2 = Image.open('p.jpg').resize((w, h), Image.LANCZOS)
background_image = ImageTk.PhotoImage(image2)
background_label = tk.Label(root, image=background_image)
background_label.image = background_image
background_label.place(x=0, y=0)

# Variables
name = tk.StringVar()
email = tk.StringVar()
password = tk.StringVar()
confirm_password = tk.StringVar()
address = tk.StringVar()
country = tk.StringVar()
phone_no = tk.StringVar()
gender = tk.IntVar()

# Database Setup
db = sqlite3.connect('knee.db')
cursor = db.cursor()
cursor.execute("""
    CREATE TABLE IF NOT EXISTS KneeReg (
        name TEXT, address TEXT, email TEXT, country TEXT, 
        phoneno TEXT, gender TEXT, password TEXT
    )
""")
db.commit()


def validate_inputs():
    """ Validates all input fields before inserting into the database """
    fname = name.get().strip()
    addr = address.get().strip()
    email_input = email.get().strip()
    mobile = phone_no.get().strip()
    selected_gender = gender.get()
    pwd = password.get().strip()
    cnpwd = confirm_password.get().strip()

    # Name validation
    if not fname.isalpha():
        ms.showerror("Error", "Please enter a valid name (letters only).")
        return False

    # Address validation
    if not addr:
        ms.showerror("Error", "Address cannot be empty.")
        return False

    # Email validation
    regex = r'^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
    if not re.search(regex, email_input):
        ms.showerror("Error", "Please enter a valid email.")
        return False

    # Phone number validation (exactly 10 digits)
    if not mobile.isdigit() or len(mobile) != 10:
        ms.showerror("Error", "Phone number must be exactly 10 digits.")
        return False

    # Country validation
    if not country.get().strip():
        ms.showerror("Error", "Country cannot be empty.")
        return False

    # Gender validation
    if selected_gender not in [1, 2]:
        ms.showerror("Error", "Please select a gender.")
        return False

    # Password validation
    special_chars = r'[@$#%]'
    if len(pwd) < 6 or len(pwd) > 20:
        ms.showerror("Error", "Password must be between 6 and 20 characters.")
        return False
    if not re.search(r'[A-Z]', pwd):
        ms.showerror("Error", "Password must contain at least one uppercase letter.")
        return False
    if not re.search(r'[a-z]', pwd):
        ms.showerror("Error", "Password must contain at least one lowercase letter.")
        return False
    if not re.search(r'\d', pwd):
        ms.showerror("Error", "Password must contain at least one number.")
        return False
    if not re.search(special_chars, pwd):
        ms.showerror("Error", "Password must contain at least one special character (@, $, #, %).")
        return False

    # Confirm Password validation
    if pwd != cnpwd:
        ms.showerror("Error", "Passwords do not match.")
        return False

    return True


def insert():
    """ Inserts the validated data into the database """
    if validate_inputs():
        with sqlite3.connect('knee.db') as db:
            cursor = db.cursor()
            cursor.execute(
                'INSERT INTO KneeReg(name, address, email, country, phoneno, gender, password) VALUES(?, ?, ?, ?, ?, ?, ?)',
                (name.get(), address.get(), email.get(), country.get(), phone_no.get(), gender.get(), password.get())
            )
            db.commit()
        ms.showinfo('Success', 'Account Created Successfully!')
        root.destroy()  # Close registration window
        from subprocess import call
        call(['python', 'login.py'])


# UI Components
label = tk.Label(root, text="Registration Form", font=("Forte", 30), bg="light yellow", fg="black")
label.place(x=180, y=40)

canvas = tk.Canvas(root, background="white", borderwidth=5)
canvas.place(x=150, y=100, width=400, height=500)

tk.Label(root, text="Name:", font=("Calibri", 10), bg="white").place(x=200, y=200)
tk.Entry(root, border=2, textvar=name).place(x=330, y=205)

tk.Label(root, text="Email:", font=("Calibri", 10), bg="white").place(x=200, y=250)
tk.Entry(root, border=2, textvar=email).place(x=330, y=255)

tk.Label(root, text="Password:", font=("Calibri", 10), bg="white").place(x=200, y=300)
tk.Entry(root, border=2, show="*", textvar=password).place(x=330, y=305)

tk.Label(root, text="Re-Enter Password:", font=("Calibri", 10), bg="white").place(x=200, y=350)
tk.Entry(root, border=2, show="*", textvar=confirm_password).place(x=330, y=355)

tk.Label(root, text="Address:", font=("Calibri", 10), bg="white").place(x=200, y=400)
tk.Entry(root, border=2, textvar=address).place(x=330, y=405)

tk.Label(root, text="Country:", font=("Calibri", 10), bg="white").place(x=200, y=450)
tk.Entry(root, border=2, textvar=country).place(x=330, y=455)

tk.Label(root, text="Phone no:", font=("Calibri", 10), bg="white").place(x=200, y=515)
tk.Entry(root, border=2, textvar=phone_no).place(x=330, y=520)

tk.Label(root, text="Gender:", font=("Calibri", 10), bg="white").place(x=200, y=490)
tk.Radiobutton(root, text="Male", font=("Calibri", 10), bg="white", value=1, variable=gender).place(x=330, y=490)
tk.Radiobutton(root, text="Female", font=("Calibri", 10), bg="white", value=2, variable=gender).place(x=400, y=490)

# Buttons
tk.Button(root, text="Create Account", font=("Arial"), width=20, command=insert, bg="black", fg="white").place(x=250,
                                                                                                               y=550)

tk.Label(root, text="Already have an account?", bg="white", font=('Cambria', 11)).place(x=250, y=700)
tk.Button(root, text="Log in", fg='blue', bg='white',
          command=lambda: [root.destroy(), __import__('subprocess').call(['python', 'login.py'])]).place(x=380, y=700)

root.mainloop()
