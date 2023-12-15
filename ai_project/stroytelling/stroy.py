import pygame
import sys
import os

# Pygame 초기화
pygame.init()

# 화면 크기 설정
screen_size = (1024, 1024)
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("Image Slideshow")

# 이미지 파일 경로 설정
image_folder = "ai_project/stroytelling/image/"  # 이미지 파일이 들어있는 폴더의 경로로 변경해주세요.
image_files = ["01.png", "02.png", "03.png", "04.png", "05.png", "06.png", "07.png", "08.png"]
image_paths = [os.path.join(image_folder, file) for file in image_files]

# 이미지 로드
images = [pygame.image.load(path) for path in image_paths]
image_rects = [image.get_rect() for image in images]

# 현재 표시 중인 이미지의 인덱스
current_image_index = 0

# 게임 루프
while True:
    # 이벤트 처리
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # 마우스 클릭 시 다음 이미지로 전환
            current_image_index = (current_image_index + 1) % len(images)

    # 화면 업데이트

    # 화면을 흰색으로 채우기
    screen.fill((255, 255, 255))

    # 현재 이미지를 화면에 그리기
    screen.blit(images[current_image_index], image_rects[current_image_index])

    # 화면 업데이트
    pygame.display.flip()

    # 초당 프레임 설정
    pygame.time.Clock().tick(60)
