#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from random import randint

import pygame
from pygame.sprite import Sprite

class Enemys(Sprite):
    """管理敌人的类"""
    def __init__(self, screen):
        super().__init__()
        self.screen = screen
        
        # 创建一个敌人图像并定位
        self.image = pygame.image.load('images/x1.png')
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()
        
        self.rect.right = self.screen_rect.right + self.rect.width
        self.rect.centery = randint(self.rect.height, (700 - self.rect.height))
        
        self.x = float(self.rect.x)
        
        # 创建一根线  敌人到达的目的地
        self.line_rect = pygame.Rect(0, 0, 1, 700)
        self.line_rect.x = 250
        self.line_rect.y = 0
    
    
    def update(self):
        """让敌人向前移动"""
        self.x -= 1
        self.rect.x = self.x
        
    def blitme(self, screen):
        """绘制敌人跟线"""
        self.screen.fill((255, 255, 255), self.line_rect)
        self.screen.blit(self.image, self.rect)
        