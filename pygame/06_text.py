# -*- coding: utf-8 -*-

import pygame
pygame.init()

screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height ))

pygame.display.set_caption("똥피하기 - 코드플레이")

clock = pygame.time.Clock()

bg = pygame.image.load("pygame/source/bg.png")

character = pygame.image.load("pygame/source/character.png")

character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_xPos = (screen_width / 2) - (character_width / 2)
character_yPos = screen_height - character_height

enemy = pygame.image.load("pygame/source/enemy.png")
enemy_size = enemy.get_rect().size
enemy_width = enemy_size[0]
enemy_height = enemy_size[1]
enemy_xPos = (screen_width / 2) - (enemy_width / 2)
enemy_yPos = (screen_height / 2 - enemy_height / 2)

game_font = pygame.font.Font(None, 40)

total_time = 10

start_ticks = pygame.time.get_ticks()

to_x = 0
to_y = 0

character_speed = 1

running = True
while running:
    dt = clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False 
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_x -= 1
            elif event.key == pygame.K_RIGHT:
                to_x += 1
            elif event.key == pygame.K_UP:
                to_y -= 1
            elif event.key == pygame.K_DOWN:
                to_y += 1
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0
    

    character_xPos += to_x * dt
    character_yPos += to_y * dt 

    if character_xPos < 0:
        character_xPos = 0
    elif character_xPos > screen_width - character_width:
        character_xPos = screen_width - character_width

    if character_yPos < 0:
        character_yPos = 0
    elif character_yPos > screen_height - character_height:
        character_yPos = screen_height - character_height

    character_rect = character.get_rect()
    character_rect.left = character_xPos    
    character_rect.top = character_yPos

    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_xPos
    enemy_rect.top = enemy_yPos

    if character_rect.colliderect(enemy_rect):
        print("충돌! 충돌!")
        running = False

    elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000
    timer = game_font.render(str(int(total_time - elapsed_time)), True, (0, 0, 0))

    if total_time - elapsed_time <= 0:
        print("타임아웃")
        running = False

            # print("2022년.4월.22일. 신서윤 사망. 사인, 증오의 매") 
    screen.blit(bg, (0, 0))
    screen.blit(character, (character_xPos, character_yPos))
    screen.blit(enemy, (enemy_xPos, enemy_yPos))
    screen.blit(timer, (10, 10))
    
    pygame.display.update()
    
pygame.quit() 
