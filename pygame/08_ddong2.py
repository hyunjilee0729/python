# -*- coding: utf-8 -*-

import pygame
import random

pygame.init()

screen_width = 800
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height ))

pygame.display.set_caption("똥피하기 - 코드플레이")

clock = pygame.time.Clock()

bg = pygame.image.load("pygame/source/bg2.png")

character = pygame.image.load("pygame/source/character.png")

character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_xPos = (screen_width / 2) - (character_width / 2)
character_yPos = (screen_height /2) - (character_height /2) 

enemy1 = pygame.image.load("pygame/source/enemy.png")
enemy1_size = enemy1.get_rect().size
enemy1_width = enemy1_size[0]
enemy1_height = enemy1_size[1]
enemy1_xPos = random.randint(0, (screen_width / 2 - enemy1_width / 2))
enemy1_yPos = 0 

enemy1_speed = 5

enemy2 = pygame.image.load("pygame/source/enemy.png")
enemy2_size = enemy2.get_rect().size
enemy2_width = enemy2_size[0]
enemy2_height = enemy2_size[1]
enemy2_xPos = screen_width / 2 - enemy2_width 
enemy2_yPos = enemy2_yPos = random.randint(0, (screen_height - enemy2_height))

enemy2_speed = 5

enemy3 = pygame.image.load("pygame/source/enemy.png")
enemy3_size = enemy3.get_rect().size
enemy3_width = enemy3_size[0]
enemy3_height = enemy3_size[1]
enemy3_xPos = random.randint(0, (screen_width / 2 - enemy3_width / 2))
enemy3_yPos = screen_height - enemy3_height

enemy3_speed = 5

enemy4 = pygame.image.load("pygame/source/enemy.png")
enemy4_size = enemy4.get_rect().size
enemy4_width = enemy4_size[0]
enemy4_height = enemy4_size[1]
enemy4_xPos = 0 
enemy4_yPos = random.randint(0, (screen_height - enemy4_height))

enemy4_speed = 5

game_font = pygame.font.Font(None, 40)

total_time = 10

start_ticks = pygame.time.get_ticks()


to_x = 0
to_y = 0
character_speed = 10

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

    enemy1_rect = enemy1.get_rect()
    enemy1_rect.left = enemy1_xPos
    enemy1_rect.top = enemy1_yPos

    enemy1_yPos += enemy1_speed

    if enemy1_yPos > screen_height:
        enemy1_yPos = enemy1_height * -1
        enemy1_xPos = random.randint(0, (screen_width - enemy1_width))
        enemy1_speed = random.randint(5, 8) 

    enemy3_rect = enemy3.get_rect()
    enemy3_rect.left = enemy1_xPos
    enemy3_rect.top = enemy3_yPos

    enemy3_yPos -= enemy3_speed

    if enemy3_yPos < 0:
        enemy3_yPos = screen_height - enemy3_height
        enemy3_xPos = random.randint(0, (screen_width - enemy3_width))
        enemy3_speed = random.randint(5, 8) 

    enemy2_rect = enemy2.get_rect()
    enemy2_rect.left = enemy2_xPos
    enemy2_rect.top = enemy2_yPos

    enemy2_xPos -= enemy2_speed

    if enemy2_xPos < 0:
        enemy2_yPos = random.randint(0, (screen_height - enemy4_height))
        enemy2_xPos = screen_width - enemy2_width
        enemy2_speed = random.randint(5, 8) 

    enemy4_rect = enemy4.get_rect()
    enemy4_rect.left = enemy4_xPos
    enemy4_rect.top = enemy4_yPos

    enemy4_xPos += enemy4_speed

    if enemy4_xPos > screen_width:
        enemy4_yPos = random.randint(0, (screen_height - enemy4_height))
        enemy4_xPos = 0
        enemy4_speed = random.randint(5, 8) 




    if character_rect.colliderect(enemy1_rect) or character_rect.colliderect(enemy2_rect) or character_rect.colliderect(enemy3_rect) or character_rect.colliderect(enemy4_rect):
        print("충돌! 충돌!")
        running = False

    elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000
    timer = game_font.render(str(int(total_time - elapsed_time)), True, (0, 0, 0))

    # if total_time - elapsed_time <= 0:
    #     print("타임아웃")
    #     running = False

            # print("2022년.4월.22일. 신서윤 사망. 사인, 증오의 매") 
    screen.blit(bg, (0, 0))
    screen.blit(character, (character_xPos, character_yPos))
    screen.blit(enemy1, (enemy1_xPos, enemy1_yPos))
    screen.blit(enemy2, (enemy2_xPos, enemy2_yPos))
    screen.blit(enemy3, (enemy3_xPos, enemy3_yPos))
    screen.blit(enemy4, (enemy4_xPos, enemy4_yPos))
    # screen.blit(timer, (10, 10))
    
    pygame.display.update()
    
pygame.time.delay(2000)
pygame.quit() 
