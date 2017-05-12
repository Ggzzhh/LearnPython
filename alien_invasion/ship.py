#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pygame


class Ship(object):
    """关于飞船的类"""
    
    def __init__(self, ai_settings, screen):
        """初始化飞船并设置其位置"""
        self.screen = screen
        self.ai_settings = ai_settings
        
        # 加载飞船图像并获取其外接矩形
        self.image = pygame.image.load('images/ship.bmp') # 读取飞船图像
        self.rect = self.image.get_rect() # 获取飞船外接矩形
        self.screen_rect = screen.get_rect() # 储存表示屏幕的矩形
        
        # 将每艘新飞船放在屏幕的底部中央
        self.rect.centerx = self.screen_rect.centerx # 飞船的中心位置 在屏幕的中心位置
        self.rect.bottom = self.screen_rect.bottom # 飞船的底部 在屏幕的底部
    
        # 在飞船的属性center中储存小数值
        self.centerx = float(self.rect.centerx)
        self.centery = float(self.rect.centery)
        
        
        # 移动标志
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False
    
    def update(self):
        """根据移动标志调整飞船位置"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            # 向右移动飞船
            self.centerx += self.ai_settings.ship_speed_factor
        
        if self.moving_left and self.rect.left > 0:
            # 向左移动飞船
            self.centerx -= self.ai_settings.ship_speed_factor
        
        if self.moving_up and self.rect.top > 0:
            # 向上移动飞船
            self.centery -= self.ai_settings.ship_speed_factor
        
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            # 向下移动飞船
            self.centery += self.ai_settings.ship_speed_factor
        
        # 根据self.centerx, self.centery 更新rect对象
        self.rect.centerx = self.centerx
        self.rect.centery = self.centery
    
    def blitme(self):
        """在制定位置绘制飞船"""
        self.screen.blit(self.image, self.rect)
    

    def center_ship(self):
        """让飞船在屏幕上居中"""
        self.centerx = self.screen_rect.centerx # 飞船的中心位置 在屏幕的中心位置
        self.centery = self.screen_rect.bottom - 20

        