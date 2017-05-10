#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys

import pygame

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
    
    # 开始游戏的主循环
    while True:
        # 响应鼠标以及键盘事件
        gf.check_events(ship)
        # 更新飞船位置以及事件
        ship.update()
        # 更新屏幕显示
        gf.update_screen(ai_settings, screen, ship)
        

# 初始化游戏并开始主循环
run_game()