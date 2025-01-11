import cv2
import os
import numpy as np
import time
from datetime import datetime
from PIL import ImageFont, ImageDraw, Image

# 웹캠 초기화
cap = cv2.VideoCapture(0)

# myself 폴더 생성
if not os.path.exists('myself'):
    os.makedirs('myself')

# 버튼과 필터 설정
button_x = 250
button_y = 440
button_w = 140
button_h = 30

# 필터 버튼 위치 재설정 (우상단, 세로 배열)
filter_buttons = [
    {"x": 520, "y": 20, "w": 100, "h": 30, "text": "Original"},
    {"x": 520, "y": 60, "w": 100, "h": 30, "text": "Blue"},
    {"x": 520, "y": 100, "w": 100, "h": 30, "text": "Red"},
    {"x": 520, "y": 140, "w": 100, "h": 30, "text": "Gray"}
]

current_filter = "Original"
is_capturing = False
captured_frames = []

def put_text(frame, text, position, font_size=32, color=(255,255,255)):
    pil_image = Image.fromarray(frame)
    draw = ImageDraw.Draw(pil_image)
    font = ImageFont.truetype('malgun.ttf', font_size)
    draw.text(position, text, font=font, fill=color)
    return np.array(pil_image)

def is_mouse_on_button(x, y):
    return button_x <= x <= button_x + button_w and button_y <= y <= button_y + button_h

def is_mouse_on_filter_button(x, y, button):
    return (button["x"] <= x <= button["x"] + button["w"] and 
            button["y"] <= y <= button["y"] + button["h"])

def mouse_callback(event, x, y, flags, param):
    global is_capturing, current_filter
    if event == cv2.EVENT_LBUTTONDOWN:
        if is_mouse_on_button(x, y):
            is_capturing = True
            captured_frames.clear()
        for button in filter_buttons:
            if is_mouse_on_filter_button(x, y, button):
                current_filter = button["text"]

def apply_blue_filter(frame):
    blue_filter = frame.copy()
    blue_filter[:,:,1] = blue_filter[:,:,1] * 0.7
    blue_filter[:,:,2] = blue_filter[:,:,2] * 0.7
    return blue_filter

def apply_red_filter(frame):
    red_filter = frame.copy()
    red_filter[:,:,0] = red_filter[:,:,0] * 0.7
    red_filter[:,:,1] = red_filter[:,:,1] * 0.7
    return red_filter

def apply_gray_filter(frame):
    return cv2.cvtColor(cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY), cv2.COLOR_GRAY2BGR)

def apply_current_filter(frame):
    if current_filter == "Blue":
        return apply_blue_filter(frame)
    elif current_filter == "Red":
        return apply_red_filter(frame)
    elif current_filter == "Gray":
        return apply_gray_filter(frame)
    return frame

def create_photo_strip(frames):
    h, w = frames[0].shape[:2]
    strip = np.zeros((h, w, 3), dtype=np.uint8)
    
    positions = [
        (0, 0),
        (0, w//2),
        (h//2, 0),
        (h//2, w//2)
    ]
    
    for frame, pos in zip(frames, positions):
        resized = cv2.resize(frame, (w//2, h//2))
        strip[pos[0]:pos[0]+h//2, pos[1]:pos[1]+w//2] = resized
    
    return strip

cv2.namedWindow('Webcam')
cv2.setMouseCallback('Webcam', mouse_callback)

last_capture_time = time.time()

preview_start_time = None  # 전역 변수로 선언

while True:
    ret, frame = cap.read()
    
    if ret:
        display_frame = frame.copy()
        filtered_frame = apply_current_filter(frame.copy())
        
        # 필터 버튼 그리기
        for button in filter_buttons:
            color = (0, 255, 0) if button["text"] == current_filter else (200, 200, 200)
            cv2.rectangle(display_frame, (button["x"], button["y"]), 
                         (button["x"] + button["w"], button["y"] + button["h"]), color, -1)
            text_x = button["x"] + 10
            text_y = button["y"]
            display_frame = put_text(display_frame, button["text"], 
                                   (text_x, text_y), font_size=20)
         # 촬영 버튼 그리기
        cv2.rectangle(display_frame, (button_x, button_y), 
                    (button_x + button_w, button_y + button_h), (0, 255, 0), -1)
        display_frame = put_text(display_frame, "촬영", 
                            (button_x + 45, button_y), font_size=24)

        if is_capturing:
            display_frame = put_text(display_frame, 
                                   f"촬영중... {len(captured_frames)+1}/4", (10, 30))
            
            current_time = time.time()
            if len(captured_frames) < 4 and current_time - last_capture_time >= 1:
                captured_frames.append(filtered_frame)
                last_capture_time = current_time
            
            if len(captured_frames) == 4:
                photo_strip = create_photo_strip(captured_frames)
                now = datetime.now().strftime("%Y%m%d_%H%M%S")
                cv2.imwrite(f'myself/photo_strip_{now}.jpg', photo_strip)
                cv2.imshow('Result', photo_strip)
                preview_start_time = time.time()
                is_capturing = False
                captured_frames.clear()

        # 프리뷰 창 체크 및 자동 닫기
        try:
            if preview_start_time and cv2.getWindowProperty('Result', cv2.WND_PROP_VISIBLE) >= 1:
                if time.time() - preview_start_time > 2:
                    cv2.destroyWindow('Result')
                    preview_start_time = None
        except:
            pass

        cv2.imshow('Webcam', display_frame)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()