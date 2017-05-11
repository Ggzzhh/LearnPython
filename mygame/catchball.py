#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
from random import randint

import pygame
from pygame.sprite import Sprite, Group

from settings import Settings


class Seed(Sprite):
    """妙蛙种子的设定"""
    def __init__(self, screen):
        super().__init__()
        self.screen = screen
        
        self.image = pygame.image.load('images/timg2.jpg')
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()
        
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom - 20
        
        self.moving_left = False
        self.moving_right = False
    
    def update(self):
        """控制左右移动"""
        if self.moving_left and self.rect.left >= 0:
            self.rect.centerx -= 2
        if self.moving_right and self.rect.right <= self.screen_rect.right:
            self.rect.centerx += 2

    def blitme(self):
        self.screen.blit(self.image, self.rect)
    

class Fire(Sprite):
    """火球设定"""
    def __init__(self, screen):
        super().__init__()
        self.screen = screen
        
        self.image = pygame.image.load('images/3.png')
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()
        
        self.rect.centerx = randint(0, self.screen_rect.right)
        self.rect.bottom = -self.rect.height
        self.y = float(self.rect.y)
    
    def update(self):
        """控制火球向下移动"""
        self.rect.y += 1

    def blitme(self):
        self.screen.blit(self.image, self.rect)


def check_collisions(seeds, fires, screen):        
        """检测是否发生碰撞或者消失在地图底部 碰撞就删除模型"""
        collisions = pygame.sprite.groupcollide(fires, seeds, True, False)
        for fire in fires:
            if fire.rect.top > 800:
                fires.remove(fire)
                new_fire = Fire(screen)
                fires.add(new_fire)
                print(len(fires))
        
        
def run_game():
    
    pygame.init()
    
    set =Settings()

    
    screen = pygame.display.set_mode(
        (set.screen_width, set.screen_height))
    pygame.display.set_caption('作死小能手')
    seed = Seed(screen)
    fires = Group()
    seeds = Group()
    seeds.add(seed)
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    seed.moving_left = True
                elif event.key == pygame.K_RIGHT:
                    seed.moving_right = True
                elif event.key == pygame.K_q:
                    sys.exit()
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    seed.moving_left = False
                elif event.key == pygame.K_RIGHT:
                    seed.moving_right = False
        
        if len(fires) == 0:
            fire = Fire(screen)
            fires.add(fire)
        
        seed.update()
        fires.update()
        check_collisions(seeds, fires, screen)
        
        screen.fill(set.bg_color)
        seed.blitme()
        fires.draw(screen)
        pygame.display.flip()
    
    
    
if __name__ == "__main__":
    run_game()