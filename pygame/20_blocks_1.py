# -*- coding: utf-8 -*-
import pygame
import random

pygame.init()

screen_width = 640
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height ))

pygame.display.set_caption("벽돌깨기")

bar_width = 150
bar_height = 25

bar_xPos = screen_width / 2 - bar_width / 2
bar_yPos = screen_height - bar_height

bar_rect = pygame.Rect(bar_xPos, bar_yPos, bar_width, bar_height)
bar_to_X = 0

ball_size = 20

ball_xPos = screen_width / 2
ball_yPos = screen_height - bar_height - ball_size

ball_rect = pygame.Rect(ball_xPos, ball_yPos, ball_size * 2, ball_size * 2)
ball_rect.center = (ball_xPos, ball_yPos)

ball_x_speed = 0.3
ball_y_speed = 0.3

block_width = screen_width / 10
block_height = screen_height / 20

block_xPos = 0
block_yPos = 0

blocks = [[] for _ in range(10)]
block_color = [[], [], [], [], [], [], [], [], [], []]

for i in range(10):
    for j in range(3):
        blocks[i].append(pygame.Rect(i*block_width, j*block_height, block_width, block_height))
        block_color[i].append((random.randrange(256), random.randrange(256), random.randrange(256)))

print(blocks)
print(block_color)

mouse_xPos = 0
mouse_yPos = 0

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False 
        
        if event.type == pygame.MOUSEMOTION:
            mouse_xPos, mouse_yPos = pygame.mouse.get_pos()
            if mouse_xPos - bar_width / 2 >= 0 and mouse_xPos + bar_width / 2 <= screen_width:
                bar_xPos = mouse_xPos - bar_width / 2
                bar_rect.left = mouse_xPos - bar_width / 2

    screen.fill((200, 200, 200))

    bar_xPos += bar_to_X

    if bar_xPos < 0:
        bar_xPos = 0
    if bar_xPos > screen_width - bar_width:
        bar_rect.left = bar_xPos

    pygame.draw.rect(screen, (90,90, 200), bar_rect)

    if ball_xPos - ball_size <= 0:
        ball_x_speed = -ball_x_speed
    elif ball_xPos >= screen_width - ball_size:
        ball_x_speed = -ball_x_speed

    if ball_yPos - ball_size <= 0:
        ball_y_speed = -ball_y_speed
    elif ball_yPos >= screen_height - ball_size:
        ball_y_speed = -ball_y_speed

    ball_xPos += ball_x_speed
    ball_yPos += ball_y_speed

    ball_rect.center = (ball_xPos, ball_yPos )
    pygame.draw.circle(screen, (255, 255, 255), (ball_xPos, ball_yPos), ball_size)

    if ball_rect.colliderect(bar_rect):
        ball_y_speed *= -1
    
    pygame.draw.rect(screen, (90, 90, 255), bar_rect)
    pygame.draw.circle(screen, (255, 255, 255), (ball_xPos, ball_yPos), ball_size)

    for i in range(10):
        for j in range(3):
            if blocks[i][j]:
                pygame.draw.rect(screen, block_color[i][j], blocks[i][j])
                blocks[i][j].topleft = (i* block_width,  j * block_height)

                if ball_rect.colliderect(blocks[i][j]):
                    ball_x_speed *= -1
                    ball_y_speed *= -1
                    blocks[i][j] = 0

    pygame.display.update()

pygame.quit()