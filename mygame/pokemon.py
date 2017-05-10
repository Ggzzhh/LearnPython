#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pygame


class Pokemon(object):
    """关于Pokemon的类"""
    
    def __init__(self, ai_setting, screen):
        """初始化并设置其位置"""
        self.screen = screen
        self.ai_setting = ai_setting
        
        # 读取人物图像以及外接矩形
        self.image = pygame.image.load('images/timg2.jpg')
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()
        
        # 位置
        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery
        
        # 移动标记
        self.moving_left = False
        self.moving_right = False
        self.moving_up = False
        self.moving_down = False
        
        # 接收float类型的数据
        self.centerx = float(self.rect.centerx)
        self.centery = float(self.rect.centery)
        
    #更新pokemon位置
    def update(self):
        """根据移动标记调整人物位置"""
        if self.moving_left and self.rect.left > 0:
            self.centerx -= self.ai_setting.pokemon_speed
        
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.centerx += self.ai_setting.pokemon_speed
    
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.centery += self.ai_setting.pokemon_speed
            
        if self.moving_up and self.rect.top > 0:
            self.centery -= self.ai_setting.pokemon_speed
            
        # 根据self.centerx, self.centery 更新rect对象
        self.rect.centerx = self.centerx
        self.rect.centery = self.centery
     
    def blitme(self):
        """在指定位置绘制人物"""
        self.screen.blit(self.image, self.rect)