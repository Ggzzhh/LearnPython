#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys

import pygame
from pygame.sprite import Sprite,Group

class Bullet(Sprite):
    """管理子弹的类"""
    def __init__(self, screen, fox):
        """在狐狸所在的位置创建一个子弹"""
        super().__init__()
        self.screen = screen
        
        self.image = pygame.image.load('images/2.jpg')
        self.rect = self.image.get_rect()
        #self.rect = pygame.Rect(0, 0, 15, 3)
        self.rect.centery = fox.rect.centery
        self.rect.left = fox.rect.right
        
        # 储存用小数表示的子弹位置
        self.x = float(self.rect.x)
        self.color = (255, 105, 180)
        
    def update(self):
        """向右移动子弹"""
        self.x += 0.5
        # 更新子弹位置
        self.rect.x = self.x
        
    def draw_bullet(self):
        """绘制子弹"""
        #pygame.draw.rect(self.screen, self.color, self.rect)
        self.screen.blit(self.image, self.rect)
        
        
class Fox(object):
    """六尾的类"""
    def __init__(self, screen):
        """设置六尾的图片以及默认位置"""
        self.screen = screen
        self.image = pygame.image.load('images/1.png')
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()
        
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
            self.rect.centery += 1
            
        if self.moving_up and self.rect.top > 0:
            self.rect.centery -= 1
        
        if self.moving_left and self.rect.left > 0:
            self.rect.centerx -= 1
        
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.rect.centerx += 1
        
    def blitme(self):
        self.screen.blit(self.image, self.rect)

        
def check_events(screen, fox, bullets):
    """根据键盘的动作进行反映"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                fox.moving_up = True
                
            elif event.key == pygame.K_DOWN:
                fox.moving_down = True
            
            elif event.key == pygame.K_LEFT:
                fox.moving_left = True

            elif event.key == pygame.K_RIGHT:
                fox.moving_right = True
                
            elif event.key == pygame.K_SPACE:
                """创建一颗子弹"""
                new_bullet = Bullet(screen, fox)
                bullets.add(new_bullet)
                
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                fox.moving_up = False
                
            elif event.key == pygame.K_DOWN:
                fox.moving_down = False
                
            elif event.key == pygame.K_LEFT:
                fox.moving_left = False

            elif event.key == pygame.K_RIGHT:
                fox.moving_right = False

def run_game():
    """运行游戏的主题"""
    pygame.init()
    
    # 创建屏幕
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption('横向射击')
    
    # 创建一个六尾实例
    fox = Fox(screen)
    # 创建一个用于储存子弹的组
    bullets = Group()
    
    # 游戏运行主体
    while True:
       
        # 监视键盘
        check_events(screen, fox, bullets)
        
        # 更新六尾位置
        fox.update()
        
        # 更新所有子弹位置
        bullets.update()
        
        # 绘制屏幕
        screen.fill((255, 255, 255))
        
        # 绘制fox
        fox.blitme()
        
        # 绘制子弹
        for bullet in bullets.sprites():
            bullet.draw_bullet()
        
        # 删除已经消失的子弹
        for bullet in bullets.copy():
            if bullet.rect.left >= fox.screen_rect.right:
                bullets.remove(bullet)
        
        # 让最近绘制的东西显示
        pygame.display.flip()
       
run_game()