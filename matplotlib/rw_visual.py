# -*- coding:utf-8 -*-
# !/usr/bin/env python

from random_walk import RandomWalk
import matplotlib.pyplot as plt

while True:
    #创建一个RandomWalk实例，并将其点都绘制出来
    rw = RandomWalk()
    rw.fill_walk()

    #设置尺寸
    plt.figure(dpi=128, figsize=(10,6))

    point_numbers = list(range(rw.num_point))
    plt.plot(rw.x_value, rw.y_value, linewidth=1)
    #plt.savefig('x_value.png')
    plt.plot(0, 0, linewidth=5)
    plt.plot(rw.x_value[-1], rw.y_value[-1], linewidth=5)

    #隐藏坐标轴
    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)

    plt.show()
    
    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n':
        break
    