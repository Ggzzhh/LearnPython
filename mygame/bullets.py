#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import time

import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """管理子弹的类"""
    def __init__(self, screen, fox):
        """在狐狸所在的位置创建一个子弹"""
        super().__init__()
        self.screen = screen
        
        self.image = pygame.image.load('images/2.png')
        self.rect = self.image.get_rect()
        #self.rect = pygame.Rect(0, 0, 15, 3)
        self.rect.centery = fox.rect.centery
        self.rect.left = fox.rect.right
        # 储存用小数表示的子弹位置
        self.x = float(self.rect.x)
        self.color = (255, 105, 180)
        
    def update(self):
        """向右移动子弹"""
        self.x += 2
        # 更新子弹位置
        self.rect.x = self.x
        
    def draw_bullet(self):
        """绘制子弹"""
        #pygame.draw.rect(self.screen, self.color, self.rect)
        self.screen.blit(self.image, self.rect)