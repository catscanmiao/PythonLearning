# -*- coding:utf-8 -*-
# !/usr/bin/env python

class Settings():
    """存储《外星入侵》的所有设置类"""

    def __init__(self):
        """初始化游戏的设置"""
        #设置屏幕
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        #飞船的速度设置
        self.ship_speed_factor = 5