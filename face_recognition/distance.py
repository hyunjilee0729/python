import pygame
import serial
import time
import cv2

# 시리얼 포트 설정
ser = serial.Serial('COM12', 9600)  # COM 포트는 아두이노가 연결된 포트로 변경

# 파이게임 초기화
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Ultrasonic Sensor Visualization")

# 폰트 설정
font = pygame.font.Font(None, 36)

# 카메라 설정
cap = cv2.VideoCapture(0)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if ser.in_waiting > 0:
        distance = ser.readline().decode('utf-8').strip()
        try:
            distance = int(distance)
        except ValueError:
            continue

        if distance > 20:  # 초음파 값이 20을 넘으면 카메라 켜기
            ret, frame = cap.read()
            if ret:
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                frame = cv2.transpose(frame)
                frame = cv2.resize(frame, (600, 800))  # 프레임을 창 크기에 맞게 조정
                frame = pygame.surfarray.make_surface(frame)
                screen.blit(frame, (0, 0))
        else:
            screen.fill((0, 0, 0))  # 초음파 값이 20 이하이면 검은 화면

        # 텍스트 렌더링
        text = font.render(f"Distance: {distance} cm", True, (255, 255, 255))
        screen.blit(text, (10, 10))

        pygame.display.flip()

    time.sleep(0.1)

cap.release()
pygame.quit()
ser.close()