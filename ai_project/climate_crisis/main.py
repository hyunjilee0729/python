import pygame
import sys
import os

# 파이게임 초기화
pygame.init()

# ... (기존 코드)

# 한글 폰트 설정
font_path = os.path.join("ai_project", "climate_crisis", "font1.ttf")
font_size = 26

# 폰트 초기화
pygame.font.init()
font = pygame.font.Font(font_path, font_size)

# ... (이하 생략)

import os

# 창 크기 설정
window_width = 1200
window_height = 700
window_size = (window_width, window_height)
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption("파이게임 창 크기 및 이미지, 텍스트 추가 예제")

# 배경 이미지 로드
background1_path = os.path.join("ai_project", "climate_crisis", "image", "room.jpg")
background2_path = os.path.join("ai_project", "climate_crisis", "image", "gmbg.jpg")
background1 = pygame.image.load(background1_path)
background2 = pygame.image.load(background2_path)
current_background = background1
background_rect = current_background.get_rect()
background_rect.center = (window_width // 2, window_height // 2)

# 추가 이미지 로드
extra_image_path = os.path.join("ai_project", "climate_crisis", "image", "ch1.png")
extra_image = pygame.image.load(extra_image_path)
extra_image_rect = extra_image.get_rect()
extra_image_rect.topleft = (20, 170)

# 특정 캐릭터 이미지 로드
character_image_path = os.path.join("ai_project", "climate_crisis", "image", "character.png")
character_image = pygame.image.load(character_image_path)
character_rect = character_image.get_rect()
character_rect.topleft = (500, 500)  # 캐릭터 초기 위치

# 게임 루프 내에서 캐릭터를 그리는 부분에 추가
screen.blit(character_image, character_rect)


# 새로운 추가 이미지 로드
new_extra_image_path = os.path.join("ai_project", "climate_crisis", "image", "menu.png")



# 텍스트 관리를 위한 클래스
class Text:
    def __init__(self, content, background_change=False, next_background=None, remove_extra_image=False,
                 show_extra_image=False, new_extra_image=None, new_extra_image_on_click=False):
        self.content = content
        self.surface = font.render(self.content, True, (255, 255, 255))
        self.rect = self.surface.get_rect()
        self.background_change = background_change
        self.next_background = next_background
        self.remove_extra_image = remove_extra_image
        self.show_extra_image = show_extra_image
        self.new_extra_image = new_extra_image
        self.new_extra_image_on_click = new_extra_image_on_click

        # 초기 텍스트 리스트 생성
texts = [
    Text("안녕!! 내 이름은 자연이야^^"),
    Text("나는 산림을 너무 좋아해서 매주 산림에서 놀아~"),
    Text("오늘도 나는 산림에 가서 놀거야!"),
    Text("뭐? 나랑 같이 가고 싶다구?"),
    Text("좋아~! 특별히 이 자연님이랑 같이 놀 수 있는 영광을 줄게!!"),
    Text("여기가 내가 자주 놀러오는 산림이야..!", background_change=True),
    Text("뭐야..! 산림이 왜 다 이 모양이지??"),
    Text("나무들이 전부 베여졌잖아..!"),
    Text("아..! 그러고보니 나무들을 막 없애버리는 나쁜... ....어쨌든 있다고 했는데..!"),
    Text("그 사람들이 벌인 짓인건가..?"),
    Text("안 되겠다..! 산림인 자연님이 직접 나서서 산림을 지켜야겠어!"),
    Text("뭐? 나를 도와주겠다구??"),
    Text("너~무 좋지~! 산림도 분명 너에게 고마워할거야!"),
     Text("그럼, 산림을 지키러 고고~~", remove_extra_image=True, new_extra_image=new_extra_image_path),]

# 현재 텍스트 인덱스
current_text_index = 0

# 이전 배경 저장 변수
previous_background = None
previous_background_rect = None

# 추가 이미지 저장 변수
current_extra_image = extra_image

# ... (기존 코드)

# 게임 루프

# 게임 루프 내에서 이벤트 처리 부분에 추가
for event in pygame.event.get():
    if event.type == pygame.MOUSEBUTTONDOWN:
        mouse_pos = pygame.mouse.get_pos()
        if character_rect.collidepoint(mouse_pos):
            print("Character caught!")  # 캐릭터가 클릭되었을 때 수행할 동작 추가

# 게임 루프# 게임 루프
# 게임 루프
show_new_extra_image = True  # 새로운 추가 이미지를 표시할지 여부
game_start_time = 0  # 게임 시작 시간 초기화
new_extra_image = None  # 새로운 추가 이미지 객체 초기화
new_extra_image_rect = None  # 새로운 추가 이미지의 rect 초기화

clock = pygame.time.Clock()  # pygame Clock 객체 생성

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # 화면 클릭 시 다음 텍스트로 넘어가기
            current_text_index += 1
            if current_text_index < len(texts):
                # 현재 텍스트가 배경 변경을 요청하거나 추가 이미지를 삭제해야 하는 경우
                if texts[current_text_index].background_change:
                    previous_background = current_background
                    previous_background_rect = background_rect
                    current_background = texts[current_text_index].next_background if texts[
                        current_text_index].next_background else background2
                    background_rect = current_background.get_rect(center=(window_width // 2, window_height // 2))

                if texts[current_text_index].remove_extra_image:
                    extra_image_rect.topleft = (window_width, window_height)  # 화면 밖으로 이동하여 숨기기

                if texts[current_text_index].show_extra_image:
                    extra_image_rect.topleft = (20, 170)  # 추가 이미지 표시 위치로 이동

                if texts[current_text_index].new_extra_image and not show_new_extra_image:
                    # 새로운 추가 이미지를 표시
                    new_extra_image_path = os.path.join("ai_project", "climate_crisis", "image", "menu.png")
                    new_extra_image = pygame.image.load(new_extra_image_path)
                    new_extra_image_rect = new_extra_image.get_rect(center=(window_width // 2, window_height // 2))
                    show_new_extra_image = True  # 새로운 추가 이미지가 표시된 후에는 True로 설정
                    game_start_time = pygame.time.get_ticks()  # 게임 시작 시간 기록

    # 게임이 시작되었는지 여부에 따라 제한 시간을 확인
    if show_new_extra_image:
        elapsed_time = (pygame.time.get_ticks() - game_start_time) // 1000  # 경과 시간(초)
        if elapsed_time >= 30:  # 제한 시간 30초
            print("Game Over!")
            pygame.quit()
            sys.exit()

    # 배경 그리기
    screen.blit(current_background, background_rect)

    # 추가 이미지 그리기
    screen.blit(extra_image, extra_image_rect)

    # 새로운 추가 이미지 그리기
    if current_text_index < len(texts) and texts[current_text_index].new_extra_image and show_new_extra_image and new_extra_image is not None:
        screen.blit(new_extra_image, new_extra_image_rect)

    # 현재 텍스트 그리기 (맨아래 가운데에 위치)
    if current_text_index < len(texts):
        texts[current_text_index].rect.midbottom = (window_width // 2, window_height)
        screen.blit(texts[current_text_index].surface, texts[current_text_index].rect)

    # 시간 표시
    font_time = pygame.font.SysFont(None, 36)
    time_text = font_time.render(f"Time: {elapsed_time}s", True, (255, 255, 255))
    screen.blit(time_text, (10, 10))

    pygame.display.flip()
    clock.tick(60)  # 60 FPS로 설정
