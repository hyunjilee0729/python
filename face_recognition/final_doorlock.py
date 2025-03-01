import tkinter as tk
import cv2
from PIL import Image, ImageTk
import serial
import time

# Initialize the main window
root = tk.Tk()
root.title("Door Lock System")
root.geometry("800x600")

# Create a label to display the video feed
video_label = tk.Label(root)
video_label.pack()

# Create a label for the message
message_label = tk.Label(root, text="", font=("Helvetica", 16))
message_label.pack(pady=20)

# Load the pre-trained face detection model
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Function to update the video feed
def update_video():
    ret, frame = cap.read()
    if ret:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

        if len(faces) > 0:
            message_label.config(text="비밀번호를 입력하세요")
        else:
            message_label.config(text="")

        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

        img = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
        imgtk = ImageTk.PhotoImage(image=img)
        video_label.imgtk = imgtk
        video_label.configure(image=imgtk)
    
    video_label.after(10, update_video)

# Function to read from Arduino
def read_from_arduino():
    if arduino.in_waiting > 0:
        data = arduino.readline().decode('utf-8').strip()
        if data:  # Only update if data is not empty
            message_label.config(text=f"Button pressed: {data}")
    root.after(100, read_from_arduino)

# Open the camera
cap = cv2.VideoCapture(0)

# Start the video update loop
update_video()

# Initialize serial communication with Arduino
arduino = serial.Serial('COM14', 9600, timeout=1)
time.sleep(2)  # Wait for the serial connection to initialize

# Start reading from Arduino
read_from_arduino()

# Run the application
root.mainloop()

# Release the camera when the window is closed
cap.release()
cv2.destroyAllWindows()
arduino.close()