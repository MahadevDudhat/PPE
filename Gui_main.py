import tkinter as tk
from PIL import Image, ImageTk
from subprocess import call

root = tk.Tk()
root.configure(background='white')
w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w, h))
root.title("Personal Protective Equipment Detection System")

# Background Image
image2 = Image.open("2.jpg")
image2 = image2.resize((w, h), Image.LANCZOS)
background_image = ImageTk.PhotoImage(image2)

background_label = tk.Label(root, image=background_image)
background_label.image = background_image
background_label.place(x=0, y=0)

# Title Label
label = tk.Label(root, text="Personal Protective Equipment Detection System", font=("Algerian", 35),
                 bg="yellow", width=50, height=1)
label.place(x=0, y=0)

# Marquee Animation
def shift():
    x1, y1, x2, y2 = canvas.bbox("marquee")
    if x2 < 0 or y1 < 0:  # Reset the coordinates
        x1 = canvas.winfo_width()
        y1 = canvas.winfo_height() // 2
        canvas.coords("marquee", x1, y1)
    else:
        canvas.move("marquee", -2, 0)
    canvas.after(1000 // fps, shift)

canvas = tk.Canvas(root, bg="yellow")
canvas.pack()
canvas.place(x=0, y=0)
text_var = "Personal Protective Equipment Detection System"
text = canvas.create_text(0, -2000, text=text_var, font=('Algerian', 35, 'bold'), fill='black', tags=("marquee",), anchor='w')
x1, y1, x2, y2 = canvas.bbox("marquee")
width = 1600
height = 70
canvas['width'] = width
canvas['height'] = height
fps = 90  # Adjust the FPS for animation speed
shift()   # Start animation

# Function to open Login Page
def open_login():
    call(['python', 'login.py'])

# Function to open Registration Page
def open_register():
    call(['python', 'registration.py'])

# Function to open About Us Page
def open_about_us():
    call(['python', 'about_us.py'])

# Set a fixed x-position for vertical alignment
x_position = 600  # Centered placement

# Buttons aligned vertically
btn_login = tk.Button(root, text="Login", command=open_login, font=("Arial", 15), width=12, bg="white", fg="black")
btn_login.place(x=x_position, y=300)  # First button

btn_register = tk.Button(root, text="Register", command=open_register, font=("Arial", 15), width=12, bg="white", fg="black")
btn_register.place(x=x_position, y=370)  # Second button below Login

btn_about_us = tk.Button(root, text="About Us", command=open_about_us, font=("Arial", 15), width=12, bg="white", fg="black")
btn_about_us.place(x=x_position, y=440)  # Third button below Register

root.mainloop()
