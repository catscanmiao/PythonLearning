# -*- coding:utf-8 -*-
# !/usr/bin/env python

from random import choice

class RandomWalk():
    
    def __init__(self, num_point=5000):
        self.num_point = num_point
        self.x_value = [0]
        self.y_value = [0]

    def get_step(self):
        

    def fill_walk(self):
        """计算随机漫步包含的所有点"""

        #不断漫步，直到列表达到指定的长度
        while len(self.x_value) < self.num_point:
            
            #决定前进的方向以及沿这个方向前进的距离
            x_direction = choice([1, -1])
            x_distance = choice([0, 1, 2, 3, 4])
            x_step = x_direction * x_distance

            y_direction = choice([1, -1])
            y_distance = choice([0, 1, 2, 3, 4])
            y_step = y_direction * y_distance

            #拒绝原地踏步
            if x_step == 0 and y_step==0:
                continue

            #计算下一个点的x和y值
            next_x = self.x_value[-1] + x_step
            next_y = self.y_value[-1] + y_step

            self.x_value.append(next_x)
            self.y_value.append(next_y)

