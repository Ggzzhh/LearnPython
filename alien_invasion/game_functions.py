#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys

import pygame

def check_events(ship):
    """响应按键和鼠标事件"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
           
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ship)
            
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)         
            

def check_keydown_events(event, ship):
    """响应按下键盘的反应"""

    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
            
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
                
    elif event.key == pygame.K_UP:
        ship.moving_up = True
            
    elif event.key == pygame.K_DOWN:
        ship.moving_down = True


def check_keyup_events(event, ship):
    """响应松开键盘"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
                
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False

    elif event.key == pygame.K_UP:
        ship.moving_up = False
            
    elif event.key == pygame.K_DOWN:
        ship.moving_down = False      
        
def update_screen(ai_settings, screen, ship):
    """更新屏幕上的图像， 并切换到新屏幕"""
    # 每次循环时都重绘屏幕
    screen.fill(ai_settings.bg_color) # ai_settings 是Settings类的实例
    # 绘制飞船
    ship.blitme()
    
    # 让最近绘制的屏幕可见
    pygame.display.flip()