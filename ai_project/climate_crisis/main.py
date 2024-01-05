import pygame
import sys

# 파이게임 초기화
pygame.init()

# 창 크기 설정
window_width = 1200
window_height = 700
window_size = (window_width, window_height)
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption("파이게임 창 크기 및 이미지, 텍스트 추가 예제")

# 배경 이미지 로드
background_path = "background_image.png"
background = pygame.image.load(background_path)
background_rect = background.get_rect()
background_rect.center = (window_width // 2, window_height // 2)

# 추가 이미지 로드
extra_image_path = "extra_image.png"
extra_image = pygame.image.load(extra_image_path)
extra_image_rect = extra_image.get_rect()
extra_image_rect.topleft = (20, 170)

# 한글 폰트 설정
font_path = "your_korean_font.ttf"  # 한글 폰트 파일의 경로
font_size = 36
font = pygame.font.Font(font_path, font_size)

# 텍스트 관리를 위한 클래스
class Text:
    def __init__(self, content, position):
        self.content = content
        self.surface = font.render(self.content, True, (255, 255, 255))
        self.rect = self.surface.get_rect()
        self.rect.topleft = position

# 초기 텍스트 리스트 생성
texts = [
    Text("안녕하세요, 파이게임!", (window_width // 2, window_height - 10)),
    Text("다른 자막도 추가할 수 있어요.", (window_width // 2, window_height - 50)),
    # 다른 텍스트가 필요하면 여기에 추가
]

# 게임 루프
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # 게임 로직 및 그리기 코드는 여기에 추가

    # 배경 이미지를 화면에 그리기
    screen.blit(background, background_rect)

    # 추가 이미지를 화면에 그리기
    screen.blit(extra_image, extra_image_rect)

    # 텍스트들을 화면에 그리기
    for text in texts:
        screen.blit(text.surface, text.rect)

    # 화면 업데이트
    pygame.display.flip()
