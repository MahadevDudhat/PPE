from datetime import datetime
from ultralytics import YOLO
import cv2
import math
import os
import winsound  # For alarm functionality on Windows
import pyttsx3  # For voice alert
import threading  # For running speech synthesis in a separate thread

def speak_alert():
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)  # Adjust speech rate for better responsiveness
    engine.say("No Safety Compliances followed")
    engine.runAndWait()

def camera_detection():
    cap = cv2.VideoCapture(0)
    cap.set(cv2.CAP_PROP_BUFFERSIZE, 1)  # Reduce buffer size for faster response
    cap.set(cv2.CAP_PROP_FPS, 30)  # Ensure smooth frame capture
    cap.set(3, 800)  # Set width
    cap.set(4, 800)  # Set height
    model = YOLO("bestest.pt")
    classNames = ['Excavator', 'Gloves', 'Hardhat', 'Ladder', 'Mask', 'NO-hardhat',
                  'NO-Mask', 'NO-Safety Vest', 'Person', 'SUV', 'Safety Cone', 'Safety Vest',
                  'bus', 'dump truck', 'fire hydrant', 'machinery', 'mini-van', 'sedan', 'semi',
                  'trailer', 'truck and trailer', 'truck', 'van', 'vehicle', 'wheel loader']
    
    colors = {
        'Hardhat': (0, 204, 255), 'Gloves': (222, 82, 175), 'NO-hardhat': (0, 100, 150),
        'Mask': (0, 180, 255), 'NO-Safety Vest': (0, 230, 200), 'Safety Vest': (0, 266, 280),
        'machinery': (85, 45, 255), 'Person': (0, 255, 0), 'Vehicle': (255, 0, 0),
        'default': (85, 45, 255)
    }

    # Create directory if it doesn't exist
    folder_name = "camdet"
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
    
    # Create a single session file
    session_timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    file_path = os.path.join(folder_name, f"{session_timestamp}.txt")

    while True:
        success, img = cap.read()
        if not success:
            print("Failed to capture image")
            break
        
        results = model(img, stream=True)
        detections = []
        alarm_triggered = False
        safe_classes_detected = False

        for r in results:
            boxes = r.boxes
            for box in boxes:
                x1, y1, x2, y2 = map(int, box.xyxy[0])
                conf = math.ceil((box.conf[0] * 100)) / 100
                cls = int(box.cls[0])
                class_name = classNames[cls]
                label = f'{class_name} {conf}'
                color = colors.get(class_name, colors['default'])
                cv2.rectangle(img, (x1, y1), (x2, y2), color, 2)
                cv2.putText(img, label, (x1, y1 - 2), 0, 0.6, [255, 255, 255], thickness=1, lineType=cv2.LINE_AA)
                detections.append(f"{class_name} {conf} at ({x1}, {y1}, {x2}, {y2})")
                
                # Stop alarm if safety-compliant classes are detected
                if class_name in ['Hardhat', 'Gloves', 'Mask', 'Safety Vest']:
                    safe_classes_detected = True
                
                # Trigger alarm if non-compliant classes are detected
                if class_name in ['NO-hardhat', 'NO-Mask', 'NO-Safety Vest']:
                    alarm_triggered = True
        
        # If specified non-compliant classes are detected and no safe classes, trigger alarm
        if alarm_triggered and not safe_classes_detected:
            winsound.Beep(1000, 500)  # Beep sound at 1000 Hz for 500 ms
            threading.Thread(target=speak_alert, daemon=True).start()
        
        # Append detection results to the session file
        if detections:
            with open(file_path, 'a') as file:
                file.write("\n".join(detections) + "\n")
        
        cv2.imshow("Camera Detection", img)
        key = cv2.waitKey(1)
        if key & 0xFF == ord('q') or key == 27:  # Press 'q' or 'Esc' to exit
            break
        if cv2.getWindowProperty("Camera Detection", cv2.WND_PROP_VISIBLE) < 1:
            break

    cap.release()
    cv2.destroyAllWindows()

# Run the camera detection function
camera_detection()
