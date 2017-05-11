#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys

import pygame

from bullet import Bullet
from alien import Alien

def check_events(ai_settings, screen, ship, bullets):
    """响应按键和鼠标事件"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
           
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)
            
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)         
            

def check_keydown_events(event, ai_settings, screen, ship, bullets):
    """响应按下键盘的反应"""

    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
            
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
                
    elif event.key == pygame.K_UP:
        ship.moving_up = True
            
    elif event.key == pygame.K_DOWN:
        ship.moving_down = True
        
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)
        
    elif event.key == pygame.K_q:
        sys.exit()

        
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


def get_number_rows(ai_settings, ship_height, alien_height):
    """计算屏幕可以容纳多少行外星人"""
    available_space_y = (ai_settings.screen_height - 
                            (3 * alien_height) - ship_height)
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows
        
        
def get_number_alien_x(ai_settings, alien_width):
    """计算每行容纳的外星人数量"""
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_alien_x = int(available_space_x / (2 * alien_width))
    return number_alien_x


def create_alien(ai_settings, screen, aliens, alien_number, row_number):
    """创建一个外星人并将其加入当前行"""
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    alien.rect.x = alien.x
    aliens.add(alien)

    
def create_fleet(ai_settings, screen, ship, aliens):
    """创建外星人群"""
    # 创建一个外星人 并计算一行能容纳多少外星人
    # 外星人间距为外星人宽度
    alien = Alien(ai_settings, screen)
    number_alien_x = get_number_alien_x(ai_settings, alien.rect.width)
    number_rows = get_number_rows(ai_settings, ship.rect.height,
        alien.rect.height)
    # 创建外星人群
    for row_number in range(number_rows):
        for alien_number in range(number_alien_x):
            create_alien(ai_settings, screen, aliens, alien_number,
                row_number)

            
def update_screen(ai_settings, screen, ship, aliens, bullets):
    """更新屏幕上的图像， 并切换到新屏幕"""
    # 每次循环时都重绘屏幕
    screen.fill(ai_settings.bg_color) # ai_settings 是Settings类的实例
    # 绘制飞船
    ship.blitme()
    aliens.draw(screen)
    # 在飞船和外星人后面重绘所有的子弹
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    
    # 让最近绘制的屏幕可见
    pygame.display.flip()

    
def update_bullets(ai_settings, screen, ship, aliens, bullets):
    """更新子弹位置，并删除已消失的子弹"""
    # 更新子弹位置
    bullets.update()
        
    # 删除已消失的子弹
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
            
    check_bullet_alien_collisions(ai_settings, screen, ship, aliens, bullets)

    
def check_bullet_alien_collisions(ai_settings, screen, ship, aliens, bullets):
    """响应子弹跟外星人碰撞"""
    # 检查是否有子弹击中了外星人
    # 如果是这样 就删除响应的子弹和外星人
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
    
    if len(aliens) == 0:
        # 删除现在已有的子弹并且新建一群外星人
        bullets.empty()
        create_fleet(ai_settings, screen, ship, aliens)

        
def fire_bullet(ai_settings, screen, ship, bullets):
    """如果子弹没有到达极限，就发射一颗子弹"""
    # 创建一颗子弹，并将其加入到编组bullets中
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)


def change_fleet_direction(ai_settings, aliens):
    """整体外星人下移，并改变他们的方向"""
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1

    
def check_fleet_edges(ai_settings, aliens):
    """有外星人到达边缘时采取相应措施"""
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings, aliens)
            break

       
def update_aliens(ai_settings, ship, aliens):
    """更新所有外星人的位置"""
    check_fleet_edges(ai_settings, aliens)
    aliens.update()
    
    # 检测外星人和飞船之间发生碰撞
    if pygame.sprite.spritecollideany(ship, aliens):
        sys.exit()