#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pygame

from settings import Settings
from pokemon import Pokemon
import game_functions as gf

def run_game():
    """初始化游戏"""
    pygame.init()
    
    ai_setting = Settings()
    
    # 设置屏幕大小以及标题
    screen = pygame.display.set_mode(
        (ai_setting.screen_width, ai_setting.screen_height))
    pygame.display.set_caption('游戏名：xxxxx')
    
    # 实例化pokemon
    pokemon = Pokemon(ai_setting, screen)
    
    # 开始游戏的主循环
    while True:
        
        # 调用game_functions
        gf.check_events(pokemon)
        # 更新pokemon位置
        pokemon.update()
        # 填充屏幕
        screen.fill(ai_setting.bg_color)
        pokemon.blitme()

        # 不断刷新屏幕
        pygame.display.flip()
        
if __name__ == '__main__':

    run_game()