import pygame
import sys

# Pygame 초기화
pygame.init()

# 창 크기 설정
width, height = 1024, 1024
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("1024x1024 정사각형")

# 게임 루프
while True:
    # 이벤트 처리
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # 화면 업데이트
    pygame.display.flip()

import pygame
import sys

# Pygame 초기화
pygame.init()

# 창 크기 설정
width, height = 1024, 1024
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("1024x1024 정사각형")

# 이미지 불러오기
image_path = "ai_project/stroytelling/image/01.png"  # 사용하려는 이미지의 경로를 입력하세요
image = pygame.image.load(image_path)
image = pygame.transform.scale(image, (200, 200))  # 이미지 크기를 조정

# 이미지 위치 설정
image_x, image_y = (width - 200) // 2, (height - 200) // 2

# 게임 루프
while True:
    # 이벤트 처리
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # 화면에 이미지 표시
    screen.fill((255, 255, 255))  # 화면을 흰색으로 채우기
    screen.blit(image, (image_x, image_y))

    # 화면 업데이트
    pygame.display.flip()
