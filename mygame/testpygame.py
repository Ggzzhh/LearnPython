#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys

import pygame
from pygame.sprite import Sprite,Group

from bullets import Bullet
from fox import Fox        
        
        
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
    
    #背景图片
    #bg = pygame.image.load('images/bg.jpg')
    
    # 游戏运行主体
    while True:
       
        # 监视键盘
        check_events(screen, fox, bullets)
        
        # 更新六尾位置
        fox.update()
        
        # 更新所有子弹位置
        bullets.update()
        
        # 绘制屏幕
        screen.fill((120, 120, 120))
        #screen.blit(bg, (0,0))
        
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