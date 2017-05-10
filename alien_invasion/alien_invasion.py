#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pygame
from pygame.sprite import Group

from settings import Settings
from ship import Ship
import game_functions as gf

def run_game():
    # 初始化游戏并创建一个屏幕对象
    pygame.init()  # 初始化游戏
    # 实例化初始设置
    ai_settings = Settings()
    # 根据设置创建一个屏幕以及标题
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption('Alien Invasion (外星人入侵)')
    
    # 初始化飞船速度 以及 默认出现的位置
    ship = Ship(ai_settings, screen)
    # 创建一个用于储存子弹的编组
    bullets = Group()
    
    # 开始游戏的主循环
    while True:
        # 响应鼠标以及键盘事件
        gf.check_events(ai_settings, screen, ship, bullets)
        # 更新飞船位置以及事件
        ship.update()
        gf.update_bullets(bullets)
        # 更新屏幕显示
        gf.update_screen(ai_settings, screen, ship, bullets)
        

# 初始化游戏并开始主循环
run_game()