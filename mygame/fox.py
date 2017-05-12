#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pygame


class Fox(object):
    """六尾的类"""
    def __init__(self, screen):
        """设置六尾的图片以及默认位置"""
        self.screen = screen
        self.image = pygame.image.load('images/1.png')
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()
        self.speed = 1
        
        # 设置默认位置
        self.rect.left = self.screen_rect.left + 3
        self.rect.centery = self.screen_rect.centery
        
        # 设置移动标记
        self.moving_up = False
        self.moving_down = False
        self.moving_left = False
        self.moving_right = False
        
    def update(self):
        """更新六尾的图片位置"""
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.rect.centery += self.speed
            
        if self.moving_up and self.rect.top > 0:
            self.rect.centery -= self.speed
        
        if self.moving_left and self.rect.left > 0:
            self.rect.centerx -= self.speed
        
        if self.moving_right and self.rect.right < 250:
            self.rect.centerx += self.speed
        
    def blitme(self):
        self.screen.blit(self.image, self.rect)