import tkinter as tk

# Initialize the main window
root = tk.Tk()
root.title("Personal Protective Equipment Detection")

# Automatically adjust to screen size
root.geometry(f"{root.winfo_screenwidth()}x{root.winfo_screenheight()}")
root.state("zoomed")  # Maximized window

# Create a Canvas for gradient background
canvas = tk.Canvas(root)
canvas.pack(fill="both", expand=True)

def create_gradient(canvas, width, height):
    """Creates a vertical gradient effect on the canvas"""
    color1 = (255, 140, 0)  # Orange
    color2 = (0, 0, 128)    # Navy Blue

    for i in range(height):
        r = int(color1[0] + (color2[0] - color1[0]) * (i / height))
        g = int(color1[1] + (color2[1] - color1[1]) * (i / height))
        b = int(color1[2] + (color2[2] - color1[2]) * (i / height))
        color = f'#{r:02x}{g:02x}{b:02x}'
        canvas.create_line(0, i, width, i, fill=color)

# Function to update gradient dynamically when resized
def update_gradient(event=None):
    canvas.delete("all")  # Clear previous gradient
    create_gradient(canvas, root.winfo_width(), root.winfo_height())

canvas.bind("<Configure>", update_gradient)  # Redraw gradient when window is resized

# Draw the initial gradient
create_gradient(canvas, root.winfo_screenwidth(), root.winfo_screenheight())

# Content Frame to prevent overlapping
content_frame = tk.Frame(root, bg="white")
content_frame.place(relx=0.5, rely=0.5, anchor="center")

# Title Label
title_label = tk.Label(content_frame, text="Personal Protective Equipment Detection", font=("Arial", 20, "bold"), bg="white")
title_label.pack(pady=10)

# Group Details
group_label = tk.Label(content_frame, text="Group No.: 12", font=("Arial", 16), bg="white")
group_label.pack()

guided_by_label = tk.Label(content_frame, text="Guided By: Prof. P. C. Kinage", font=("Arial", 16), bg="white")
guided_by_label.pack(pady=5)

members_label = tk.Label(content_frame, text="Group Members:", font=("Arial", 16, "bold"), bg="white")
members_label.pack()

members_text = "1] Vedant Borgaonkar\n2] Prasad Misal\n3] Mahadev Dudhat"
members_list = tk.Label(content_frame, text=members_text, font=("Arial", 14), bg="white", justify="center")
members_list.pack()

# Abstract
abstract_label = tk.Label(content_frame, text="Abstract:", font=("Arial", 16, "bold"), bg="white")
abstract_label.pack(pady=10)

abstract_text = (
    "In industrial environments, real-time object identification has become crucial for automating various "
    "tasks, including the monitoring of Personal Protective Equipment (PPE) usage. Ensuring the proper application "
    "of PPE in hazardous areas is essential for enhancing worker safety. Typically, PPE usage is monitored through "
    "video streams from security cameras, and when an employee is detected without the required PPE, automatic "
    "visual or auditory warnings are triggered to raise awareness. However, most existing solutions rely on "
    "cloud-based systems, which require substantial network bandwidth and a reliable internet connection to transmit "
    "video data for analysis. This centralized architecture introduces challenges related to network reliability, "
    "bandwidth consumption, and privacy. This paper proposes a real-time PPE detection system based on deep learning "
    "and edge computing to overcome these limitations. By leveraging Convolutional Neural Networks (CNNs) and "
    "deploying the system on low-cost hardware, such as Raspberry Pi and Intel Neural Compute Stick, PPE "
    "detection can be conducted locally, reducing bandwidth usage and enhancing system reliability and worker "
    "privacy. The proposed system is tested with various deep learning models, evaluating the trade-offs between "
    "detection accuracy and processing speed, leading to practical recommendations for real-time deployment in "
    "industrial environments."
)

abstract_text_label = tk.Label(content_frame, text=abstract_text, font=("Arial", 14), wraplength=900, bg="white", justify="left")
abstract_text_label.pack(pady=10)

# Close window with Escape key
def close_window(event=None):
    root.destroy()

root.bind("<Escape>", close_window)  # Press "Esc" to close the window

root.mainloop()