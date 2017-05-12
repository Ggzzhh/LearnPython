#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pygame
from pygame.sprite import Group

from settings import Settings
from ship import Ship
import game_functions as gf
from alien import Alien
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard

def run_game():
    # 初始化游戏并创建一个屏幕对象
    pygame.init()  # 初始化游戏
    # 实例化初始设置
    ai_settings = Settings()
    # 根据设置创建一个屏幕以及标题
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption('Alien Invasion (外星人入侵)')
    
    # 创建play按钮
    play_button = Button(ai_settings, screen, 'Play')
    # 创建一个用于储存游戏统计信息的实例 以及记分牌
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)
    
    # 初始化飞船速度 以及 默认出现的位置
    ship = Ship(ai_settings, screen)
    # 创建一个用于储存子弹的编组和一个储存外星人的编组
    bullets = Group()
    aliens = Group()
    # 创建外星人实例
    alien = Alien(ai_settings, screen)
    # 创建外星人群组
    gf.create_fleet(ai_settings, screen, ship,aliens)
    
    # 开始游戏的主循环
    while True:
        # 响应鼠标以及键盘事件
        gf.check_events(ai_settings, screen, stats, sb, play_button, ship, aliens,
            bullets)
        # 更新飞船位置以及事件
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, stats, sb, ship, 
                aliens, bullets)
            gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets)
        # 更新屏幕显示
        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, 
            play_button)
        

# 初始化游戏并开始主循环
run_game()