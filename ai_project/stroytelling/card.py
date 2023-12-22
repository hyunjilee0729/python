import pygame
import sys
import random

# 파이게임 초기화
pygame.init()

# 창 크기 설정
screen_width = 800
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pygame Window with Rotating, Scaling, and Falling Images")

# 사용자가 제공한 이미지 파일 경로를 지정하세요
user_image_path = "ai_project/stroytelling/image/card.jpg"
additional_image_path = "ai_project/stroytelling/image/snow.png"

# 이미지 로드
user_image = pygame.image.load(user_image_path)
user_image_rect = user_image.get_rect()
user_image_rect.center = (screen_width // 2, screen_height // 2)

# 추가 이미지를 여러 개 관리하기 위한 리스트
additional_images = []
num_additional_images = 20  # 원하는 이미지 개수 설정

for _ in range(num_additional_images):
    image = pygame.image.load(additional_image_path)
    initial_size = random.randint(50, 200)  # 초기 크기를 랜덤하게 설정
    image = pygame.transform.scale(image, (initial_size, initial_size))
    image_rect = image.get_rect()

    # 초기 추가 이미지 위치 설정 (랜덤한 위치, 맨 위쪽에서 시작)
    image_rect.x = random.randint(0, screen_width)
    image_rect.y = 0

    # 추가 이미지의 떨어지는 속도를 랜덤하게 설정
    falling_speed = random.randint(1, 5)
    
    # 추가 이미지의 회전 속도를 랜덤하게 설정
    rotation_speed = random.uniform(0.1, 0.5)

    additional_images.append({
        'image': image,
        'rect': image_rect,
        'falling_speed': falling_speed,
        'rotation_angle': 0,
        'rotation_speed': rotation_speed,
        'size_change_speed': random.uniform(-0.1, 0.1)  # 크기 변화 속도를 랜덤하게 설정
    })

# 배경 이미지 로드
background_image_path = "ai_project/stroytelling/image/card.jpg"
background_image = pygame.image.load(background_image_path)
background_image = pygame.transform.scale(background_image, (screen_width, screen_height))

# 음악 로드 및 재생
music_path = "ai_project/stroytelling/image/song.mp3"  # 음악 파일 경로를 지정하세요
pygame.mixer.music.load(music_path)
pygame.mixer.music.play(-1)  # -1은 반복 재생을 나타냅니다.

music_paused = False  # 노래 일시 정지 상태를 나타내는 변수

# 게임 루프
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.mixer.music.stop()  # 프로그램 종료 시 음악 정지
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # 마우스 왼쪽 버튼 클릭
            if music_paused:
                pygame.mixer.music.unpause()  # 노래 재생 재개
            else:
                pygame.mixer.music.pause()  # 노래 일시 정지
            music_paused = not music_paused  # 상태 업데이트

    # 화면 클리어 및 배경 이미지 그리기
    screen.blit(background_image, (0, 0))

    # 이미지를 화면에 그림
    screen.blit(user_image, user_image_rect)

    for image_info in additional_images:
        # 크기가 변하는 이미지를 화면에 그림
        scaled_image = pygame.transform.scale(image_info['image'], (image_info['rect'].width, image_info['rect'].height))
        rotated_image = pygame.transform.rotate(scaled_image, image_info['rotation_angle'])
        rotated_rect = rotated_image.get_rect(center=image_info['rect'].center)
        screen.blit(rotated_image, rotated_rect)

        # 이미지를 떨어뜨리고 회전 및 크기를 조절
        image_info['rect'].y += image_info['falling_speed']  # 이미지를 아래로 이동
        image_info['rotation_angle'] += image_info['rotation_speed']

        # 크기 변화 적용
        new_width = max(50, min(image_info['rect'].width + image_info['size_change_speed'], 200))
        new_height = max(50, min(image_info['rect'].height + image_info['size_change_speed'], 200))
        image_info['rect'].width = new_width
        image_info['rect'].height = new_height

        if image_info['rect'].y > screen_height:
            # 이미지가 화면 아래로 벗어나면 다시 맨 위쪽에서 랜덤한 위치로 설정
            image_info['rect'].x = random.randint(0, screen_width)
            image_info['rect'].y = 0

            # 추가 이미지의 떨어지는 속도를 다시 랜덤하게 설정
            image_info['falling_speed'] = random.randint(1, 5)
            image_info['rotation_speed'] = random.uniform(0.1, 0.5)
            image_info['size_change_speed'] = random.uniform(-0.1, 0.1)

    # 화면 업데이트
    pygame.display.flip()
