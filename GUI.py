import os
import cv2
import subprocess
import tkinter as tk
from tkinter import ttk, LEFT, END
from PIL import Image, ImageTk
from tkinter import messagebox as ms
from tkinter.filedialog import askopenfilename
global fn
global vid
global frame_
frame_=""
vid=""

fn=""


root = tk.Tk()
root.configure(background="grey")
# root.geometry("1300x700")


w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w, h))
root.title("main")

image2=Image.open('1.jpg')
image2=image2.resize((w,h),Image.LANCZOS)

background_image = ImageTk.PhotoImage(image2)
background_label = tk.Label(root,image=background_image)
background_label.image = background_image
background_label.place(x=0,y=0)


current_path = str(os.path.dirname(os.path.realpath('__file__')))

basepath=current_path  + "\\" 

frame_no = tk.StringVar()
frame_no2 = tk.StringVar()
encode_text = tk.StringVar()
key1 = tk.StringVar()
key2 = tk.StringVar()

label_l1 = tk.Label(root, text="___Personal Protective Equipment____", font=("Algerian", 25, 'bold'),
                    background="orange", fg="white", width=90, height=2)
label_l1.place(x=0, y=0)

def shift():
    x1,y1,x2,y2 = canvas.bbox("marquee")
    if(x2<0 or y1<0): #reset the coordinates
        x1 = canvas.winfo_width()
        y1 = canvas.winfo_height()//2
        canvas.coords("marquee",x1,y1)
    else:
        canvas.move("marquee", -2, 0)
    canvas.after(1000//fps,shift)

canvas=tk.Canvas(root,bg="orange")
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



    
from datetime import datetime
from ultralytics import YOLO
import cv2
import math


def video_detection(path):
    video_capture = path
    cap = cv2.VideoCapture(video_capture)
    frame_width = int(cap.get(3))
    frame_height = int(cap.get(4))

    model = YOLO("bestest.pt")
    classNames = ['Excavator', 'Gloves', 'Hardhat', 'Ladder', 'Mask', 'NO-hardhat',
                  'NO-Mask', 'NO-Safety Vest', 'Person', 'SUV', 'Safety Cone', 'Safety Vest',
                  'bus', 'dump truck', 'fire hydrant', 'machinery', 'mini-van', 'sedan', 'semi',
                  'trailer', 'truck and trailer', 'truck', 'van', 'vehicle', 'wheel loader']

    start_time = datetime.now()
    detection_results = []

    # **Set OpenCV Window to Full Screen**
    cv2.namedWindow("Detection", cv2.WINDOW_NORMAL)
    cv2.setWindowProperty("Detection", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

    while cap.isOpened():
        success, img = cap.read()
        if not success:
            break  # Stop when video ends

        results = model(img, stream=True)

        for r in results:
            boxes = r.boxes
            for box in boxes:
                x1, y1, x2, y2 = box.xyxy[0]
                x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
                conf = math.ceil((box.conf[0] * 100)) / 100
                cls = int(box.cls[0])
                class_name = classNames[cls]
                label = f'{class_name} {conf}'
                t_size = cv2.getTextSize(label, 0, fontScale=1, thickness=2)[0]
                c2 = x1 + t_size[0], y1 - t_size[1] - 3

                color = (85, 45, 255)
                if class_name == 'Hardhat':
                    color = (0, 204, 255)
                elif class_name == "Gloves":
                    color = (222, 82, 175)
                elif class_name == "NO-hardhat":
                    color = (0, 100, 150)
                elif class_name == "Mask":
                    color = (0, 180, 255)
                elif class_name == "NO-Safety Vest":
                    color = (0, 230, 200)
                elif class_name == "Safety Vest":
                    color = (0, 266, 280)
                elif class_name == "machinery":
                    color = (85, 45, 255)

                if conf > 0.6:
                    cv2.rectangle(img, (x1, y1), (x2, y2), color, 3)
                    cv2.rectangle(img, (x1, y1), c2, color, -1, cv2.LINE_AA)
                    cv2.putText(img, label, (x1, y1 - 2), 0, 1, [255, 255, 255], thickness=1, lineType=cv2.LINE_AA)

                    if class_name in ['NO-Mask', 'NO-Safety Vest', 'NO-hardhat']:
                        detection_results.append({
                            'class': class_name,
                            'confidence': conf,
                            'bounding_box': (x1, y1, x2, y2),
                            'time': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                        })

        if (datetime.now() - start_time).seconds >= 30:
            with open('detection_results.txt', 'a') as file:
                for detection in detection_results:
                    file.write(f"[ {detection['time']} ] {detection['class']} {detection['confidence']} {detection['bounding_box']} \n")
                file.write('\n')

            start_time = datetime.now()
            detection_results = []

        cv2.imshow("Detection", img)

        key = cv2.waitKey(1) & 0xFF
        if key == ord('q') or cv2.getWindowProperty("Detection", cv2.WND_PROP_VISIBLE) < 1:
            break  # Close the window if 'q' is pressed or user closes the window

    cap.release()
    cv2.destroyAllWindows()
        
def dec_main():
    fileName = askopenfilename(initialdir='/dataset', title='Select image',
                               filetypes=[("all files", "*.*")])

    videopath = fileName
    print(fileName)
    #fn = fileName
    fn = fileName
    Sel_F = fileName.split('/').pop()
    Sel_F = Sel_F.split('.').pop(1)
    
    video_detection(fn)
    # if Sel_F != 'mp4':
    #     print("Select Video .mp4 File!!!!!!")
    # else:
        #enc_main(fn)
   
      
#def window():
   # root.destroy()
   
# def camdetection():
#     subprocess.Popen(["python", "trail.py"])

    
def window():
    cv2.destroyAllWindows()
    root.destroy()
    subprocess.run(["python", "Gui_main.py"])

button1 = tk.Button(root, text="Upload Video", command=dec_main, width=14,
                    height=1, font=('times', 20, 'bold'), bg="white", fg="black")
button1.place(x=450, y=300)  # Adjusted x position for alignment

button3 = tk.Button(root, text="EXIT", command=window, width=14,
                    height=1, font=('times', 20, 'bold'), bg="orange", fg="black")
button3.place(x=450, y=380)  # Same x position, slightly below


# button5 = tk.Button(root,text="WEBCAM",command=camdetection,width=14,height=1,font=('times',20,'bold'),bg="orange",fg="black")
# button5.place(x=450,y=460)

# if __name__ == "__main__":
#     main()
root.mainloop()
