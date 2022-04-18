# -*- coding: utf-8 -*-

import pygame
pygame.init()

screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height ))

pygame.display.set_caption("똥피하기 - 코드플레이")

bg = pygame.image.load("pygame/source/bg.png")

character = pygame.image.load("pygame/source/character.png")

character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
# character_xPos = (screen_width / 2) - (character_width / 2)
# character_yPos = screen_height - character_height
#1
# character_xPos = 0
# character_yPos = 0
#2
character_xPos = (screen_width / ) - (character_width / )
character_yPos = 0

# #3
# character_xPos = (screen_width / 100) - (character_width / 100)
# character_yPos = screen_height - character_height
#4
# character_xPos = (screen_width / 2) - (character_width / 2)
# character_yPos = 0  

# #5
# character_xPos = 
# character_yPos = 

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False 
            # print("ㅈ...ㅜㄱ...ㅇ ㅕ.....ㅈ..ㅝ...") 
    screen.blit(bg, (0, 0))
    screen.blit(character, (character_xPos, character_yPos))
    pygame.display.update()
    
pygame.quit() 
