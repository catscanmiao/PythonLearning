# -*- coding:utf-8 -*-
# !/usr/bin/env python

import pygame

class Ship()

    def __init__(self, screen):
        """初始化飞船并设置初始位置"""
        self.screen = screen

        #加载飞船图像并获取其外形矩形
        self.image = pygame.image.load