# -*- coding:utf-8 -*-
# !/usr/bin/env python

import pygame

class Ship():

    def __init__(self, screen):
        """初始化飞船并设置初始位置"""
        self.screen = screen

        #加载飞船图像并获取其外形矩形
        self.image = pygame.image.load("image/ship.bmp")
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        #将飞船放在屏幕底部中央
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom


    def blitme(self):
        """指定位置绘制飞船"""
        self.screen.blit(self.image, self.rect)