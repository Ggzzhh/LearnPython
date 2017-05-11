#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys 
from random import randint

import pygame
from pygame.sprite import Sprite, Group


class Star(Sprite):
    
    def __init__(self, screen):
        super().__init__()
        self.screen = screen
        self.image = pygame.image.load('images/star.png')
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()
        
        self.rect.x = self.rect.width
        self.rect.y = -self.rect.height
    
    def blitme(self):
        self.screen.blit(self.image, self.rect)


def create_stars(screen, star, stars):
    
    # 计算行星的数量
    star_width = star.rect.width
    star_height = star.rect.height
    star_space_x = star.screen_rect.width - 2 * star_width
    star_space_y = star.screen_rect.height - 2 * star_height
    number_x = int(star_space_x / (2 * star_width))
    number_rows = int(star_space_y / (2 * star_height))
    
    # 把创建的星星加入组中
    for y_number in range(number_rows):
        for x_number in range(number_x):
            new_star = Star(screen)
            x = randint(1, star_width)
            y = randint(1, star_height)
            new_star.rect.x = x + 2 * star_width * x_number
            new_star.rect.y = y + 3 * star_height * y_number
                    
            stars.add(new_star)

def create_stars_row(screen, star, stars):
    star_width = star.rect.width
    star_space_x = star.screen_rect.width - 2 * star_width
    number_x = int(star_space_x / (2 * star_width))
    for x_number in range(number_x):
        new_star = Star(screen)
        x = randint(1, star_width)
        new_star.rect.x = x + 2 * star_width * x_number
                    
        stars.add(new_star)
    
  
def star_run(screen, star, stars):
    """让星星动起来"""
    for star in stars:
        star.rect.y += randint(1, 10)
        star.rect.x += randint(-20, 20)
        if star.rect.y >= 800:
            stars.remove(star)
        if len(stars) < 60:
            create_stars_row(screen, star, stars)
            
def run_game():
    
    pygame.init()
    
    screen = pygame.display.set_mode((1440, 800))
    pygame.display.set_caption('星星')
    
    star = Star(screen)
    stars = Group()

    create_stars(screen, star, stars)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    sys.exit()
        
        star_run(screen, star, stars)
        screen.fill([230, 80, 105])
        stars.draw(screen)
        pygame.display.flip()

run_game()