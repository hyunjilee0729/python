# -*- coding: utf-8 -*-
import pygame
pygame.init()

screen_with = 480
screen_height = 640
scrren = pygame.display.set_mode((screen_with, screen_height ))

pygame.display.set_caption("똥피하기 - 코드플레이")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False 
            # print("ㅈ...ㅜㄱ...ㅇ ㅕ.....ㅈ..ㅝ...")
pygame.quit() 