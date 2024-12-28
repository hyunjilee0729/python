import pygame
import random

# 초기화
pygame.init()

# 배경음악 설정
pygame.mixer.init()
pygame.mixer.music.load("python_data_A/Tin_Spirit.mp3")  # 배경음악 파일 경로
pygame.mixer.music.play(-1)  # 무한 반복 재생

# 화면 설정
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("계단 오르기 게임")

# 색상 설정
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
blue = (0, 0, 255)  # 파란색 추가

# 폰트 설정
font = pygame.font.Font("C:/Windows/Fonts/malgun.ttf", 36)

# 플레이어 설정
player_size = 50
player_x = screen_width // 2
player_y = screen_height - player_size
player_speed = 10

# 계단 설정
stair_width = 150  # 계단 폭을 넓힘
stair_height = 20
stairs = []
stair_frequency = 10  # 계단 생성 빈도 (프레임 수)

# 아이템 설정
item_size = 30
items = []
item_frequency = 50  # 아이템 생성 빈도 (프레임 수)

# 게임 루프
running = True
clock = pygame.time.Clock()
frame_count = 0
start_ticks = pygame.time.get_ticks()  # 게임 시작 시간
score = 0

while running:
    screen.fill(white)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x - player_speed > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x + player_speed < screen_width - player_size:
        player_x += player_speed
    
    # 계단 생성
    if frame_count % stair_frequency == 0:
        stair_x = random.randint(0, screen_width - stair_width)
        stair_speed = random.randint(15, 20)  # 계단 속도를 15에서 20으로 랜덤하게 설정
        stairs.append({"rect": pygame.Rect(stair_x, 0, stair_width, stair_height), "speed": stair_speed})
    
    # 아이템 생성
    if frame_count % item_frequency == 0:
        item_x = random.randint(0, screen_width - item_size)
        item_speed = random.randint(10, 15)  # 아이템 속도를 랜덤하게 설정
        items.append({"rect": pygame.Rect(item_x, 0, item_size, item_size), "speed": item_speed})
    
    # 계단 이동
    for stair in stairs:
        stair["rect"].y += stair["speed"]
        if stair["rect"].colliderect(pygame.Rect(player_x, player_y, player_size, player_size)):
            running = False
        pygame.draw.rect(screen, black, stair["rect"])
    
    # 아이템 이동 및 충돌 처리
    for item in items:
        item["rect"].y += item["speed"]
        if item["rect"].colliderect(pygame.Rect(player_x, player_y, player_size, player_size)):
            score += 1
            items.remove(item)
        pygame.draw.polygon(screen, blue, [  # 파란색으로 변경
            (item["rect"].x + item_size // 2, item["rect"].y),
            (item["rect"].x + item_size * 3 // 4, item["rect"].y + item_size // 3),
            (item["rect"].x + item_size, item["rect"].y + item_size // 2),
            (item["rect"].x + item_size * 3 // 4, item["rect"].y + item_size * 2 // 3),
            (item["rect"].x + item_size // 2, item["rect"].y + item_size),
            (item["rect"].x + item_size // 4, item["rect"].y + item_size * 2 // 3),
            (item["rect"].x, item["rect"].y + item_size // 2),
            (item["rect"].x + item_size // 4, item["rect"].y + item_size // 3)
        ])
    
    # 플레이어 그리기
    pygame.draw.rect(screen, red, (player_x, player_y, player_size, player_size))
    
    # 계단 제거
    stairs = [stair for stair in stairs if stair["rect"].y < screen_height]
    
    # 아이템 제거
    items = [item for item in items if item["rect"].y < screen_height]
    
    # 경과 시간 표시
    elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000  # 초 단위로 변환
    timer_text = font.render(f"Time: {elapsed_time:.2f} s", True, black)
    screen.blit(timer_text, (10, 10))
    
    # 점수 표시
    score_text = font.render(f"Score: {score}", True, black)
    screen.blit(score_text, (10, 50))
    
    pygame.display.flip()
    clock.tick(30)
    frame_count += 1

# 게임 종료 메시지
screen.fill(white)
game_over_text = font.render("게임 오버!", True, red)
screen.blit(game_over_text, (screen_width // 2 - game_over_text.get_width() // 2, screen_height // 2 - game_over_text.get_height() // 2))
final_time_text = font.render(f"최종 시간: {elapsed_time:.2f} s", True, black)
screen.blit(final_time_text, (screen_width // 2 - final_time_text.get_width() // 2, screen_height // 2 + game_over_text.get_height()))
final_score_text = font.render(f"최종 점수: {score}", True, black)
screen.blit(final_score_text, (screen_width // 2 - final_score_text.get_width() // 2, screen_height // 2 + game_over_text.get_height() + final_time_text.get_height()))
pygame.display.flip()
pygame.time.wait(3000)  # 3초 동안 메시지 표시

pygame.quit()