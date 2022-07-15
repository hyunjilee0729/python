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

ball_size = 20

ball_xPos = screen_width / 2
ball_yPos = screen_height - bar_height - ball_size

ball_rect = pygame.Rect(ball_xPos, ball_yPos, ball_size * 2, ball_size * 2)
ball_rect.center = (ball_xPos, ball_yPos)

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

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False 

    screen.fill((200, 200, 100))
    pygame.draw.rect(screen, (90, 90, 255), bar_rect)
    pygame.draw.circle(screen, (255, 255, 255), (ball_xPos, ball_yPos), ball_size)

    for i in range(10):
        for j in range(3):
            pygame.draw.rect(screen, block_color[i][j], blocks[i][j])

    pygame.display.update()

pygame.quit()