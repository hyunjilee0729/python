import cv2
import time
from PIL import Image, ImageDraw, ImageFont
import numpy as np
import pyttsx3

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

if face_cascade.empty():
    print("Error: Could not load face cascade.")
    exit()

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Could not open video capture.")
    exit()

engine = pyttsx3.init()

def draw_text(img, text, pos, font_size=30, color=(255, 255, 255)):
    img_pil = Image.fromarray(img)
    draw = ImageDraw.Draw(img_pil)
    font = ImageFont.truetype("malgun.ttf", font_size)
    draw.text(pos, text, font=font, fill=color)
    return np.array(img_pil)

def speak(text):
    engine.say(text)
    engine.runAndWait()

last_print_time = time.time()

while True:
    ret, frame = cap.read()
    if not ret:
        print("Error: Could not read frame.")
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    if len(faces) == 0:
        # 얼굴이 인식되지 않으면 "No one Detected" 메시지를 검정색 배경에 출력
        frame = cv2.rectangle(frame, (0, 0), (frame.shape[1], frame.shape[0]), (0, 0, 0), -1)
        frame = draw_text(frame, "No one Detected", (50, 50))
    elif len(faces) == 1:
        # 얼굴이 1명 인식되면 콘솔에 메시지 출력 및 TTS로 음성 출력
        print("어서오세요")
        speak("어서오세요")
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
    elif len(faces) >= 2:
        # 얼굴이 2명 이상 인식되면 빨간색 배경에 "한 명씩 입장하세요" 메시지를 화면에 출력 및 TTS로 음성 출력
        frame = cv2.rectangle(frame, (0, 0), (frame.shape[1], frame.shape[0]), (0, 0, 255), -1)
        frame = draw_text(frame, "한 명씩 입장하세요", (50, 50))
        print("한 명씩 입장하세요")
        speak("한 명씩 들어오세요")

    cv2.imshow('Face Deter', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    time.sleep(0.3)

cap.release()
cv2.destroyAllWindows()