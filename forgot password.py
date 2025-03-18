from tkinter import *
from tkinter import messagebox as ms
import sqlite3
import tkinter as tk
import re

root = tk.Tk()
root.title("Forgot Password")
w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w, h))


# Gradient background function
def create_gradient(canvas, width, height):
    gradient = PhotoImage(width=width, height=height)
    for y in range(height):
        r = int(255 * (y / height))
        g = 100
        b = int(255 * (1 - y / height))
        color = f"#{r:02x}{g:02x}{b:02x}"
        gradient.put(color, to=(0, y, width, y + 1))
    return gradient


canvas = Canvas(root, width=w, height=h)
canvas.pack()
gradient_image = create_gradient(canvas, w, h)
canvas.create_image(0, 0, anchor=NW, image=gradient_image)

email = tk.StringVar()
password = tk.StringVar()
confirmPassword = tk.StringVar()

db = sqlite3.connect('knee.db')
cursor = db.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS KneeReg"
               "(name TEXT, address TEXT,  Email TEXT PRIMARY KEY, country TEXT, Phoneno TEXT, Gender TEXT, password TEXT)")
db.commit()


def validate_email(email):
    return re.match(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$", email)


def change_password():
    user_email = email.get()
    new_password = password.get()
    confirm_password = confirmPassword.get()

    if not validate_email(user_email):
        ms.showerror("Error", "Invalid Email Format")
        return

    if len(new_password) < 6:
        ms.showerror("Error", "Password must be at least 6 characters long")
        return

    if new_password != confirm_password:
        ms.showerror("Error", "Passwords do not match")
        return

    with sqlite3.connect('knee.db') as db:
        c = db.cursor()
        c.execute("SELECT * FROM KneeReg WHERE Email=?", (user_email,))
        result = c.fetchone()

    if result:
        with sqlite3.connect("knee.db") as db:
            curs = db.cursor()
            curs.execute("UPDATE KneeReg SET password=? WHERE Email=?", (new_password, user_email))
            db.commit()
        ms.showinfo('Success', 'Password changed successfully')
        root.destroy()
    else:
        ms.showerror('Error', "Email not found in database")


# UI Components with bordered box
frame = Frame(root, bg="white", bd=3, relief=SOLID, highlightbackground="black", highlightthickness=2)
frame.place(x=w // 3 - 50, y=100, width=500, height=300)

label = tk.Label(frame, text="Reset Your Password", font=("Algerian", 20), bg="white")
label.pack(pady=10)

tk.Label(frame, text='Email', font=('Cambria', 14), bg="white").pack()
tk.Entry(frame, width=40, textvariable=email).pack()

tk.Label(frame, text='New Password', font=('Cambria', 14), bg="white").pack()
tk.Entry(frame, width=40, textvariable=password, show="*").pack()

tk.Label(frame, text='Confirm Password', font=('Cambria', 14), bg="white").pack()
tk.Entry(frame, width=40, show="*", textvariable=confirmPassword).pack()

tk.Button(frame, text="Reset Password", width=15, command=change_password).pack(pady=10)

root.mainloop()
