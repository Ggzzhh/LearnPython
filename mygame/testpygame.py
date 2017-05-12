#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
from time import sleep

import pygame
from pygame.sprite import Sprite,Group

from bullets import Bullet
from fox import Fox
from enemy import Enemys    
from button import Button   
        

start_game = False
run_enemy = 3  
      
def check_events(screen, fox, bullets, play):
    """根据键盘鼠标的动作进行反映"""
    global start_game, run_enemy
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            button_clicked = play.rect.collidepoint(mouse_x, mouse_y)
            if button_clicked and not start_game:
                # 隐藏鼠标
                pygame.mouse.set_visible(False)
                start_game = True
                sleep(0.5)
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
            elif event.key == pygame.K_q:
                sys.exit()
                
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                fox.moving_up = False
                
            elif event.key == pygame.K_DOWN:
                fox.moving_down = False
                
            elif event.key == pygame.K_LEFT:
                fox.moving_left = False

            elif event.key == pygame.K_RIGHT:
                fox.moving_right = False


def creat_enemy(screen, enemys):
    # 创建一个敌人
    global run_enemy            
    enemy = Enemys(screen)
    enemys.add(enemy)
    
    
def run_game():
    """运行游戏的主题"""
    pygame.init()
    global start_game, run_enemy
    # 创建屏幕
    screen = pygame.display.set_mode((1000, 700))
    pygame.display.set_caption('横向射击')
    
    # 创建一个六尾实例
    fox = Fox(screen)
    # 创建一个用于储存子弹的组
    bullets = Group()
    # 敌人
    enemys = Group()
    #背景图片
    #bg = pygame.image.load('images/bg.jpg')
    
    # 游戏状态

    play = Button(screen, 'play')
    # 游戏运行主体
    while True:
        
        # 监视键盘
        check_events(screen, fox, bullets, play)
        # 监视鼠标
        if not start_game:
            pygame.mouse.set_visible(True)
            screen.fill((120, 120, 120))
            play.draw_button()
            pygame.display.flip()
            continue
        else:
            pass
            
        # 如果敌人数量不足1 就创造一个
        if len(enemys) < 1:
            creat_enemy(screen, enemys)
        
        # 更新六尾位置
        fox.update()
        # 更新敌人位置
        enemys.update()
        # 监测敌人是否超过线 超过线就删除 然后生命-1  为0 则退出游戏
        for enemy in enemys.sprites(): 
            if enemy.rect.centerx == 250:
                enemys.remove(enemy)
                run_enemy -= 1
                if run_enemy < 0:
                    start_game = False
        # 更新所有子弹位置
        bullets.update()
        
        # 绘制屏幕
        screen.fill((120, 120, 120))
        #screen.blit(bg, (0,0))
        
        # 绘制fox
        fox.blitme()
        for enemy in enemys.sprites():
            enemy.blitme(screen)

        
        # 绘制子弹
        for bullet in bullets.sprites():
            bullet.draw_bullet()
        
        # 监测子弹跟敌人是否发生碰撞 碰撞就删除
        pygame.sprite.groupcollide(bullets, enemys, True, True)
        
        
        # 删除已经消失的子弹
        for bullet in bullets.copy():
            if bullet.rect.left >= fox.screen_rect.right:
                bullets.remove(bullet)
        
        # 让最近绘制的东西显示
        pygame.display.flip()
       
run_game()