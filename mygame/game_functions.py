#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys

import pygame


# 响应键盘鼠标事件
def check_events(pokemon):
    # 监视键盘鼠标事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_event(pokemon, event)
        elif event.type == pygame.KEYUP:
            check_keyup_event(pokemon, event)
            
# 响应按下键盘
def check_keydown_event(pokemon, event):
    """根据按键产生不同的结果"""
    if event.key == pygame.K_LEFT:
        pokemon.moving_left = True
    
    elif event.key == pygame.K_RIGHT:
        pokemon.moving_right = True
        
    elif event.key == pygame.K_UP:
        pokemon.moving_up = True
        
    elif event.key == pygame.K_DOWN:
        pokemon.moving_down = True
# 响应弹开键盘
def check_keyup_event(pokemon, event):
    """根据按键产生不同的结果"""
    if event.key == pygame.K_LEFT:
        pokemon.moving_left = False
    
    elif event.key == pygame.K_RIGHT:
        pokemon.moving_right = False
        
    elif event.key == pygame.K_UP:
        pokemon.moving_up = False
        
    elif event.key == pygame.K_DOWN:
        pokemon.moving_down = False