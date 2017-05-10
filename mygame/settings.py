#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Settings(object):
    """游戏默认设定"""
    
    def __init__(self):
        self.screen_width = 1200  # 设置屏幕宽
        self.screen_height = 800  # 设置屏幕高
        self.bg_color = (135, 206, 250)    # 设置屏幕颜色
        
        # 移动速度
        self.pokemon_speed = 1.5