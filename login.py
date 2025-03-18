import tkinter as tk 
import tkinter
import sqlite3
import random
from tkinter import messagebox as ms
from PIL import Image,ImageTk
from tkinter.ttk import *

root=tk.Tk()
root.configure(background='white')

w,h=root.winfo_screenwidth(),root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w,h))
# oot.title("Background Image")

image2=Image.open('1.jpg')
image2=image2.resize((w,h),Image.LANCZOS)

background_image = ImageTk.PhotoImage(image2)
background_label = tk.Label(root,image=background_image)
background_label.image = background_image
background_label.place(x=0,y=0)

#############################################################################################################


Email = tk.StringVar()
password = tk.StringVar() 
 
def login():
 

    with sqlite3.connect('knee.db') as db:
         c = db.cursor()

        
         db = sqlite3.connect('knee.db')
         cursor = db.cursor()
         cursor.execute("CREATE TABLE IF NOT EXISTS KneeReg"
                        "(name TEXT, address TEXT,  Email TEXT, country TEXT, Phoneno TEXT, Gender TEXT, password TEXT)")
         db.commit()
         
         
         find_entry = ('SELECT * FROM KneeReg WHERE Email = ? and password = ?')
         
         c.execute(find_entry, [(Email.get()), (password.get())])
         result = c.fetchall()
         if result:
            msg = ""
          
            print(msg)
            ms.showinfo("messege", "Login sucessfully")
            

            from subprocess import call
            call(['python','GUI.py'])
            
           
         
         else:
           ms.showerror('Oops!', 'Username Or Password Did Not Found/Match.')





# New_Password=tk.StringVar()
# def forget():
#     con=sqlite3.connect("project11.db")
#     con.execute("""
#                 update registration set New_Password= Password where pass)

###############################################################################################################

label=tk.Label(root,text="Personal Protective Equipment Detection System",font=("Algerian",35),
               bg="brown",
               width=70,
               height=1)
label.place(x=0,y=0)

def shift():
    x1,y1,x2,y2 = canvas.bbox("marquee")
    if(x2<0 or y1<0): #reset the coordinates
        x1 = canvas.winfo_width()
        y1 = canvas.winfo_height()//2
        canvas.coords("marquee",x1,y1)
    else:
        canvas.move("marquee", -2, 0)
    canvas.after(1000//fps,shift)

canvas=tk.Canvas(root,bg="brown")
canvas.pack()
canvas.place(x=0, y=0)
text_var="Personal Protective Equipment Detection System"
text=canvas.create_text(0,-2000,text=text_var,font=('Algerian',35,'bold'),fill='white',tags=("marquee",),anchor='w')
x1,y1,x2,y2 = canvas.bbox("marquee")
width = 1600
height = 70
canvas['width']=width
canvas['height']=height
fps=90    #Change the fps to make the animation faster/slower
shift()   #F

a11=tk. Label(root,text='Login here ',fg='black',bg ='brown',font=('Forte',25)).place(x=170,y=150)

canvas1=tk.Canvas(root,background="light yellow")
canvas1.place(x=20,y=220,width=500,height=400)

#login=Label(root,text="Login",font=('Arial',25),foreground='green').place(x=270,y=350)
a11=tk. Label(root,text='Enter Email',bg='light gray',font=('Cambria',14)).place(x=100,y=300)
a12=tk. Label(root,text='Enter Password',bg='light gray',font=('Cambria',14)).place(x=100,y=350)

b11=tk.Entry(root,width=40, textvariable=Email).place(x=250,y=300,)
b12=tk. Entry(root,width=40,show='*', textvariable=password).place(x=250,y=355,)


def forgot():
    from subprocess import call
    call(['python','forgot password.py'])


button2=tk.Button(root,text="Forgot Password?",fg='blue',bg='light gray',command=forgot)
button2.place(x=400,y=390)



button2=tk.Button(root,text="Login",font=("Bold",9),command=login,width=50,bg='light gray')
button2.place(x=110,y=460)

a=tk. Label(root,text='Not a Member?',font=('Cambria',11),bg='light gray').place(x=350,y=590)

def reg():
    from subprocess import call
    call(['python','registration.py'])

button1=tk.Button(root,text="sign up",fg='blue',bg='light gray',command=reg)
button1.place(x=450,y=595,width=55)



root.mainloop()